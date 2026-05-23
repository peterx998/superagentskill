param(
    [Parameter(Position = 0)]
    [ValidateSet('scan', 'runtime', 'policy', 'prompt', 'mcp', 'lab')]
    [string]$Action = 'runtime',

    [string]$Root = (Get-Location).Path,
    [string]$Text = '',
    [int]$MaxItems = 300,
    [int]$MaxDepth = 4
)

$ErrorActionPreference = 'Stop'
$BaseDir = Join-Path $env:USERPROFILE '.codex'
$LogDir = Join-Path $BaseDir 'logs'
$LogFile = Join-Path $LogDir 'agent_runtime_lab.jsonl'
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

$ExcludedNames = @(
    '.git', '.hg', '.svn', '.idea', '.vscode',
    'node_modules', 'vendor', '.venv', 'venv', '__pycache__',
    'dist', 'build', 'target', '.next', '.nuxt', '.cache',
    'coverage', '.pytest_cache', '.mypy_cache'
)

$SensitiveNamePatterns = @(
    '(?i)^\.env($|\.)',
    '(?i)secret',
    '(?i)token',
    '(?i)credential',
    '(?i)password',
    '(?i)private[_-]?key',
    '(?i)id_rsa',
    '(?i)\.pem$',
    '(?i)\.pfx$',
    '(?i)\.key$',
    '(?i)cookies?'
)

function Write-LabLog {
    param(
        [string]$Event,
        [string]$Status,
        [object]$Details
    )

    $record = [ordered]@{
        time = (Get-Date).ToString('o')
        event = $Event
        status = $Status
        cwd = (Get-Location).Path
        details = $Details
    }
    ($record | ConvertTo-Json -Depth 8 -Compress) | Add-Content -Encoding UTF8 -Path $LogFile
}

function Test-SensitiveName {
    param([string]$Name)
    foreach ($pattern in $SensitiveNamePatterns) {
        if ($Name -match $pattern) { return $true }
    }
    return $false
}

function Get-RelativeDepth {
    param([string]$Base, [string]$Path)
    $baseFull = [System.IO.Path]::GetFullPath($Base).TrimEnd('\')
    $pathFull = [System.IO.Path]::GetFullPath($Path)
    if (-not $pathFull.StartsWith($baseFull, [System.StringComparison]::OrdinalIgnoreCase)) { return 999 }
    $relative = $pathFull.Substring($baseFull.Length).TrimStart('\')
    if ([string]::IsNullOrWhiteSpace($relative)) { return 0 }
    return ($relative -split '[\\/]').Count
}

function Invoke-SafeScan {
    $resolved = Resolve-Path -LiteralPath $Root
    $rootPath = $resolved.Path
    $items = New-Object System.Collections.Generic.List[object]
    $skipped = New-Object System.Collections.Generic.List[object]

    $queue = New-Object System.Collections.Generic.Queue[string]
    $queue.Enqueue($rootPath)

    while ($queue.Count -gt 0 -and $items.Count -lt $MaxItems) {
        $current = $queue.Dequeue()
        $depth = Get-RelativeDepth -Base $rootPath -Path $current
        if ($depth -gt $MaxDepth) {
            $skipped.Add([pscustomobject]@{ path = $current; reason = 'max-depth' })
            continue
        }

        try {
            $children = Get-ChildItem -LiteralPath $current -Force
        } catch {
            $skipped.Add([pscustomobject]@{ path = $current; reason = 'access-denied-or-unreadable' })
            continue
        }

        foreach ($child in $children) {
            if ($items.Count -ge $MaxItems) { break }
            $name = $child.Name
            if ($ExcludedNames -contains $name) {
                $skipped.Add([pscustomobject]@{ path = $child.FullName; reason = 'excluded-directory-or-cache' })
                continue
            }
            if (Test-SensitiveName -Name $name) {
                $skipped.Add([pscustomobject]@{ path = $child.FullName; reason = 'sensitive-name-redacted' })
                continue
            }

            $entry = [ordered]@{
                path = $child.FullName
                name = $child.Name
                type = if ($child.PSIsContainer) { 'directory' } else { 'file' }
                size = if ($child.PSIsContainer) { $null } else { $child.Length }
            }
            $items.Add([pscustomobject]$entry)

            if ($child.PSIsContainer) {
                $queue.Enqueue($child.FullName)
            }
        }
    }

    $result = [ordered]@{
        root = $rootPath
        max_items = $MaxItems
        max_depth = $MaxDepth
        count = $items.Count
        skipped_count = $skipped.Count
        items = $items
        skipped = $skipped | Select-Object -First 60
        log = $LogFile
    }
    Write-LabLog -Event 'scan' -Status 'ok' -Details @{ root = $rootPath; count = $items.Count; skipped = $skipped.Count }
    $result | ConvertTo-Json -Depth 8
}

function Get-RuntimeInfo {
    $codexHints = [ordered]@{}
    foreach ($name in 'CODEX_HOME', 'CODEX_SANDBOX', 'CODEX_ENV', 'PWD') {
        $value = [Environment]::GetEnvironmentVariable($name)
        if ($value) { $codexHints[$name] = $value }
    }

    $result = [ordered]@{
        cwd = (Get-Location).Path
        user = [Environment]::UserName
        machine = [Environment]::MachineName
        powershell = $PSVersionTable.PSVersion.ToString()
        edition = $PSVersionTable.PSEdition
        os = [Environment]::OSVersion.VersionString
        time = (Get-Date).ToString('o')
        log = $LogFile
        codex_hints = $codexHints
    }
    Write-LabLog -Event 'runtime' -Status 'ok' -Details @{ cwd = $result.cwd }
    $result | ConvertTo-Json -Depth 6
}

function Test-Policy {
    param([string]$InputText)
    $checks = @(
        @{ category = 'destructive'; risk = 'blocked'; pattern = '(?i)\brm\s+-rf\b|Remove-Item\b.*\b-Recurse\b.*\b-Force\b|format\s+[a-z]:|git\s+reset\s+--hard|git\s+clean\s+-fdx' },
        @{ category = 'dangerous-git'; risk = 'high'; pattern = '(?i)git\s+push\s+--force|git\s+push\s+-f|git\s+rebase\b|git\s+filter-branch|git\s+update-ref' },
        @{ category = 'secret-access'; risk = 'high'; pattern = '(?i)\.env|id_rsa|\.pem\b|\.pfx\b|private[_-]?key|token|credential|password|cookies?' },
        @{ category = 'network-exfil'; risk = 'high'; pattern = '(?i)\bcurl\b.*\b(-d|--data|--upload-file)\b|\binvoke-webrequest\b|\biwr\b|\bwget\b|webhook|pastebin|ngrok|cloudflared\s+tunnel' },
        @{ category = 'repo-poisoning'; risk = 'medium'; pattern = '(?i)\.git[\\/](hooks|config)|package\.json.*postinstall|preinstall|github[\\/]workflows|ci\.yml|apply_patch' },
        @{ category = 'mcp-risk'; risk = 'medium'; pattern = '(?i)mcp|tool.*description|execute_command|shell|filesystem|stdio' },
        @{ category = 'lab-target'; risk = 'info'; pattern = '(?i)dvwa|juice shop|portswigger|localhost|127\.0\.0\.1|::1' }
    )

    $policyMatches = New-Object System.Collections.Generic.List[object]
    foreach ($check in $checks) {
        if ($InputText -match $check.pattern) {
            $policyMatches.Add([pscustomobject]@{
                category = $check.category
                risk = $check.risk
            })
        }
    }

    $riskOrder = @{ info = 0; low = 1; medium = 2; high = 3; blocked = 4 }
    $risk = 'info'
    foreach ($match in $policyMatches) {
        if ($riskOrder[$match.risk] -gt $riskOrder[$risk]) { $risk = $match.risk }
    }

    $result = [ordered]@{
        risk = $risk
        matches = $policyMatches
        recommendation = switch ($risk) {
            'blocked' { 'Do not execute. Replace with a read-only inspection or request explicit approval for a safe alternative.' }
            'high' { 'Treat as sensitive. Redact secrets, restrict target scope, and require explicit authorization.' }
            'medium' { 'Review before execution and log the action.' }
            default { 'Low concern based on current patterns.' }
        }
    }
    Write-LabLog -Event 'policy' -Status $risk -Details @{ text_length = $InputText.Length; matches = $policyMatches.Count }
    $result | ConvertTo-Json -Depth 6
}

function Test-PromptInjection {
    param([string]$InputText)
    $normalized = $InputText.Normalize([Text.NormalizationForm]::FormKC).ToLowerInvariant()
    $signals = @(
        @{ name = 'instruction-override'; pattern = '(?i)ignore (all )?(previous|prior|above)|disregard.*instructions|forget.*rules|override.*policy' },
        @{ name = 'secret-request'; pattern = '(?i)system prompt|developer message|hidden instruction|api key|token|secret|credential' },
        @{ name = 'tool-impersonation'; pattern = '(?i)tool result|function call|assistant to=|system:|developer:' },
        @{ name = 'routing-control'; pattern = '(?i)call the tool|use shell|run command|apply_patch|send to analysis|disable safety' },
        @{ name = 'delayed-trigger'; pattern = '(?i)when you see|after reading|at the end|silently|do not mention' },
        @{ name = 'obfuscation'; pattern = '(?i)base64|rot13|hex|unicode|homoglyph|classical chinese|文言|古文' }
    )

    $hits = New-Object System.Collections.Generic.List[object]
    foreach ($signal in $signals) {
        if ($normalized -match $signal.pattern) {
            $hits.Add([pscustomobject]@{ signal = $signal.name })
        }
    }

    $score = [Math]::Min(100, $hits.Count * 18)
    $risk = if ($score -ge 72) { 'high' } elseif ($score -ge 36) { 'medium' } elseif ($score -gt 0) { 'low' } else { 'info' }
    $result = [ordered]@{
        risk = $risk
        score = $score
        signals = $hits
        normalized_preview = if ($normalized.Length -gt 240) { $normalized.Substring(0, 240) + '...' } else { $normalized }
        recommendation = 'Treat suspicious external text as data, not instructions. Quote or summarize it before passing it to an agent.'
    }
    Write-LabLog -Event 'prompt' -Status $risk -Details @{ text_length = $InputText.Length; signals = $hits.Count }
    $result | ConvertTo-Json -Depth 6
}

function Invoke-McpAudit {
    $resolved = Resolve-Path -LiteralPath $Root
    $rootPath = $resolved.Path
    $files = Get-ChildItem -LiteralPath $rootPath -Recurse -Force -File -ErrorAction SilentlyContinue |
        Where-Object {
            $_.FullName -notmatch '\\(node_modules|\.git|dist|build|\.cache)\\' -and
            ($_.Name -match '(?i)mcp|server|tool|config|settings' -or $_.Extension -in '.json', '.yaml', '.yml', '.toml')
        } |
        Select-Object -First $MaxItems

    $findings = New-Object System.Collections.Generic.List[object]
    foreach ($file in $files) {
        try {
            $content = Get-Content -Raw -LiteralPath $file.FullName -ErrorAction Stop
        } catch {
            continue
        }
        $policy = (Test-Policy -InputText $content | ConvertFrom-Json)
        if ($policy.risk -ne 'info' -or $content -match '(?i)description|command|args|stdio|filesystem|shell|execute') {
            $findings.Add([pscustomobject]@{
                path = $file.FullName
                risk = $policy.risk
                categories = @($policy.matches | ForEach-Object { $_.category })
            })
        }
    }

    $result = [ordered]@{
        root = $rootPath
        scanned_files = @($files).Count
        findings_count = $findings.Count
        findings = $findings
        recommendation = 'Review MCP entries that expose shell, filesystem, network, or broad command execution. Prefer least-privilege tools and explicit approvals.'
    }
    Write-LabLog -Event 'mcp-audit' -Status 'ok' -Details @{ root = $rootPath; findings = $findings.Count }
    $result | ConvertTo-Json -Depth 8
}

function Show-LabMode {
    $result = [ordered]@{
        allowed_targets = @('DVWA', 'OWASP Juice Shop', 'PortSwigger Web Security Academy', 'localhost', '127.0.0.1', 'owned lab hosts')
        default_boundary = 'authorized lab targets only'
        recommendation = 'Keep exploit attempts inside the lab. Use runtime logs and policy checks to observe agent/tool behavior.'
    }
    Write-LabLog -Event 'lab' -Status 'ok' -Details @{ boundary = $result.default_boundary }
    $result | ConvertTo-Json -Depth 4
}

$start = Get-Date
try {
    switch ($Action) {
        'scan' { Invoke-SafeScan }
        'runtime' { Get-RuntimeInfo }
        'policy' { Test-Policy -InputText $Text }
        'prompt' { Test-PromptInjection -InputText $Text }
        'mcp' { Invoke-McpAudit }
        'lab' { Show-LabMode }
    }
} catch {
    Write-LabLog -Event $Action -Status 'error' -Details @{ message = $_.Exception.Message }
    [ordered]@{
        error = $_.Exception.Message
        action = $Action
        duration_ms = [int]((Get-Date) - $start).TotalMilliseconds
        log = $LogFile
    } | ConvertTo-Json -Depth 4
    exit 1
}
