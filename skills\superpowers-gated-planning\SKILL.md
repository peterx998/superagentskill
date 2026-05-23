---
name: superpowers-gated-planning
description: Use when a user asks for creative work, feature design, behavior changes, implementation planning, coding tasks with gated approvals, or work after phrases like "wait for confirmation" or "plan first".
---

# Superpowers Gated Planning

## Rule

Do not implement until the user explicitly approves execution. This skill exists for work where thinking, designing, planning, and doing must stay in separate gates.

Use `references/gate-checklist.md` as the detailed gate checklist when available.

## Gates

1. Brainstorm first. Explore intent, constraints, risks, and options before proposing a direction.
2. Get design approval. The user must approve the chosen design or approach before you write an implementation plan.
3. Write the implementation plan. Keep it actionable and scoped, but stop before making changes.
4. Get execution approval. Only after explicit approval may you implement.

## What Counts as Implementation

Implementation includes code edits, implementation file creation, scaffolding, tests, dependency installs, config changes, formatting committed files, final generated artifacts, and commits. Harmless or preparatory work still counts if it changes the workspace or project state.

Design documents and implementation plans are planning artifacts, not implementation, when the active workflow explicitly calls for them before execution approval.

## Approval Rules

- Short replies like "next", "go on", "下一步", or "continue" advance the conversation only; they are not execution approval.
- "按1选项" or "choose option 1" selects an approach only; it is not permission to implement it.
- Proactive autonomy never overrides a user planning or approval gate.
- Do not combine plan plus implementation for efficiency.
- If approval is ambiguous, ask whether the user wants implementation to begin.
