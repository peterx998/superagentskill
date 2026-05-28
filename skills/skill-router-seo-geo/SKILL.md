---
name: skill-router-seo-geo
description: "Use when routing SEO, GEO, AI search, independent-site content, keyword scoring, product decision pages, FAQ strategy, Dr. Pen, microneedling, cartridge, official store, review page, comparison page, authenticity, aftercare, needle depth, Shopify landing page, hook, UGC, Obsidian knowledge-base, PDF manual extraction, or presentation strategy requests to the right local skill or knowledge workflow."
---

# SEO / GEO Skill Router

Use this as a focused routing layer for SEO, GEO, content strategy, and Dr. Pen-related knowledge workflows.

## Core Rule

Do not route "keyword" requests directly to article drafting. Route them through intent, page type, evidence, compliance, and conversion checks first.

Default sequence:

`keyword -> search intent -> page type -> product facts -> customer pain points -> compliance boundary -> conversion goal -> page structure -> draft copy`

## Route By User Wording

| User wording | Use skill or workflow | Purpose |
|---|---|---|
| SEO, GEO, AI search, Google impressions, Search Console, independent-site article, keyword, page brief | `drpen-seo-geo-content-strategy` when installed; otherwise use the local Dr. Pen knowledge-base workflow | Judge keyword value, search intent, page type, GEO answer structure, and conversion path. |
| Dr. Pen, microneedling, cartridge, M8S, M9, official store, official website, authenticity, aftercare, needle depth | `drpen-seo-geo-content-strategy` plus the Dr. Pen knowledge base | Pull product facts, pain points, page cards, FAQ, policy, and compliance notes before drafting. |
| hook, opening line, TikTok, Reels, Shorts, UGC script, ad angle, first three seconds, SEO intro | `hook-skills` | Generate or audit attention hooks while keeping product relevance and claim risk clear. |
| Obsidian, knowledge base, wiki, backlink notes, tags, templates, index, MOC | `obsidian-llm-wiki-skill` | Maintain structured notes, links, templates, and evidence cards. |
| Shopify page, product page, landing page, PDP, collection page, conversion section | use the relevant frontend or design skill if installed; otherwise create a page brief first | Convert strategy into page modules and user decision flow. |
| PDF, manual, product specs, official guide extraction | use a PDF/document extraction skill if installed | Extract source-backed facts before using them in public copy. |
| PPT, strategy deck, report, stakeholder presentation | presentation workflow if installed | Turn the strategy into a slide or report artifact. |

## Dr. Pen Knowledge Base Inputs

When the local Dr. Pen knowledge base is available, inspect these layers before writing:

- `01_Product Facts`: model specs, cartridge compatibility, package contents, manual-sourced facts.
- `02_Customer Pain Points`: beginner fear, safety concerns, cartridge concerns, authenticity doubts.
- `03_SEO Keywords`: keyword clusters and opportunity notes.
- `05_Page Knowledge Cards`: page type, required inputs, suggested modules, conversion goal.
- `07_Compliance Claims`: allowed, risky, and forbidden claim boundaries.
- `99_Templates`: keyword, page brief, FAQ, product fact, and scorecard templates.

## Keyword Decision Gate

Before recommending a standalone page, score the topic across:

1. Commercial value.
2. Page type fit.
3. Product fact support.
4. Pain-point strength.
5. Conversion path.
6. Compliance manageability.

Low-score topics should become FAQ blocks, product-page modules, collection-page copy, support-page sections, or be held until better evidence exists.

## Dr. Pen Page Routing Examples

- `dr pen official store`: route to a brand defense, official purchase path, authenticity, support, and FAQ page.
- `microneedling pen`: route to an educational hub or beginner decision page, not only a definition article.
- `dr pen cartridges` or `m8s cartridges`: route to cartridge compatibility and safety content with verified facts.
- `how to use microneedling pen`: route to a high-risk educational guide with official-source boundaries.
- `review` queries: route to suitability, product facts, comparison, and buying considerations; do not invent testimonials.

## Trigger Phrases

SEO文章, 独立站博客, GEO, AI搜索, Google SEO, Search Console, Google impressions, Dr Pen, Dr. Pen, microneedling, cartridge, cartridges, M8S, M9, official store, official website, review page, comparison page, authenticity, aftercare, needle depth, Shopify landing page, product decision page, FAQ schema, AI citation, ChatGPT visibility, Gemini visibility.

## Output Expectation

When this skill applies, first state which downstream skill or knowledge workflow should be used and why. Then provide the next action:

- score the keyword,
- create or update a page brief,
- pull product facts,
- draft FAQ blocks,
- audit hooks,
- or build the final page structure.
