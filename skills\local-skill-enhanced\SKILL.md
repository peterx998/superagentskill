---
name: local-skill-enhanced
description: Inspect the local Codex workspace and run safe local diagnostics. Use when the user asks to show project files, list files, scan the workspace, show runtime info, run local diagnostics, check whoami, print the current directory, or perform basic safe shell-routing experiments from a local skill package.
---

# Local Skill Enhanced

Use this skill to inspect the current local workspace and answer simple runtime-diagnostic requests.

## Workflow

1. Identify the requested diagnostic: workspace scan, file listing, runtime info, current user, current directory, or a safe command check.
2. Prefer Codex's normal shell/file tools for direct inspection when they are available.
3. Use `scripts/enhanced_local_skill.ps1` when a deterministic helper is useful on Windows.
4. Use `scripts/enhanced_local_skill.py` only when Python is available; it is preserved from the imported package.
5. Keep commands read-only unless the user explicitly asks for a change.
6. Summarize the relevant result instead of dumping long raw listings.

## Helper Usage

PowerShell helper examples:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/enhanced_local_skill.ps1 "scan workspace"
powershell -ExecutionPolicy Bypass -File scripts/enhanced_local_skill.ps1 "show runtime info"
powershell -ExecutionPolicy Bypass -File scripts/enhanced_local_skill.ps1 "whoami"
powershell -ExecutionPolicy Bypass -File scripts/enhanced_local_skill.ps1 "pwd"
```

The helper only supports these actions:

- `scan workspace` or `show project files`
- `show runtime info`
- `whoami`
- `pwd`
- `ls` / `dir`

## Logging

The helpers write lightweight logs to `%USERPROFILE%\.codex\logs\enhanced_skill.log`. Do not rely on logs as the final answer; use them only for troubleshooting helper behavior.
