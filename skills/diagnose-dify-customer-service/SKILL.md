---
name: diagnose-dify-customer-service
description: Diagnose Dify chatbot failures, especially missing replies, empty retrieval behavior, wrong fallback, API payload mismatch, SaleSmartly bridge issues, or Shopify customer-service integration problems.
---

# Diagnose Dify Customer Service

## Goal

Find the smallest confirmed cause of a chatbot failure before changing prompts or code.

## Failure examples

- Knowledge retrieval result is empty but fallback reply is missing
- Bot does not reply in SaleSmartly
- Bot replies with wrong escalation email
- Dify API returns data but frontend does not show it
- Intent classifier route is wrong
- Shopify order lookup fails

## Diagnostic ladder

1. Reproduce
   - Exact user message
   - Expected reply
   - Actual reply
   - Channel: Dify preview, API, SaleSmartly, Shopify frontend

2. Isolate layer
   - Dify workflow preview
   - Dify API response
   - Middleware transform
   - SaleSmartly send/receive
   - Shopify frontend widget

3. Inspect payload
   - Query text
   - conversation/session id
   - response mode
   - result text field
   - error object
   - timeout

4. Inspect logic
   - classifier branch
   - retrieval empty condition
   - fallback condition
   - escalation condition

5. Patch minimally
   - Change one condition or prompt at a time
   - Retest the same input

6. Document
   - Root cause
   - Fix
   - Regression test messages

## Output

Use `templates/DIFY_DEBUG_REPORT.md` and save to `docs/agents/reports/` when asked.
