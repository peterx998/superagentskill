---
name: tdd-commerce-implementation
description: Implement Shopify, Dify middleware, API sync, or SEO build tasks using a test-first or verification-first loop. Use when code changes are required.
---

# TDD Commerce Implementation

## Goal

Prevent Codex from making broad, unverified changes.

## Loop

1. Define behavior.
2. Write or identify a failing test.
3. Implement the smallest code change.
4. Run relevant tests/lint/build.
5. Manually verify if automated tests are not available.
6. Refactor only after behavior is proven.
7. Document verification.

## If no test framework exists

Create a verification checklist instead:

- Input
- Expected output
- Actual output
- Screenshot/log path if available
- Risk if not verified

## For SEO/page work

Use content QA instead of unit tests:

- H1 present
- Meta title/description present
- FAQ present
- CTA present
- No prohibited medical claims
- Mobile layout considered
- Internal links included

## Output

- Files changed
- Verification command(s)
- Manual checks
- Remaining risks
