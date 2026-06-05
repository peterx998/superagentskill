---
name: shopify-app-sync-workflow
description: Plan and implement Shopify App or middleware features that sync products, prices, inventory, orders, or customer-service data into Dify, SaleSmartly, or internal tools.
---

# Shopify App Sync Workflow

## Goal

Build small, safe integration features between Shopify and AI/customer-service systems.

## Common features

- Sync product title, handle, variant, price, inventory status to Dify knowledge base
- Track order lookup endpoint
- Discount code lookup endpoint
- Customer email handoff from Shopify frontend to chat frontend
- Admin-only debug dashboard
- Webhook receiver for product/order updates

## Required safeguards

- Use `.env.example`; never write real tokens.
- Apply least-privilege API scopes.
- Log request ids, not raw customer PII.
- Support dry-run mode before writing to external systems.
- Add retry and failure reporting.
- Add fallback behavior when Shopify/Dify API is unavailable.

## Process

1. Create or read a PRD.
2. Identify data source and target system.
3. Define payload schema.
4. Build a tracer bullet: one product/order through the full path.
5. Add tests or manual verification.
6. Add admin/operator documentation.

## Output

- PRD or implementation plan
- `.env.example` patch if needed
- Payload schema
- Verification steps
- Rollback notes
