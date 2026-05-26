# Scripts

This directory contains small maintenance scripts for the skills library.

## build catalog

`build_skill_catalog.py`

Rebuilds catalog files from available skill sources. Run this after adding, renaming, removing, or materially changing skill metadata.

```powershell
python scripts/build_skill_catalog.py
```

## query skills

`query_skills.py`

Searches the generated catalog with a natural-language query and returns likely skill matches.

```powershell
python scripts/query_skills.py "报错 跑不起来"
```

## sync descriptions

`sync_skill_descriptions.py`

Syncs optimized trigger descriptions from local installed skills back into matching repository skill folders.

Review changes before committing.

## validate repo

`validate_repo.py`

Checks required public-release files and directories. It also warns when installable-looking skill folders do not contain `SKILL.md`.

```powershell
python scripts/validate_repo.py
```

## Cleanup Rules

- Preserve existing skill files and catalog files.
- Do not delete docs unless replacing them with a better file and linking old paths.
- Do not copy content from unrelated repositories.
- Do not add fake stars, sponsors, community claims, or production claims.
