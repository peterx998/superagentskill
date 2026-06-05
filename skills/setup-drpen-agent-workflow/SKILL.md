---
name: setup-drpen-agent-workflow
description: Initialize a Dr. Pen commerce repo for Codex skills. Use when starting a new Shopify, Dify, SEO, or middleware project and Codex needs to discover docs, issue workflow, labels, and repository type.
---

# Setup Dr. Pen Agent Workflow

Use this skill before any substantial work in a new or copied repository.

## Goal

Establish the project context Codex should follow for commerce, Shopify, Dify, and SEO tasks.

## Steps

1. Inspect the repository root.
   - Identify whether this is a Shopify theme, Shopify app, Dify middleware, content repo, or mixed repo.
   - Look for `package.json`, `shopify.app.toml`, `extensions/`, `theme.liquid`, `app/`, `src/`, `docs/`, `.env.example`.

2. Read project guidance.
   - `AGENTS.md`
   - `docs/agents/CONTEXT.md`
   - all ADRs in `docs/agents/adr/`

3. Report what you found.
   - Repo type
   - Main commands, if detectable
   - Missing docs or risks
   - Suggested issue tracker mode: GitHub Issues or local markdown in `docs/agents/issues/`

4. Create missing folders if needed.
   - `docs/agents/prds/`
   - `docs/agents/issues/`
   - `docs/agents/handoffs/`
   - `docs/agents/reports/`

5. Do not make code changes during setup unless explicitly asked.

## Output

Return a concise setup summary:

- Project type
- Active skills likely needed
- Existing commands
- Missing secrets or `.env.example` placeholders
- Next recommended task
