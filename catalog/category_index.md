# Superagent Skills Catalog

Generated: `2026-05-25T15:57:52.071666+00:00`
Total records: `142`
Unique skill names: `86`

## How Matching Works

Use natural-language words from the user request against `description`, `keywords`, `zh_triggers`, `category`, and `search_text`.
Prefer the narrowest high-score skill. If a process skill and a domain skill both match, use the process skill first, then the domain skill.

SQLite FTS example:

```sql
SELECT s.name, s.category, s.description, bm25(skills_fts) AS score
FROM skills_fts
JOIN skills s ON s.rowid = skills_fts.rowid
WHERE skills_fts MATCH '报错 OR 修复 OR debug'
ORDER BY score
LIMIT 8;
```

## Categories

### agent-security-runtime

- `agent-runtime-lab` (repository): Use when the user asks to inspect, audit, harden, diagnose, or test local AI agent runtimes, Codex, Claude Code, MCP tools, shell hooks, tool routing, tool logs, prompt injection, repo poisoning, policy checks, or authorized security lab targets.
  - 中文触发: MCP安全, 提示注入, 代理运行时, 工具调用, 策略检查, 安全审计
- `agent-runtime-lab` (local): Use when the user asks to inspect, audit, harden, diagnose, or test local AI agent runtimes, Codex, Claude Code, MCP tools, shell hooks, tool routing, tool logs, prompt injection, repo poisoning, policy checks, or authorized security lab targets.
  - 中文触发: MCP安全, 提示注入, 代理运行时, 工具调用, 策略检查, 安全审计
- `plugin-creator` (.system): Use when creating, scaffolding, validating, or updating Codex plugins, personal plugin folders, .codex-plugin/plugin.json, plugin manifests, marketplace entries, plugin ordering, or plugin availability metadata.
  - 中文触发: MCP安全, 提示注入, 代理运行时, 工具调用, 策略检查, 安全审计
- `plugin-creator` (.system): Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/files, valid manifest defaults, and personal-marketplace entries by default. Use when Codex needs to create a new personal plugin, add optional plugin structure, or generate or update marketplace entries for plugin ordering and availability metadata.
  - 中文触发: MCP安全, 提示注入, 代理运行时, 工具调用, 策略检查, 安全审计

### animation-rendering

- `css-animations` (repository): Use when authoring CSS keyframes, CSS-only animation, animation-delay timing, animation-fill-mode, play-state, transitions, or deterministic CSS motion for HyperFrames preview and rendering.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `css-animations` (local): Use when authoring CSS keyframes, CSS-only animation, animation-delay timing, animation-fill-mode, play-state, transitions, or deterministic CSS motion for HyperFrames preview and rendering.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `gsap-performance` (repository): Use when optimizing GSAP performance, animation jank, FPS, smoothness, 60fps, layout thrashing, transforms, will-change, batching, heavy scroll animation, or stuttering motion.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `gsap-performance` (local): Use when optimizing GSAP performance, animation jank, FPS, smoothness, 60fps, layout thrashing, transforms, will-change, batching, heavy scroll animation, or stuttering motion.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `gsap-utils` (repository): Use when using gsap.utils, clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe, helper utilities, value mapping, or utility-driven animation logic.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `gsap-utils` (local): Use when using gsap.utils, clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe, helper utilities, value mapping, or utility-driven animation logic.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `svg-assembly-animator` (local): 为 SVG 矢量图创建充满“力量感”与“速度感”的零件组装动画，并支持一键导出 30fps 的透明背景序列帧。适用于需要将静态 SVG 转换为可用于视频剪辑（如 AE/PR）的透明素材场景。
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `three` (repository): Use when creating Three.js, WebGL, 3D scenes, canvas layers, cameras, shaders, AnimationMixer timelines, deterministic renders, or HyperFrames hf-seek driven 3D animation.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `three` (local): Use when creating Three.js, WebGL, 3D scenes, canvas layers, cameras, shaders, AnimationMixer timelines, deterministic renders, or HyperFrames hf-seek driven 3D animation.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `typegpu` (repository): Use when creating TypeGPU or raw WebGPU visuals, WGSL shaders, compute pipelines, GPU particles, liquid glass effects, navigator.gpu canvas layers, or HyperFrames hf-seek driven WebGPU scenes.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `typegpu` (local): Use when creating TypeGPU or raw WebGPU visuals, WGSL shaders, compute pipelines, GPU particles, liquid glass effects, navigator.gpu canvas layers, or HyperFrames hf-seek driven WebGPU scenes.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `waapi` (repository): Use when authoring Web Animations API motion, element.animate, Animation currentTime, KeyframeEffect timing, fill modes, document.getAnimations, native browser animations, or deterministic WAAPI rendering in HyperFrames.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `waapi` (local): Use when authoring Web Animations API motion, element.animate, Animation currentTime, KeyframeEffect timing, fill modes, document.getAnimations, native browser animations, or deterministic WAAPI rendering in HyperFrames.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子

### content-knowledge-marketing

- `agency-agents` (repository): Use when the user asks to consult, activate, invoke, or roleplay a specialist agent such as frontend, backend, UI, UX, product, marketing, sales, finance, academic, game, spatial, support, testing, strategy, expert, persona, or agency role.
  - 中文触发: 短视频hook, 广告开头, UGC脚本, 知识库, 双链笔记, Obsidian
- `agency-agents` (local): Use when the user asks to consult, activate, invoke, or roleplay a specialist agent such as frontend, backend, UI, UX, product, marketing, sales, finance, academic, game, spatial, support, testing, strategy, expert, persona, or agency role.
  - 中文触发: 短视频hook, 广告开头, UGC脚本, 知识库, 双链笔记, Obsidian
- `hook-skills` (repository): Use when the user asks for short-video hooks, TikTok, Reels, Shorts, UGC scripts, ad openings, first lines, first-three-seconds optimization, landing-page hooks, SEO intros, GEO intros, curiosity-gap copy, pain-point angles, or product feature hooks.
  - 中文触发: 短视频hook, 广告开头, UGC脚本, 知识库, 双链笔记, Obsidian
- `hook-skills` (local): Use when the user asks for short-video hooks, TikTok, Reels, Shorts, UGC scripts, ad openings, first lines, first-three-seconds optimization, landing-page hooks, SEO intros, GEO intros, curiosity-gap copy, pain-point angles, or product feature hooks.
  - 中文触发: 短视频hook, 广告开头, UGC脚本, 知识库, 双链笔记, Obsidian
- `obsidian-llm-wiki-builder` (repository): Use when the user asks to organize Obsidian notes, personal knowledge management, LLM-assisted reading notes, wiki links, tags, templates, indexes, evergreen notes, vault structure, note cleanup, or knowledge workflows.
  - 中文触发: 短视频hook, 广告开头, UGC脚本, 知识库, 双链笔记, Obsidian
- `obsidian-llm-wiki-builder` (local): Use when the user asks to organize Obsidian notes, personal knowledge management, LLM-assisted reading notes, wiki links, tags, templates, indexes, evergreen notes, vault structure, note cleanup, or knowledge workflows.
  - 中文触发: 短视频hook, 广告开头, UGC脚本, 知识库, 双链笔记, Obsidian
- `remotion-3d-ticker` (local): Creates infinite 3D vertical scrolling ticker animations in Remotion. Use when you need to build a parallax gallery, infinite image scroll, multi-column continuous vertical scrolling effect, or a 3D photo wall (3D照片滚动墙 / 3D相册瀑布流).
  - 中文触发: 短视频hook, 广告开头, UGC脚本, 知识库, 双链笔记, Obsidian
- `remotion-vinyl-player` (local): Creates an elegant, realistic Vinyl Record Player animation component for Remotion. Use when needing a music player UI, album showcase, or audio-visualizer interface in a video. (Keywords: 黑胶唱片, 音乐播放器, 唱片机, 专辑展示, 音频可视化)
  - 中文触发: 短视频hook, 广告开头, UGC脚本, 知识库, 双链笔记, Obsidian

### debugging-code-quality

- `Spreadsheets` (openai-primary-runtime): Use this skill when a user requests to create, modify, analyze, visualize, or work with spreadsheet files (`.xlsx`, `.xls`, `.csv`, `.tsv`) or Google Sheets-targeted spreadsheet artifacts with formulas, formatting, charts, tables, and recalculation.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `agents-sdk` (openai-developers): Build, run, deploy, and evaluate OpenAI Agents SDK apps from Codex. Use when the user asks to create or adapt an Agents SDK app, build from a prompt or Codex thread, prepare a runnable agent prototype, add a focused eval harness, or deploy locally through the Agents SDK Deployment Manager.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `animejs` (repository): Use when writing Anime.js animations in HyperFrames, converting Anime.js examples, creating timelines, registering window.__hfAnime, making motion deterministic, or fixing Anime.js preview or render behavior.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `animejs` (local): Use when writing Anime.js animations in HyperFrames, converting Anime.js examples, creating timelines, registering window.__hfAnime, making motion deterministic, or fixing Anime.js preview or render behavior.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `chatgpt-app-submission` (openai-developers): Inspect a ChatGPT Apps MCP server codebase and generate chatgpt-app-submission.json with app info suggestions, tool hint justifications, test cases, and negative test cases, then report review-check findings and outputSchema warnings for submission review.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `dispatching-parallel-agents` (repository): Use when a task has two or more independent workstreams, parallel subtasks, separate files, independent research tracks, or can be split among subagents without shared state or sequential dependency.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `dispatching-parallel-agents` (local): Use when a task has two or more independent workstreams, parallel subtasks, separate files, independent research tracks, or can be split among subagents without shared state or sequential dependency.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `figma-use` (figma): **MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `figma-use-slides` (figma): This skill helps agents use Figma's use_figma MCP tool in the Slides context. Can be used alongside figma-use which has foundational context for using the use_figma tool.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `finishing-a-development-branch` (repository): Use when implementation is complete and the user needs to finish a branch, decide next integration steps, prepare merge or PR options, clean up work, summarize tests, or choose how to land completed changes.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `finishing-a-development-branch` (local): Use when implementation is complete and the user needs to finish a branch, decide next integration steps, prepare merge or PR options, clean up work, summarize tests, or choose how to land completed changes.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `gh-fix-ci` (github): Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions. Use the GitHub app from this plugin for PR metadata and patch context, and use `gh` for Actions check and log inspection before implementing any approved fix.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `gsap` (hyperframes): GSAP animation reference for HyperFrames. Covers gsap.to(), from(), fromTo(), easing, stagger, defaults, timelines (gsap.timeline(), position parameter, labels, nesting, playback), and performance (transforms, will-change, quickTo). Use when writing GSAP animations in HyperFrames compositions.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `gsap-core` (repository): Use when the user asks for GSAP core animation, JavaScript animation, DOM or SVG tweens, gsap.to, from, fromTo, easing, duration, stagger, defaults, matchMedia, responsive animation, reduced motion, or framework-agnostic animation.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `gsap-core` (local): Use when the user asks for GSAP core animation, JavaScript animation, DOM or SVG tweens, gsap.to, from, fromTo, easing, duration, stagger, defaults, matchMedia, responsive animation, reduced motion, or framework-agnostic animation.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `gsap-frameworks` (repository): Use when using GSAP with Vue, Nuxt, Svelte, SvelteKit, onMounted, onMount, onDestroy, framework lifecycle cleanup, scoped selectors, or non-React component animation.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `gsap-frameworks` (local): Use when using GSAP with Vue, Nuxt, Svelte, SvelteKit, onMounted, onMount, onDestroy, framework lifecycle cleanup, scoped selectors, or non-React component animation.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `gsap-scrolltrigger` (repository): Use when building scroll-based animation with GSAP ScrollTrigger, parallax, pinning, scrub, scroll triggers, scroll-driven scenes, pinned sections, reveal-on-scroll, or ScrollTrigger debugging.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `gsap-scrolltrigger` (local): Use when building scroll-based animation with GSAP ScrollTrigger, parallax, pinning, scrub, scroll triggers, scroll-driven scenes, pinned sections, reveal-on-scroll, or ScrollTrigger debugging.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `karpathy-guidelines` (repository): Use when writing, reviewing, debugging, or refactoring code where simplicity, minimal changes, clear assumptions, surgical edits, readability, verification, or Andrej Karpathy-style engineering discipline matters.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `karpathy-guidelines` (local): Use when writing, reviewing, debugging, or refactoring code where simplicity, minimal changes, clear assumptions, surgical edits, readability, verification, or Andrej Karpathy-style engineering discipline matters.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `openai-platform-api-key` (openai-developers): Use for building, running, testing, debugging, or configuring apps, UIs, scripts, CLIs, generators, and tools that use AI, including AI-powered apps, apps that generate output with AI, and user-input-driven AI features. Treat unspecified AI in build requests as OpenAI API usage unless the user names another provider or says not to use OpenAI. First inspect credentials safely, then ask whether to reuse an existing key or create one before API-dependent implementation. Also use for OPENAI_API_KEY or sk-proj setup requests. Never expose plaintext.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `receiving-code-review` (repository): Use when the user gives code review feedback, requested changes, reviewer comments, inline comments, unclear suggestions, questionable advice, or asks to address review feedback before implementation.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `receiving-code-review` (local): Use when the user gives code review feedback, requested changes, reviewer comments, inline comments, unclear suggestions, questionable advice, or asks to address review feedback before implementation.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `remotion-to-hyperframes` (repository): Use when the user explicitly asks to port, convert, migrate, translate, or rewrite an existing Remotion React video composition into a HyperFrames HTML composition.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `remotion-to-hyperframes` (local): Use when the user explicitly asks to port, convert, migrate, translate, or rewrite an existing Remotion React video composition into a HyperFrames HTML composition.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `requesting-code-review` (repository): Use when work is complete or near complete and the user wants review, asks to check implementation quality, verify requirements, find risks, review before merge, or inspect a major feature before shipping.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `requesting-code-review` (local): Use when work is complete or near complete and the user wants review, asks to check implementation quality, verify requirements, find risks, review before merge, or inspect a major feature before shipping.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `skill-router` (local): Use when choosing which local Codex skill should apply, when many installed skills may match, when routing a request by intent, or when the assistant should select the right process, coding, content, video, animation, document, agent, or security skill.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `systematic-debugging` (repository): Use when something is broken, failing, crashing, hanging, flaky, slow, behaving unexpectedly, tests fail, commands error, setup does not work, or the user asks to debug, fix, diagnose, troubleshoot, inspect logs, 排查, 修复, 报错, 卡住, or find root cause.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `systematic-debugging` (local): Use when something is broken, failing, crashing, hanging, flaky, slow, behaving unexpectedly, tests fail, commands error, setup does not work, or the user asks to debug, fix, diagnose, troubleshoot, inspect logs, 排查, 修复, 报错, 卡住, or find root cause.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `test-driven-development` (repository): Use when implementing any feature, bugfix, behavior change, refactor, or code modification before writing implementation code, especially when tests, expected behavior, or verification can be defined first.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `test-driven-development` (local): Use when implementing any feature, bugfix, behavior change, refactor, or code modification before writing implementation code, especially when tests, expected behavior, or verification can be defined first.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `verification-before-completion` (repository): Use when claiming work is complete, fixed, passing, ready, merged, or shippable, before committing or opening PRs, or when final verification, test evidence, command output, or proof of success is needed.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `verification-before-completion` (local): Use when claiming work is complete, fixed, passing, ready, merged, or shippable, before committing or opening PRs, or when final verification, test evidence, command output, or proof of success is needed.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `writing-skills` (repository): Use when creating, editing, packaging, testing, verifying, or improving Codex skills, SKILL.md files, descriptions, trigger behavior, skill folders, skill docs, or skill deployment.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `writing-skills` (local): Use when creating, editing, packaging, testing, verifying, or improving Codex skills, SKILL.md files, descriptions, trigger behavior, skill folders, skill docs, or skill deployment.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃

### documents-data-presentations

- `canva-branded-presentation` (canva): Create on-brand Canva presentations from a brief, outline, existing Canva doc, or design link. Use when the user wants a branded slide deck, wants to turn notes into a presentation, or needs a presentation generated in Canva with the right brand kit and a clear slide plan.
  - 中文触发: 表格, 文档, PPT, 幻灯片, 演示文稿, Figma
- `figma-create-new-file` (figma): **MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `create_new_file` tool call. NEVER call `create_new_file` directly without loading this skill first. Trigger whenever the user wants a new blank Figma file — a new design, FigJam, or Slides file — or when you need a fresh file before calling `use_figma`. Usage — /figma-create-new-file [editorType] [fileName] (e.g. /figma-create-new-file figjam My Whiteboard, /figma-create-new-file slides Q3 Review)
  - 中文触发: 表格, 文档, PPT, 幻灯片, 演示文稿, Figma

### github-project-workflows

- `github` (github): Triage and orient GitHub repository, pull request, and issue work through the connected GitHub app. Use when the user asks for general GitHub help, wants PR or issue summaries, or needs repository context before choosing a more specific GitHub workflow.
  - 中文触发: 上传GitHub, 私有库, 提交, 推送, PR, issue
- `procedural-fish-render` (local): Clone or update https://github.com/vibe-motion/procedural-fish and render procedural-fish animation to a video using the project's own render command. Use when the user asks to render 程序鱼/procedural fish, export a 程序鱼视频, or run procedural-fish Remotion rendering.
  - 中文触发: 上传GitHub, 私有库, 提交, 推送, PR, issue
- `yeet` (github): Publish local changes to GitHub by confirming scope, committing intentionally, pushing the branch, and opening a draft PR through the GitHub app from this plugin, with `gh` used only as a fallback where connector coverage is insufficient.
  - 中文触发: 上传GitHub, 私有库, 提交, 推送, PR, issue

### hyperframes-video

- `contribute-catalog` (repository): Use when the user explicitly wants to contribute a HyperFrames registry block, caption style, VFX block, transition, lower third, text effect, overlay, snippet, catalog component, upstream PR, or public registry item.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `contribute-catalog` (local): Use when the user explicitly wants to contribute a HyperFrames registry block, caption style, VFX block, transition, lower third, text effect, overlay, snippet, catalog component, upstream PR, or public registry item.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `gsap` (repository): Use when writing GSAP animations in HyperFrames, using gsap.to, from, fromTo, timelines, easing, stagger, labels, nesting, playback, transforms, quickTo, or deterministic GSAP motion for video compositions.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `gsap` (local): Use when writing GSAP animations in HyperFrames, using gsap.to, from, fromTo, timelines, easing, stagger, labels, nesting, playback, transforms, quickTo, or deterministic GSAP motion for video compositions.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `hyperframes` (repository): Use when creating HyperFrames video compositions, HTML-based videos, animated scenes, captions, subtitles, voiceovers, audio-reactive visuals, title cards, overlays, transitions, marker sweeps, hand-drawn highlights, or full video production workflows.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `hyperframes` (local): Use when creating HyperFrames video compositions, HTML-based videos, animated scenes, captions, subtitles, voiceovers, audio-reactive visuals, title cards, overlays, transitions, marker sweeps, hand-drawn highlights, or full video production workflows.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `hyperframes` (hyperframes): Create video compositions, animations, title cards, overlays, captions, voiceovers, audio-reactive visuals, and scene transitions in HyperFrames HTML. Use when asked to build any HTML-based video content, add captions or subtitles synced to audio, generate text-to-speech narration, create audio-reactive animation (beat sync, glow, pulse driven by music), add animated text highlighting (marker sweeps, hand-drawn circles, burst lines, scribble, sketchout), or add transitions between scenes (crossfades, wipes, reveals, shader transitions). Covers composition authoring, timing, media, and the full video production workflow. For CLI commands (init, lint, preview, render, transcribe, tts) see the hyperframes-cli skill.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `hyperframes-cli` (repository): Use when running or troubleshooting HyperFrames CLI commands such as init, lint, inspect, preview, render, doctor, browser, info, upgrade, build environment checks, or npx hyperframes dev loops.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `hyperframes-cli` (local): Use when running or troubleshooting HyperFrames CLI commands such as init, lint, inspect, preview, render, doctor, browser, info, upgrade, build environment checks, or npx hyperframes dev loops.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `hyperframes-cli` (hyperframes): HyperFrames CLI tool — hyperframes init, lint, inspect, preview, render, transcribe, tts, doctor, browser, info, upgrade, compositions, docs, benchmark. Use when scaffolding a project, linting, validating, inspecting visual layout in compositions, previewing in the studio, rendering to video, transcribing audio, generating TTS, or troubleshooting the HyperFrames environment.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `hyperframes-media` (repository): Use when preparing HyperFrames media assets, generating TTS voiceover, choosing voices, transcribing audio or video, creating captions from speech, removing image or video backgrounds, or chaining TTS, transcription, and captions.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `hyperframes-media` (local): Use when preparing HyperFrames media assets, generating TTS voiceover, choosing voices, transcribing audio or video, creating captions from speech, removing image or video backgrounds, or chaining TTS, transcription, and captions.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `hyperframes-registry` (repository): Use when installing, adding, wiring, or discovering HyperFrames registry blocks or components, using hyperframes add, editing hyperframes.json, merging component snippets, or connecting registry items to index.html.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `hyperframes-registry` (local): Use when installing, adding, wiring, or discovering HyperFrames registry blocks or components, using hyperframes add, editing hyperframes.json, merging component snippets, or connecting registry items to index.html.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `hyperframes-registry` (hyperframes): Install and wire registry blocks and components into HyperFrames compositions. Use when running hyperframes add, installing a block or component, wiring an installed item into index.html, or working with hyperframes.json. Covers the add command, install locations, block sub-composition wiring, component snippet merging, and registry discovery.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `lottie` (repository): Use when embedding Lottie or dotLottie animations in HyperFrames, using lottie-web, .lottie files, @lottiefiles/dotlottie-web, After Effects exports, window.__hfLottie, or deterministic Lottie rendering.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `lottie` (local): Use when embedding Lottie or dotLottie animations in HyperFrames, using lottie-web, .lottie files, @lottiefiles/dotlottie-web, After Effects exports, window.__hfLottie, or deterministic Lottie rendering.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `website-to-hyperframes` (repository): Use when the user provides a website URL or link and wants a HyperFrames video, promo, product tour, social ad, launch video, capture, website-to-video conversion, or says turn this site into video content.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `website-to-hyperframes` (local): Use when the user provides a website URL or link and wants a HyperFrames video, promo, product tour, social ad, launch video, capture, website-to-video conversion, or says turn this site into video content.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `website-to-hyperframes` (hyperframes): Capture a website and create a HyperFrames video from it. Use when: (1) a user provides a URL and wants a video, (2) someone says "capture this site", "turn this into a video", "make a promo from my site", (3) the user wants a social ad, product tour, or any video based on an existing website, (4) the user shares a link and asks for any kind of video content. Even if the user just pastes a URL — this is the skill to use.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频

### openai-api-apps

- `build-chatgpt-app` (openai-developers): Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widget UI. Use when Codex needs to design tools, register UI resources, wire the MCP Apps bridge or ChatGPT compatibility APIs, apply Apps SDK metadata or CSP or domain settings, or produce a docs-aligned project scaffold. Prefer a docs-first workflow by invoking the openai-docs skill or OpenAI developer docs MCP tools before generating code.
  - 中文触发: OpenAI接口, API key, 智能体, 模型, ChatGPT应用, 评测
- `openai-docs` (.system): Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade guidance; prioritize OpenAI docs MCP tools, use bundled references only as helper context, and restrict any fallback browsing to official OpenAI domains.
  - 中文触发: OpenAI接口, API key, 智能体, 模型, ChatGPT应用, 评测
- `openai-docs` (.system): Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade guidance; prioritize OpenAI docs MCP tools, use bundled references only as helper context, and restrict any fallback browsing to official OpenAI domains.
  - 中文触发: OpenAI接口, API key, 智能体, 模型, ChatGPT应用, 评测

### routing-process

- `brainstorming` (repository): Use when starting creative work, feature design, behavior changes, app components, product ideas, UI flows, content direction, or any request that needs intent, requirements, design, tradeoffs, or approval before implementation.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `brainstorming` (local): Use when starting creative work, feature design, behavior changes, app components, product ideas, UI flows, content direction, or any request that needs intent, requirements, design, tradeoffs, or approval before implementation.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `browser` (openai-bundled): Browser automation for the Codex in-app browser. Use to open, navigate, inspect, test, click, type, screenshot, or verify local targets such as localhost, 127.0.0.1, ::1, file://, the current in-app browser tab, and websites shown side by side inside Codex.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `canva-resize-for-all-social-media` (canva): Resize a Canva design into standard social media formats and prepare export-ready results. Use when the user wants one Canva design adapted across multiple social platforms such as Facebook, Instagram, and LinkedIn, especially when they want all variants produced in one pass.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `canva-translate-design` (canva): Translate the text in a Canva design into another language while preserving the original layout as much as possible. Use when the user wants a localized or translated version of an existing Canva design and expects the original file to remain unchanged.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `executing-plans` (repository): Use when the user provides or approves a written implementation plan, asks to execute a plan, continue from a plan, run planned tasks, or work through checkpoints in a separate execution session.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `executing-plans` (local): Use when the user provides or approves a written implementation plan, asks to execute a plan, continue from a plan, run planned tasks, or work through checkpoints in a separate execution session.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `figma-code-connect` (figma): Creates and maintains Figma Code Connect template files that map Figma components to code snippets. Use when the user mentions Code Connect, Figma component mapping, design-to-code translation, or asks to create/update .figma.ts or .figma.js files.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `figma-generate-design` (figma): Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code', 'convert this modal/dialog/drawer/panel to Figma'. This is the preferred workflow skill whenever the user wants to build or update a full page, modal, dialog, drawer, sidebar, panel, or any composed multi-section view in Figma from code or a description. Discovers design system components, variables, and styles from Code Connect files, existing screens, and library search, then imports them and assembles views incrementally section-by-section using design system tokens instead of hardcoded values.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `figma-generate-diagram` (figma): MANDATORY prerequisite — load this skill BEFORE every `generate_diagram` tool call. NEVER call `generate_diagram` directly without loading this skill first. Trigger whenever the user asks to create, generate, draw, render, sketch, or build a diagram — flowchart, architecture diagram, sequence diagram, ERD or entity-relationship diagram, state diagram or state machine, gantt chart, or timeline. Also trigger when the user mentions Mermaid syntax or wants a system architecture, decision tree, dependency graph, API call flow, auth handshake, schema, or pipeline visualized in FigJam. Routes to type-specific guidance, sets universal Mermaid constraints, and tells you when to use a different diagram type or skip the tool entirely (mindmaps, pie charts, class diagrams, etc.).
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `figma-generate-library` (figma): Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, create individual components with proper variant sets and variable bindings, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma. Also use when the user asks to create or generate any component in Figma — even a single one — since components require proper variable foundations, variant states, and design token bindings to be production-quality. This skill teaches WHAT to build and in WHAT ORDER — it complements the `figma-use` skill which teaches HOW to call the Plugin API. Both skills should be loaded together.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `figma-use-figjam` (figma): This skill helps agents use Figma's use_figma MCP tool in the FigJam context. Can be used alongside figma-use which has foundational context for using the use_figma tool.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `gh-address-comments` (github): Address actionable GitHub pull request review feedback. Use when the user wants to inspect unresolved review threads, requested changes, or inline review comments on a PR, then implement selected fixes. Use the GitHub app for PR metadata and flat comment reads, and use the bundled GraphQL script via `gh` whenever thread-level state, resolution status, or inline review context matters.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `gsap-timeline` (repository): Use when sequencing GSAP animations, choreographing animation order, creating timelines, labels, nested timelines, timeline playback, position parameters, staggered sequences, or ordered motion.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `gsap-timeline` (local): Use when sequencing GSAP animations, choreographing animation order, creating timelines, labels, nested timelines, timeline playback, position parameters, staggered sequences, or ordered motion.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `linear` (linear): Manage issues, projects & team workflows in Linear. Use when the user wants to read, create or updates tickets in Linear.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `openai-api-troubleshooting` (openai-developers): Use when an OpenAI API request fails and Codex needs to classify the likely cause, explain the next step, and route to the right follow-up. Covers common runtime failures such as blocked outbound network access, invalid credentials, exhausted API quota or credits, rate limits, and model, project, or organization access issues; delegate key provisioning to openai-platform-api-key and current documentation lookups to openai-docs.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `skill-creator` (.system): Use when creating, updating, designing, packaging, testing, or improving Codex skills, SKILL.md files, skill folders, specialized workflows, knowledge extensions, tool integrations, or trigger descriptions.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `skill-creator` (.system): Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Codex's capabilities with specialized knowledge, workflows, or tool integrations.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `subagent-driven-development` (repository): Use when executing an implementation plan that has independent tasks in the current session, parallelizable steps, separable modules, or work that benefits from subagent task execution and review.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `subagent-driven-development` (local): Use when executing an implementation plan that has independent tasks in the current session, parallelizable steps, separable modules, or work that benefits from subagent task execution and review.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `superpowers-gated-planning` (repository): Use when the user asks for planning before action, wait for confirmation, plan first, gated approvals, feature design, creative work, behavior changes, coding tasks with approval gates, or implementation planning.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `superpowers-gated-planning` (local): Use when the user asks for planning before action, wait for confirmation, plan first, gated approvals, feature design, creative work, behavior changes, coding tasks with approval gates, or implementation planning.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `using-git-worktrees` (repository): Use when starting feature work that should be isolated, creating or using git worktrees, protecting a dirty workspace, executing implementation plans safely, or separating branch work from current changes.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `using-git-worktrees` (local): Use when starting feature work that should be isolated, creating or using git worktrees, protecting a dirty workspace, executing implementation plans safely, or separating branch work from current changes.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `using-superpowers` (repository): Use when starting a conversation or task, deciding whether any skill applies, enforcing skill checks before clarifying questions or actions, or preventing missed skill invocation.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `using-superpowers` (local): Use when starting a conversation or task, deciding whether any skill applies, enforcing skill checks before clarifying questions or actions, or preventing missed skill invocation.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `writing-plans` (repository): Use when a spec, requirements, approved design, or multi-step task needs a written implementation plan before touching code or coordinating execution.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `writing-plans` (local): Use when a spec, requirements, approved design, or multi-step task needs a written implementation plan before touching code or coordinating execution.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务

### skill-authoring-local-diagnostics

- `Chrome` (openai-bundled): Browser automation for the user's Chrome browser. Use for browser tasks that require the user's cookies, logged-in sessions, existing tabs, extensions, or remote authenticated sites.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `Chrome` (openai-bundled): Browser automation for the user's Chrome browser. Use for browser tasks that require the user's cookies, logged-in sessions, existing tabs, extensions, or remote authenticated sites.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `Chrome` (openai-bundled): Browser automation for the user's Chrome browser. Use for browser tasks that require the user's cookies, logged-in sessions, existing tabs, extensions, or remote authenticated sites.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `Presentations` (openai-primary-runtime): Build premium editorial analytics presentation decks for PowerPoint and Google Slides with artifact-tool presentation JSX, using ruthless narrative editing, chart-first storytelling, rendered critique, platform-specific delivery rules, and iteration until the output beats the reference deck.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `claude-typer` (local): Render a Claude-style prompt typing animation video by calling Remotion CLI against the remote site https://www.laosunwendao.com. Use when the user asks for "做一个 claude 的提示词打字机动画", "做 Claude 打字动画", "创建提示词动画", or similar requests that convert a text prompt into a typing-animation video.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `documents` (openai-primary-runtime): Create, edit, redline, and comment on `.docx`, Word, and Google Docs-targeted document artifacts inside the container, with a strict render-and-verify workflow. Use `render_docx.py` to generate page PNGs (and optional PDF) for visual QA, then iterate until layout is flawless before delivering the final document.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `gsap-plugins` (repository): Use when the user asks about GSAP plugins such as ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, SVG drawing, physics plugins, CustomEase, CustomWiggle, CustomBounce, or plugin registration.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `gsap-plugins` (local): Use when the user asks about GSAP plugins such as ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, SVG drawing, physics plugins, CustomEase, CustomWiggle, CustomBounce, or plugin registration.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `gsap-react` (repository): Use when using GSAP with React or Next.js, useGSAP, refs, gsap.context, component cleanup, React animation hooks, or React-specific animation lifecycle issues.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `gsap-react` (local): Use when using GSAP with React or Next.js, useGSAP, refs, gsap.context, component cleanup, React animation hooks, or React-specific animation lifecycle issues.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `imagegen` (.system): Use when generating or editing raster images, AI-created bitmap visuals, photos, illustrations, textures, sprites, mockups, transparent cutouts, image variants, or reference-based visual assets rather than SVG, vector, code-native, HTML, CSS, or canvas visuals.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `imagegen` (.system): Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts. Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector. Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `light-spotlight-render` (local): Generate a swinging spotlight text-reveal HTML animation with configurable text, swing angle, lamp scale, glow, and colors. Use when users ask for 聚光灯扫字动画, spotlight text reveal, light logo reveal, 发光文字揭示动画, or want a reusable HTML animation instead of a static image.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `local-skill-enhanced` (repository): Use when the user asks to inspect local project files, list files, scan the workspace, show runtime info, run safe diagnostics, check current directory, whoami, shell routing, or basic local skill package behavior.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `local-skill-enhanced` (local): Use when the user asks to inspect local project files, list files, scan the workspace, show runtime info, run safe diagnostics, check current directory, whoami, shell routing, or basic local skill package behavior.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `remotion-best-practices` (local): Best practices for Remotion - Video creation in React
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `ruler-progress-render` (local): Clone or update https://github.com/sxhzju/ruler-progress-animator and render a ruler progress video with default parameters. Use when users ask for requests like "绘制个尺子进度条", "做个尺子进度动画", "渲染 ruler progress", or ask to export the default demo video from this project.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `skill-installer` (.system): Use when listing, installing, importing, or updating Codex skills from curated sources, GitHub repositories, private repos, zip packages, local folders, or into $CODEX_HOME/skills.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `skill-installer` (.system): Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos).
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `tailwind` (repository): Use when using Tailwind CSS v4 in HyperFrames, hyperframes init --tailwind, Tailwind utility classes, CSS-first theme tokens, browser runtime Tailwind, v3 vs v4 syntax issues, or compiling Tailwind for compositions.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `tailwind` (local): Use when using Tailwind CSS v4 in HyperFrames, hyperframes init --tailwind, Tailwind utility classes, CSS-first theme tokens, browser runtime Tailwind, v3 vs v4 syntax issues, or compiling Tailwind for compositions.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `threejs-earth-render` (local): Clone or update https://github.com/vibe-motion/threejs-earth and render the Three.js Earth route animation with Puppeteer frame capture. Use when users ask for 三维地球航线动画, Three.js Earth, 地球飞线, globe route animation, or exporting an Earth GIF/MP4/PNG sequence.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `wechat-2d-render` (local): Clone or update https://github.com/sxhzju/wechat-2d and render the default WeChat-style 2D chat motion video with Remotion. Use when users ask for 微信聊天动画, wechat 2d chat render, 微信视频消息动效, or exporting the default demo from the wechat-2d project.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
