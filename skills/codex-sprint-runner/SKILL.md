---
name: codex-sprint-runner
description: Execute one ready commerce issue at a time with Codex. Use after PRD and issue breakdown exist, especially for Shopify, Dify, SEO, or middleware work.
---

# Codex Sprint Runner

## Goal

Run one issue through planning, implementation, verification, and handoff.

## Rules

- Pick one issue only unless the user explicitly asks for multiple.
- Do not start if the issue lacks acceptance criteria.
- Do not hide assumptions.
- Stop for human review if credentials, production deploy, customer data, or payment configuration are required.

## Process

1. Read the issue.
2. Restate acceptance criteria.
3. Inspect relevant files.
4. Create a short implementation plan.
5. Make minimal changes.
6. Run tests/build/lint or manual verification.
7. Update issue with result.
8. Create handoff if needed.

## Output

- Summary
- Changed files
- Verification
- Risks
- Next issue recommendation
