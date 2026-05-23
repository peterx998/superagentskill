---
name: obsidian-llm-wiki-builder
description: Use when the user wants to build, revise, or maintain a personal knowledge management workflow with Obsidian, LLM-assisted reading notes, wiki-style links, tags, templates, indexes, and evergreen notes.
---

# Obsidian LLM Wiki Builder

Use this skill to help a user turn reading, research, saved articles, meeting notes, or scattered ideas into an Obsidian-centered personal wiki with clear structure, reusable templates, and LLM-assisted refinement.

## Core stance

- Treat the user's notes as a long-term knowledge system, not one-off summaries.
- Preserve the user's original language, terminology, and source context.
- Prefer small linked notes, stable metadata, and explicit relationships over large undifferentiated documents.
- Separate capture, processing, connection, and review.
- Do not invent citations, facts, dates, or source claims. Mark uncertainty clearly.

## Workflow

1. **Capture the source**
   - Identify the input type: article, book chapter, web page, transcript, chat, PDF, meeting note, or loose thought.
   - Extract title, author/source if known, date, link/path, topic, and why the note matters.
   - Keep raw excerpts short and only when useful.

2. **Create a literature note**
   - Summarize the source in the user's words.
   - Pull out concepts, arguments, examples, methods, tools, objections, and practical steps.
   - Add tags that describe topic and use case, not only content category.
   - Add outbound wiki links for concepts that should become independent notes.

3. **Distill evergreen notes**
   - Convert durable ideas into short atomic notes.
   - Give each note a claim-style title when possible.
   - Include context, explanation, examples, counterpoints, and links back to source notes.
   - Avoid turning every heading into a separate note; split only when the idea can stand alone.

4. **Build navigation**
   - Create or update maps of content (MOCs) for broad domains.
   - Maintain indexes for projects, topics, people, tools, and reading queues.
   - Use consistent frontmatter so notes can be queried later.

5. **Review and evolve**
   - Suggest missing links, stale notes, duplicate notes, weak tags, and orphaned ideas.
   - Recommend merges only when notes express the same idea.
   - Recommend splits when a note contains multiple reusable claims.

## Default Obsidian note schema

Use this frontmatter unless the user already has a vault convention:

```yaml
---
type: literature | evergreen | moc | project | daily | reference
status: seed | growing | evergreen | archived
source:
created:
updated:
tags:
  - topic/
links:
---
```

## Output patterns

When creating a new note, return:

- Suggested file name.
- Frontmatter.
- Body in Markdown.
- Suggested backlinks and outbound links.
- Suggested tags.
- Follow-up notes to create next.

When improving existing notes, return:

- A concise diagnosis of the current structure.
- The revised note or patch-style edits.
- Link, tag, and metadata cleanup suggestions.
- Any assumptions caused by missing source material.

## Templates

Load `references/templates.md` when the user asks for ready-to-use Obsidian templates, vault structure, daily-note structure, source-note structure, MOC structure, or review checklists.

## Quality bar

- Prefer Chinese output when the user's notes or request are in Chinese.
- Keep summaries faithful and practical.
- Use clear Markdown headings.
- Make links meaningful: `[[concept name]]`, not vague generic labels.
- Keep tags consistent: lowercase English slugs or the user's existing taxonomy.
- End with concrete next actions or the completed note content, not open-ended questions unless information is truly missing.
