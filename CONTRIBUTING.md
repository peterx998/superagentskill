# Contributing to superagentSkills

Thanks for helping improve this Codex skills library. Contributions should make skills easier to find, safer to restore, and clearer to maintain.

## Types of Contributions

- Add a new skill
- Improve an existing skill
- Improve trigger descriptions
- Improve catalog/search/routing
- Add examples
- Fix docs

## Local Setup

1. Clone the repository.
2. Use Python 3.11 or newer.
3. Run the validation script:

```powershell
python scripts/validate_repo.py
```

4. If you change skill metadata, rebuild the catalog:

```powershell
python scripts/build_skill_catalog.py
```

5. Search the catalog with at least one natural-language query related to your change:

```powershell
python scripts/query_skills.py "your natural language query"
```

## Branch Naming

Use short, descriptive branch names:

- `docs/readme-public-release`
- `skill/add-routing-helper`
- `catalog/improve-chinese-triggers`
- `fix/query-ranking`

## Commit Style

Use one of these prefixes:

- `docs:` documentation-only changes
- `skill:` skill additions or skill body updates
- `catalog:` generated catalog or routing metadata updates
- `script:` maintenance script changes
- `fix:` bug fixes
- `chore:` repository maintenance

## Skill Contribution Checklist

- Has a clear skill name
- Has a `SKILL.md`
- Has trigger phrases
- Has use cases
- Avoids secrets and private data
- Does not include copyrighted content copied from other repos

## Pull Request Checklist

- The change is scoped and easy to review
- Existing skill files are preserved unless the PR intentionally improves them
- `python scripts/validate_repo.py` passes
- Catalog files are rebuilt when skill metadata changed
- Examples are generic and do not contain private project details
- Public docs do not contain unnecessary local-only absolute paths

## Security and Privacy

Do not include API keys, private tokens, production credentials, customer data, or private local paths that are not required for understanding the example.
