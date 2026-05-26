# Codex Integration

Status: supported

## Expected Target Directory

Use your local Codex skills directory, commonly:

```text
<user-home>/.codex/skills
```

## Manual Installation Idea

Copy one skill folder from `skills/` into the local Codex skills directory, then restart Codex or open a new session.

```powershell
Copy-Item -Recurse ".\skills\<skill-folder-name>" "<user-home>\.codex\skills\<skill-folder-name>"
```

## Future Automation Plan

- Add a safe restore script with dry-run mode.
- Detect existing target folders before copying.
- Produce a clear diff or backup note when local content already exists.
- Validate that each restored skill contains `SKILL.md`.
