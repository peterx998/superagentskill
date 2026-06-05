---
name: diagnose-shopify-integration
description: Diagnose Shopify theme, Shopify App, Admin API, webhook, metafield, checkout, tracking, or frontend widget integration issues with minimal high-confidence changes.
---

# Diagnose Shopify Integration

## Goal

Debug Shopify integration issues without guessing.

## Common issues

- Theme navigation does not match backend menu
- Customer email not passed to chat widget
- Admin API returns 401/403
- Metafields/metaobjects not rendering
- Webhook receiver not firing
- Product/price sync incorrect
- App proxy or CORS failure

## Steps

1. Reproduce the issue.
2. Identify surface:
   - Theme Liquid
   - Shopify Admin API
   - App backend
   - App proxy
   - Webhook
   - Third-party script
3. Check configuration before code.
   - App installed?
   - Scopes granted?
   - API version?
   - Environment variables?
   - Theme published vs preview?
   - Cache/CDN?
4. Add temporary logging if safe.
5. Make the smallest fix.
6. Verify with exact steps.
7. Remove sensitive logs.

## Output

- Root cause hypothesis
- Evidence
- Fix plan
- Verification steps
- Rollback plan
