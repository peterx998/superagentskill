param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$PromptParts
)

$Prompt = ($PromptParts -join ' ').ToLowerInvariant()
$BaseDir = Join-Path $env:USERPROFILE '.codex'
$LogDir = Join-Path $BaseDir 'logs'
$LogFile = Join-Path $LogDir 'enhanced_skill.log'
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

function Write-SkillLog($Message) {
    $timestamp = (Get-Date).ToString('o')
    Add-Content -Encoding UTF8 -Path $LogFile -Value "[$timestamp] $Message"
}

function Show-Workspace {
    $cwd = (Get-Location).Path
    $items = Get-ChildItem -Force | Select-Object -ExpandProperty Name
    Write-SkillLog "Workspace scanned: $cwd"
    [pscustomobject]@{
        cwd = $cwd
        files = $items
        count = @($items).Count
    } | ConvertTo-Json -Depth 4
}

function Show-RuntimeInfo {
    Write-SkillLog 'Runtime info requested.'
    [pscustomobject]@{
        cwd = (Get-Location).Path
        powershell = $PSVersionTable.PSVersion.ToString()
        platform = $PSVersionTable.Platform
        os = $PSVersionTable.OS
        time = (Get-Date).ToString('o')
    } | ConvertTo-Json -Depth 4
}

Write-SkillLog "Skill triggered with prompt: $Prompt"

if ($Prompt -match 'runtime') { Show-RuntimeInfo; exit }
if ($Prompt -match 'scan|files|project') { Show-Workspace; exit }
if ($Prompt -match 'whoami') { whoami; Write-SkillLog 'Executed safe command: whoami'; exit }
if ($Prompt -match 'pwd') { (Get-Location).Path; Write-SkillLog 'Executed safe command: pwd'; exit }
if ($Prompt -match '\bls\b|dir') { Get-ChildItem -Force | Select-Object -ExpandProperty Name; Write-SkillLog 'Executed safe command: list files'; exit }

Write-Output 'Enhanced Local Skill active.'
Write-Output 'Available actions:'
Write-Output '- scan workspace'
Write-Output '- show runtime info'
Write-Output '- whoami'
Write-Output '- pwd'
Write-Output '- ls / dir'
