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

## Natural-Language Skill Routing

This private repository indexes local Codex skills so an assistant can route natural-language requests to the right skill without requiring the user to remember skill names.

## Files

- `catalog/skills.json`: full structured database.
- `catalog/preferred-skills.json`: de-duplicated best source per skill name.
- `catalog/skills.jsonl`: one skill per line for ingestion.
- `catalog/skills.csv`: spreadsheet-friendly inventory.
- `catalog/skills.sqlite`: SQLite database with FTS5 full-text search.
- `catalog/keyword_index.json`: keyword to skill-id inverted index.
- `catalog/category_index.md`: human-readable category map.
- `docs/skill-routing-policy.md`: routing policy and tie breakers.
- `scripts/query_skills.py`: local natural-language query helper.

## Query Example

```powershell
& 'C:\Users\LENOVO\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts\query_skills.py '报错 跑不起来 帮我排查'
```

## Design

The database is trigger-first: descriptions and search fields describe when to use a skill, not the workflow inside the skill. Chinese trigger phrases are included for common local usage.

