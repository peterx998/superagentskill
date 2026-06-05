---
name: to-commerce-prd
description: Convert a conversation, feature idea, SEO page request, Shopify App requirement, or Dify customer-service improvement into a commerce PRD with scope, user stories, risks, and acceptance criteria.
---

# To Commerce PRD

## Goal

Turn a loose request into a PRD that can be executed by Codex or a developer.

## Steps

1. Read `docs/agents/CONTEXT.md` and relevant ADRs.
2. Determine PRD type:
   - SEO page
   - Shopify theme component
   - Shopify App feature
   - Dify/RAG workflow
   - Customer-service fallback
   - Data sync / middleware
3. Use `templates/PRD_TEMPLATE.md`.
4. Include:
   - Background
   - Problem
   - Goals and non-goals
   - User stories
   - Data sources
   - UX/content requirements
   - Compliance guardrails
   - Technical approach
   - Acceptance criteria
   - Rollback plan
5. Save to `docs/agents/prds/YYYY-MM-DD-<slug>.md` unless the user asks for a different destination.

## Output

- PRD path
- Summary
- Main risks
- Recommended next skill: `$to-vertical-commerce-issues`
