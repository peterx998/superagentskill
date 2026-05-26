# Workflow: Catalog Rebuild

This example shows the command flow for rebuilding local catalog files.

## When to Use

Rebuild the catalog after:

- adding a skill
- renaming a skill folder
- changing `SKILL.md` trigger descriptions
- changing catalog generation logic

## Command Flow

```powershell
python scripts/build_skill_catalog.py
python scripts/validate_repo.py
python scripts/query_skills.py "example routing phrase"
```

## Review

Check generated changes under `catalog/` and confirm they reflect the intended metadata update.

Do not include private cache content in a public release unless it is intentionally part of the repository and safe to publish.
