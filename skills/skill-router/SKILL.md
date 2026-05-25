---
name: skill-router
description: "Use when choosing which local Codex skill should apply, when many installed skills may match, when routing a request by intent, or when the assistant should select the right process, coding, content, video, animation, document, agent, or security skill."
---

# Skill Router

Use this skill as the first routing layer when the user has many local Codex skills installed and the request does not explicitly name one.

## Routing Rule

Match the user's natural wording to intent, symptoms, file types, tools, and desired output. If one or more skills likely apply, read the most specific skill before acting.

Process skills come before domain skills:

1. If the user asks to design, plan, or change behavior, consider `brainstorming`, `superpowers-gated-planning`, or `writing-plans`.
2. If something is broken, consider `systematic-debugging` before proposing fixes.
3. If code will change, consider `test-driven-development` before implementation.
4. If work is done, consider `verification-before-completion` before claiming success.
5. If multiple independent tracks exist, consider `dispatching-parallel-agents` or `subagent-driven-development`.

## Categories

### Routing And Process

- `using-superpowers`: skill invocation discipline and startup checks.
- `skill-router`: choose the right local skill when the user does not remember names.
- `brainstorming`: intent, requirements, design, creative work, feature behavior.
- `superpowers-gated-planning`: plan first, wait for confirmation, approval gates.
- `writing-plans`: turn approved specs or requirements into implementation plans.
- `executing-plans`: execute an existing written plan.
- `dispatching-parallel-agents`: independent parallel workstreams.
- `subagent-driven-development`: execute planned independent tasks with subagents.
- `using-git-worktrees`: isolate feature work or protect dirty workspaces.
- `finishing-a-development-branch`: finish, merge, PR, or clean up completed work.

### Code Quality And Debugging

- `systematic-debugging`: broken, failing, crashing, flaky, unexpected behavior.
- `test-driven-development`: features, bugfixes, behavior changes, refactors.
- `karpathy-guidelines`: simple, surgical, verifiable coding discipline.
- `receiving-code-review`: address review comments and requested changes.
- `requesting-code-review`: review completed work before shipping.
- `verification-before-completion`: prove work is complete or passing.

### Skill Authoring And Local Diagnostics

- `writing-skills`: create, edit, package, and verify skills.
- `local-skill-enhanced`: safe local file scans and runtime diagnostics.
- `agent-runtime-lab`: agent runtime, MCP, prompt injection, policy, and lab audits.

### Content And Knowledge Work

- `hook-skills`: short-video hooks, ad openings, UGC, SEO/GEO intros, pain angles.
- `obsidian-llm-wiki-skill`: Obsidian notes, wiki links, tags, templates, knowledge workflows.
- `agency-agents`: role-based expert agents and specialist personas.

### HyperFrames Video

- `hyperframes`: video composition authoring and production workflows.
- `hyperframes-cli`: init, lint, inspect, preview, render, doctor, and CLI environment.
- `hyperframes-media`: TTS, transcription, captions, and background removal.
- `hyperframes-registry`: install and wire registry blocks or components.
- `website-to-hyperframes`: turn a URL or website into a HyperFrames video.
- `remotion-to-hyperframes`: explicitly port Remotion video compositions to HyperFrames.
- `contribute-catalog`: contribute public HyperFrames registry items.

### Animation And Rendering

- `gsap`: GSAP in HyperFrames.
- `gsap-core`: GSAP core tweens and general DOM or SVG animation.
- `gsap-react`: GSAP with React or Next.js.
- `gsap-frameworks`: GSAP with Vue, Nuxt, Svelte, or SvelteKit.
- `gsap-scrolltrigger`: scroll animation, pinning, scrub, parallax.
- `gsap-timeline`: sequencing and timeline choreography.
- `gsap-plugins`: GSAP plugins and registration.
- `gsap-performance`: jank, FPS, layout thrashing, smoothness.
- `gsap-utils`: clamp, mapRange, snap, wrap, and helper utilities.
- `animejs`: Anime.js in HyperFrames.
- `css-animations`: CSS keyframes and deterministic CSS motion.
- `waapi`: Web Animations API motion.
- `lottie`: Lottie and dotLottie in HyperFrames.
- `three`: Three.js and WebGL scenes.
- `typegpu`: TypeGPU, raw WebGPU, and WGSL effects.
- `tailwind`: Tailwind CSS v4 in HyperFrames.

## Common Natural Language Triggers

- "报错", "跑不起来", "卡住", "失败", "修复", "排查": `systematic-debugging`
- "做个功能", "改行为", "设计一下", "先想方案": `brainstorming` or `superpowers-gated-planning`
- "写计划", "按计划执行": `writing-plans` or `executing-plans`
- "帮我 review", "处理 review comments": `requesting-code-review` or `receiving-code-review`
- "做短视频 hook", "广告开头", "UGC 脚本": `hook-skills`
- "整理 Obsidian", "知识库", "双链笔记": `obsidian-llm-wiki-skill`
- "做视频", "HyperFrames", "字幕", "配音": `hyperframes`
- "这个网址做成视频": `website-to-hyperframes`
- "MCP 安全", "prompt injection", "agent runtime": `agent-runtime-lab`

## Tie Breakers

Prefer the narrowest skill that matches the concrete task. If the task has both a workflow concern and a domain concern, use the workflow skill first and the domain skill second.
