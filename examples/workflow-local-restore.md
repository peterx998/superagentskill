# Workflow: Local Restore

This example restores one repository skill into a local Codex skills directory. Replace placeholders with your own paths.

## Inputs

```text
Repository path: <path-to-repo>
Skill name: <skill-folder-name>
Local Codex skills directory: <path-to-local-codex-skills>
```

## Command Shape

```powershell
Copy-Item -Recurse "<path-to-repo>\skills\<skill-folder-name>" "<path-to-local-codex-skills>\<skill-folder-name>"
```

## After Restore

1. Restart Codex or open a new session.
2. Search for the skill by natural-language trigger phrase.
3. Confirm the restored skill is discoverable.

## Notes

If a skill with the same name already exists locally, compare the two folders before replacing anything. Preserve local-only notes or copy them into a clearly named backup location.
