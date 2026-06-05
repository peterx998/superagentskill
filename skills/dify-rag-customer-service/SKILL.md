---
name: dify-rag-customer-service
description: Design or improve Dify RAG customer-service workflows for Shopify live chat, including retrieval-empty fallback, classifier logic, escalation, and answer policy.
---

# Dify RAG Customer Service

## Goal

Make the chatbot answer safely, accurately, and with fewer unnecessary escalations.

## Scope

Use this for:

- Dify workflow design
- knowledge base coverage
- classifier rules
- retrieval-empty handling
- customer-service fallback messages
- order tracking handoff
- SaleSmartly integration behavior

## Steps

1. Identify the user intent classes:
   - greeting/vague help
   - order tracking
   - shipping policy
   - return/refund/warranty
   - product compatibility
   - authenticity verification
   - medical/safety escalation
   - out-of-scope country/policy exception
2. Check retrieval behavior.
   - Is retrieval empty?
   - Is the query too vague?
   - Is the knowledge document missing?
   - Is the chunking too narrow?
3. Apply fallback logic.
   - Vague message: ask for details.
   - Order issue: Track Your Order button or order/tracking number.
   - Medical/safety: do not diagnose; advise professional support when needed.
   - Policy exception: escalate to human support.
4. Produce Dify node-level recommendations.
5. Produce customer-facing reply examples.

## Output

- Intent classification table
- Workflow node recommendations
- Prompt/system instruction patch
- Retrieval test cases
- Safe fallback responses
