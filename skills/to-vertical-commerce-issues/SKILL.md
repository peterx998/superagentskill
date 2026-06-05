---
name: to-vertical-commerce-issues
description: Break a commerce PRD into independently executable vertical slice issues for Shopify, Dify, SEO, or middleware work. Use after a PRD exists.
---

# To Vertical Commerce Issues

## Goal

Turn a PRD into small, testable tasks that Codex can execute without losing context.

## Rules

- Prefer 5-8 issues for a medium feature.
- Each issue must cut through enough layers to verify behavior.
- Avoid purely horizontal issues such as only backend, only frontend, only docs.
- Every issue must include acceptance criteria and verification.
- Mark human-in-the-loop tasks clearly.

## Steps

1. Locate the PRD.
2. Read `templates/ISSUE_TEMPLATE.md`.
3. Identify integration risks and unknowns.
4. Create tracer bullet issue first.
5. Create follow-up issues for expansion, edge cases, UX polish, and documentation.
6. Save issues to `docs/agents/issues/<prd-slug>/ISSUE-XX-<slug>.md` unless using GitHub Issues.

## Issue labels

Use these labels when applicable:

- `area:shopify-theme`
- `area:shopify-app`
- `area:dify`
- `area:seo`
- `area:customer-service`
- `risk:compliance`
- `risk:data-privacy`
- `ready-for-codex`
- `needs-human-review`

## Output

- Issue list
- Recommended execution order
- HITL checkpoints
