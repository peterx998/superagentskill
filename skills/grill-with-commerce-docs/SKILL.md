---
name: grill-with-commerce-docs
description: Stress-test a Shopify, Dify, SEO, or customer-service plan against business docs and compliance rules. Use before PRD writing when the request is vague, risky, or spans multiple systems.
---

# Grill With Commerce Docs

## Goal

Challenge a plan before implementation so Codex does not build the wrong thing.

## Required inputs

- User's plan, idea, page request, bug report, or feature request
- Existing docs from `docs/agents/CONTEXT.md`
- Relevant ADRs
- Relevant templates

## Process

1. Restate the objective in business terms.
2. Identify affected surfaces:
   - Shopify theme/page
   - Shopify app/backend
   - Dify workflow/RAG
   - SaleSmartly/chat frontend
   - SEO/GEO content
   - Product data / order data / customer data
3. Ask up to 8 hard questions, grouped by risk.
   - Conversion risk
   - Compliance risk
   - Data accuracy risk
   - Technical integration risk
   - Customer-service escalation risk
4. If enough information already exists, answer assumptions explicitly and continue.
5. Update or propose updates to domain docs only when a stable decision is made.
6. End with a PRD-ready brief.

## Output

- Refined objective
- Assumptions
- Open questions
- Risks
- Suggested next skill: usually `$to-commerce-prd`
