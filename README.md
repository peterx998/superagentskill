# superagentSkills

Local backup of installed Codex skills from `C:\Users\LENOVO\.codex\skills`.

## Contents

- `skills/` contains the installed skill folders copied from the local Codex skills directory.
- System skills under `skills/.system/` are included because they are part of the local installed skills tree.
- Log files, environment files, obvious secret/token/cookie files, dependency caches, and nested Git metadata are intentionally excluded from this backup.

## Restore

Copy a skill folder from `skills/` into:

```powershell
C:\Users\LENOVO\.codex\skills
```

Restart Codex or open a new session after restoring or adding skills so Codex rescans them.
