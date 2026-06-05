# Superagent Skills Catalog

Generated: `2026-06-05T13:12:46.053209+00:00`
Total records: `102`
Unique skill names: `102`

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

### animation-rendering

- `animejs` (repository): Use when writing Anime.js animations in HyperFrames, converting Anime.js examples, creating timelines, registering window.__hfAnime, making motion deterministic, or fixing Anime.js preview or render behavior.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `css-animations` (repository): Use when authoring CSS keyframes, CSS-only animation, animation-delay timing, animation-fill-mode, play-state, transitions, or deterministic CSS motion for HyperFrames preview and rendering.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `gsap-core` (repository): Use when the user asks for GSAP core animation, JavaScript animation, DOM or SVG tweens, gsap.to, from, fromTo, easing, duration, stagger, defaults, matchMedia, responsive animation, reduced motion, or framework-agnostic animation.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `gsap-frameworks` (repository): Use when using GSAP with Vue, Nuxt, Svelte, SvelteKit, onMounted, onMount, onDestroy, framework lifecycle cleanup, scoped selectors, or non-React component animation.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `gsap-performance` (repository): Use when optimizing GSAP performance, animation jank, FPS, smoothness, 60fps, layout thrashing, transforms, will-change, batching, heavy scroll animation, or stuttering motion.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `gsap-plugins` (repository): Use when the user asks about GSAP plugins such as ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, SVG drawing, physics plugins, CustomEase, CustomWiggle, CustomBounce, or plugin registration.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `gsap-react` (repository): Use when using GSAP with React or Next.js, useGSAP, refs, gsap.context, component cleanup, React animation hooks, or React-specific animation lifecycle issues.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `gsap-scrolltrigger` (repository): Use when building scroll-based animation with GSAP ScrollTrigger, parallax, pinning, scrub, scroll triggers, scroll-driven scenes, pinned sections, reveal-on-scroll, or ScrollTrigger debugging.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `gsap-utils` (repository): Use when using gsap.utils, clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe, helper utilities, value mapping, or utility-driven animation logic.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `light-spotlight-render` (repository): Generate a swinging spotlight text-reveal HTML animation with configurable text, swing angle, lamp scale, glow, and colors. Use when users ask for 聚光灯扫字动画, spotlight text reveal, light logo reveal, 发光文字揭示动画, or want a reusable HTML animation instead of a static image.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `svg-assembly-animator` (repository): 为 SVG 矢量图创建充满“力量感”与“速度感”的零件组装动画，并支持一键导出 30fps 的透明背景序列帧。适用于需要将静态 SVG 转换为可用于视频剪辑（如 AE/PR）的透明素材场景。
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `tailwind` (repository): Use when using Tailwind CSS v4 in HyperFrames, hyperframes init --tailwind, Tailwind utility classes, CSS-first theme tokens, browser runtime Tailwind, v3 vs v4 syntax issues, or compiling Tailwind for compositions.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `three` (repository): Use when creating Three.js, WebGL, 3D scenes, canvas layers, cameras, shaders, AnimationMixer timelines, deterministic renders, or HyperFrames hf-seek driven 3D animation.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `threejs-earth-render` (repository): Clone or update https://github.com/vibe-motion/threejs-earth and render the Three.js Earth route animation with Puppeteer frame capture. Use when users ask for 三维地球航线动画, Three.js Earth, 地球飞线, globe route animation, or exporting an Earth GIF/MP4/PNG sequence.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `typegpu` (repository): Use when creating TypeGPU or raw WebGPU visuals, WGSL shaders, compute pipelines, GPU particles, liquid glass effects, navigator.gpu canvas layers, or HyperFrames hf-seek driven WebGPU scenes.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子
- `waapi` (repository): Use when authoring Web Animations API motion, element.animate, Animation currentTime, KeyframeEffect timing, fill modes, document.getAnimations, native browser animations, or deterministic WAAPI rendering in HyperFrames.
  - 中文触发: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子

### content-knowledge-marketing

- `agency-agents` (repository): Use when the user asks to consult, activate, invoke, or roleplay a specialist agent such as frontend, backend, UI, UX, product, marketing, sales, finance, academic, game, spatial, support, testing, strategy, expert, persona, or agency role.
  - 中文触发: 短视频hook, 广告开头, UGC脚本, 知识库, 双链笔记, Obsidian
- `git-guardrails-claude-code` (repository): Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git operations, add git safety hooks, or block git push/reset in Claude Code.
  - 中文触发: 短视频hook, 广告开头, UGC脚本, 知识库, 双链笔记, Obsidian
- `hook-skills` (repository): Use when the user asks for short-video hooks, TikTok, Reels, Shorts, UGC scripts, ad openings, first lines, first-three-seconds optimization, landing-page hooks, SEO intros, GEO intros, curiosity-gap copy, pain-point angles, or product feature hooks.
  - 中文触发: 短视频hook, 广告开头, UGC脚本, 知识库, 双链笔记, Obsidian
- `obsidian-llm-wiki-builder` (repository): Use when the user asks to organize Obsidian notes, personal knowledge management, LLM-assisted reading notes, wiki links, tags, templates, indexes, evergreen notes, vault structure, note cleanup, or knowledge workflows.
  - 中文触发: 短视频hook, 广告开头, UGC脚本, 知识库, 双链笔记, Obsidian
- `obsidian-vault` (repository): Search, create, and manage notes in the Obsidian vault with wikilinks and index notes. Use when user wants to find, create, or organize notes in Obsidian.
  - 中文触发: 短视频hook, 广告开头, UGC脚本, 知识库, 双链笔记, Obsidian
- `seo-page-builder` (repository): Build or improve a Shopify SEO/GEO page for Dr. Pen. Use for page briefs, page architecture, compliant copy, FAQ, meta fields, internal links, and Codex-ready implementation issues.
  - 中文触发: 短视频hook, 广告开头, UGC脚本, 知识库, 双链笔记, Obsidian
- `skill-router-seo-geo` (repository): Use when routing SEO, GEO, AI search, independent-site content, keyword scoring, product decision pages, FAQ strategy, Dr. Pen, microneedling, cartridge, official store, review page, comparison page, authenticity, aftercare, needle depth, Shopify landing page, hook, UGC, Obsidian knowledge-base, PDF manual extraction, or presentation strategy requests to the right local skill or knowledge workflow.
  - 中文触发: 短视频hook, 广告开头, UGC脚本, 知识库, 双链笔记, Obsidian
- `zoom-out` (repository): Tell the agent to zoom out and give broader context or a higher-level perspective. Use when you're unfamiliar with a section of code or need to understand how it fits into the bigger picture.
  - 中文触发: 短视频hook, 广告开头, UGC脚本, 知识库, 双链笔记, Obsidian

### debugging-code-quality

- `caveman` (repository): Ultra-compressed communication mode. Cuts token usage ~75% by dropping filler, articles, and pleasantries while keeping full technical accuracy. Use when user says "caveman mode", "talk like caveman", "use caveman", "less tokens", "be brief", or invokes /caveman.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `design-an-interface` (repository): Generate multiple radically different interface designs for a module using parallel sub-agents. Use when user wants to design an API, explore interface options, compare module shapes, or mentions "design it twice".
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `diagnose` (repository): Disciplined diagnosis loop for hard bugs and performance regressions. Reproduce → minimise → hypothesise → instrument → fix → regression-test. Use when user says "diagnose this" / "debug this", reports a bug, says something is broken/throwing/failing, or describes a performance regression.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `diagnose-dify-customer-service` (repository): Diagnose Dify chatbot failures, especially missing replies, empty retrieval behavior, wrong fallback, API payload mismatch, SaleSmartly bridge issues, or Shopify customer-service integration problems.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `diagnose-shopify-integration` (repository): Diagnose Shopify theme, Shopify App, Admin API, webhook, metafield, checkout, tracking, or frontend widget integration issues with minimal high-confidence changes.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `dify-rag-customer-service` (repository): Design or improve Dify RAG customer-service workflows for Shopify live chat, including retrieval-empty fallback, classifier logic, escalation, and answer policy.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `dispatching-parallel-agents` (repository): Use when a task has two or more independent workstreams, parallel subtasks, separate files, independent research tracks, or can be split among subagents without shared state or sequential dependency.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `edit-article` (repository): Edit and improve articles by restructuring sections, improving clarity, and tightening prose. Use when user wants to edit, revise, or improve an article draft.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `finishing-a-development-branch` (repository): Use when implementation is complete and the user needs to finish a branch, decide next integration steps, prepare merge or PR options, clean up work, summarize tests, or choose how to land completed changes.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `grill-with-commerce-docs` (repository): Stress-test a Shopify, Dify, SEO, or customer-service plan against business docs and compliance rules. Use before PRD writing when the request is vague, risky, or spans multiple systems.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `improve-codebase-architecture` (repository): Find deepening opportunities in a codebase, informed by the domain language in CONTEXT.md and the decisions in docs/adr/. Use when the user wants to improve architecture, find refactoring opportunities, consolidate tightly-coupled modules, or make a codebase more testable and AI-navigable.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `karpathy-guidelines` (repository): Use when writing, reviewing, debugging, or refactoring code where simplicity, minimal changes, clear assumptions, surgical edits, readability, verification, or Andrej Karpathy-style engineering discipline matters.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `migrate-to-shoehorn` (repository): Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `as` in tests, or needs partial test data.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `qa` (repository): Interactive QA session where user reports bugs or issues conversationally, and the agent files GitHub issues. Explores the codebase in the background for context and domain language. Use when user wants to report bugs, do QA, file issues conversationally, or mentions "QA session".
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `receiving-code-review` (repository): Use when the user gives code review feedback, requested changes, reviewer comments, inline comments, unclear suggestions, questionable advice, or asks to address review feedback before implementation.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `remotion-to-hyperframes` (repository): Use when the user explicitly asks to port, convert, migrate, translate, or rewrite an existing Remotion React video composition into a HyperFrames HTML composition.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `requesting-code-review` (repository): Use when work is complete or near complete and the user wants review, asks to check implementation quality, verify requirements, find risks, review before merge, or inspect a major feature before shipping.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `scaffold-exercises` (repository): Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exercises, create exercise stubs, or set up a new course section.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `setup-pre-commit` (repository): Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky, configure lint-staged, or add commit-time formatting/typechecking/testing.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `shopify-app-sync-workflow` (repository): Plan and implement Shopify App or middleware features that sync products, prices, inventory, orders, or customer-service data into Dify, SaleSmartly, or internal tools.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `systematic-debugging` (repository): Use when something is broken, failing, crashing, hanging, flaky, slow, behaving unexpectedly, tests fail, commands error, setup does not work, or the user asks to debug, fix, diagnose, troubleshoot, inspect logs, 排查, 修复, 报错, 卡住, or find root cause.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `tdd` (repository): Test-driven development with red-green-refactor loop. Use when user wants to build features or fix bugs using TDD, mentions "red-green-refactor", wants integration tests, or asks for test-first development.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `tdd-commerce-implementation` (repository): Implement Shopify, Dify middleware, API sync, or SEO build tasks using a test-first or verification-first loop. Use when code changes are required.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `test-driven-development` (repository): Use when implementing any feature, bugfix, behavior change, refactor, or code modification before writing implementation code, especially when tests, expected behavior, or verification can be defined first.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `to-issues` (repository): Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertical slices. Use when user wants to convert a plan into issues, create implementation tickets, or break down work into issues.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `to-vertical-commerce-issues` (repository): Break a commerce PRD into independently executable vertical slice issues for Shopify, Dify, SEO, or middleware work. Use after a PRD exists.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `triage` (repository): Triage issues through a state machine driven by triage roles. Use when user wants to create an issue, triage issues, review incoming bugs or feature requests, prepare issues for an AFK agent, or manage issue workflow.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `verification-before-completion` (repository): Use when claiming work is complete, fixed, passing, ready, merged, or shippable, before committing or opening PRs, or when final verification, test evidence, command output, or proof of success is needed.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `writing-beats` (repository): Shape an article as a journey of beats, choose-your-own-adventure style. The user picks a starting beat from the raw material, you write only that beat, then offer options for where to pivot next, beat by beat, until the article reaches a natural end. Use when the user has raw material and wants to assemble it as a narrative rather than an argument.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `writing-fragments` (repository): Grilling session that mines the user for fragments — heterogeneous nuggets of writing (claims, vignettes, sharp sentences, half-thoughts) — and appends them to a single document as raw material for a future article. Use when the user wants to develop ideas before imposing structure, or mentions "fragments", "ideate", or "raw material" for writing.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃
- `writing-skills` (repository): Use when creating, editing, packaging, testing, verifying, or improving Codex skills, SKILL.md files, descriptions, trigger behavior, skill folders, skill docs, or skill deployment.
  - 中文触发: 报错, 修复, 排查, 跑不起来, 失败, 崩溃

### github-project-workflows

- `operator-handoff` (repository): Create a clear handoff after a Codex task, including what changed, how to verify, open risks, follow-up tasks, and non-technical operator notes.
  - 中文触发: 上传GitHub, 私有库, 提交, 推送, PR, issue
- `prototype` (repository): Build a throwaway prototype to flesh out a design before committing to it. Routes between two branches — a runnable terminal app for state/business-logic questions, or several radically different UI variations toggleable from one route. Use when the user wants to prototype, sanity-check a data model or state machine, mock up a UI, explore design options, or says "prototype this", "let me play with it", "try a few designs".
  - 中文触发: 上传GitHub, 私有库, 提交, 推送, PR, issue
- `request-refactor-plan` (repository): Create a detailed refactor plan with tiny commits via user interview, then file it as a GitHub issue. Use when user wants to plan a refactor, create a refactoring RFC, or break a refactor into safe incremental steps.
  - 中文触发: 上传GitHub, 私有库, 提交, 推送, PR, issue
- `setup-drpen-agent-workflow` (repository): Initialize a Dr. Pen commerce repo for Codex skills. Use when starting a new Shopify, Dify, SEO, or middleware project and Codex needs to discover docs, issue workflow, labels, and repository type.
  - 中文触发: 上传GitHub, 私有库, 提交, 推送, PR, issue
- `setup-matt-pocock-skills` (repository): Sets up an `## Agent skills` block in AGENTS.md/CLAUDE.md and `docs/agents/` so the engineering skills know this repo's issue tracker (GitHub or local markdown), triage label vocabulary, and domain doc layout. Run before first use of `to-issues`, `to-prd`, `triage`, `diagnose`, `tdd`, `improve-codebase-architecture`, or `zoom-out` — or if those skills appear to be missing context about the issue tracker, triage labels, or domain docs.
  - 中文触发: 上传GitHub, 私有库, 提交, 推送, PR, issue
- `to-prd` (repository): Turn the current conversation context into a PRD and publish it to the project issue tracker. Use when user wants to create a PRD from the current context.
  - 中文触发: 上传GitHub, 私有库, 提交, 推送, PR, issue

### hyperframes-video

- `claude-typer` (repository): Render a Claude-style prompt typing animation video by calling Remotion CLI against the remote site https://www.laosunwendao.com. Use when the user asks for "做一个 claude 的提示词打字机动画", "做 Claude 打字动画", "创建提示词动画", or similar requests that convert a text prompt into a typing-animation video.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `contribute-catalog` (repository): Use when the user explicitly wants to contribute a HyperFrames registry block, caption style, VFX block, transition, lower third, text effect, overlay, snippet, catalog component, upstream PR, or public registry item.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `gsap` (repository): Use when writing GSAP animations in HyperFrames, using gsap.to, from, fromTo, timelines, easing, stagger, labels, nesting, playback, transforms, quickTo, or deterministic GSAP motion for video compositions.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `hyperframes` (repository): Use when creating HyperFrames video compositions, HTML-based videos, animated scenes, captions, subtitles, voiceovers, audio-reactive visuals, title cards, overlays, transitions, marker sweeps, hand-drawn highlights, or full video production workflows.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `hyperframes-cli` (repository): Use when running or troubleshooting HyperFrames CLI commands such as init, lint, inspect, preview, render, doctor, browser, info, upgrade, build environment checks, or npx hyperframes dev loops.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `hyperframes-media` (repository): Use when preparing HyperFrames media assets, generating TTS voiceover, choosing voices, transcribing audio or video, creating captions from speech, removing image or video backgrounds, or chaining TTS, transcription, and captions.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `hyperframes-registry` (repository): Use when installing, adding, wiring, or discovering HyperFrames registry blocks or components, using hyperframes add, editing hyperframes.json, merging component snippets, or connecting registry items to index.html.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `lottie` (repository): Use when embedding Lottie or dotLottie animations in HyperFrames, using lottie-web, .lottie files, @lottiefiles/dotlottie-web, After Effects exports, window.__hfLottie, or deterministic Lottie rendering.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `procedural-fish-render` (repository): Clone or update https://github.com/vibe-motion/procedural-fish and render procedural-fish animation to a video using the project's own render command. Use when the user asks to render 程序鱼/procedural fish, export a 程序鱼视频, or run procedural-fish Remotion rendering.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `remotion-3d-ticker` (repository): Creates infinite 3D vertical scrolling ticker animations in Remotion. Use when you need to build a parallax gallery, infinite image scroll, multi-column continuous vertical scrolling effect, or a 3D photo wall (3D照片滚动墙 / 3D相册瀑布流).
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `remotion-best-practices` (repository): Best practices for Remotion - Video creation in React
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `remotion-vinyl-player` (repository): Creates an elegant, realistic Vinyl Record Player animation component for Remotion. Use when needing a music player UI, album showcase, or audio-visualizer interface in a video. (Keywords: 黑胶唱片, 音乐播放器, 唱片机, 专辑展示, 音频可视化)
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `ruler-progress-render` (repository): Clone or update https://github.com/sxhzju/ruler-progress-animator and render a ruler progress video with default parameters. Use when users ask for requests like "绘制个尺子进度条", "做个尺子进度动画", "渲染 ruler progress", or ask to export the default demo video from this project.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `website-to-hyperframes` (repository): Use when the user provides a website URL or link and wants a HyperFrames video, promo, product tour, social ad, launch video, capture, website-to-video conversion, or says turn this site into video content.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频
- `wechat-2d-render` (repository): Clone or update https://github.com/sxhzju/wechat-2d and render the default WeChat-style 2D chat motion video with Remotion. Use when users ask for 微信聊天动画, wechat 2d chat render, 微信视频消息动效, or exporting the default demo from the wechat-2d project.
  - 中文触发: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频

### openai-api-apps

- `openai-docs` (.system): Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade guidance; prioritize OpenAI docs MCP tools, use bundled references only as helper context, and restrict any fallback browsing to official OpenAI domains.
  - 中文触发: OpenAI接口, API key, 智能体, 模型, ChatGPT应用, 评测

### routing-process

- `brainstorming` (repository): Use when starting creative work, feature design, behavior changes, app components, product ideas, UI flows, content direction, or any request that needs intent, requirements, design, tradeoffs, or approval before implementation.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `codex-sprint-runner` (repository): Execute one ready commerce issue at a time with Codex. Use after PRD and issue breakdown exist, especially for Shopify, Dify, SEO, or middleware work.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `executing-plans` (repository): Use when the user provides or approves a written implementation plan, asks to execute a plan, continue from a plan, run planned tasks, or work through checkpoints in a separate execution session.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `grill-me` (repository): Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `grill-with-docs` (repository): Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (CONTEXT.md, ADRs) inline as decisions crystallise. Use when user wants to stress-test a plan against their project's language and documented decisions.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `gsap-timeline` (repository): Use when sequencing GSAP animations, choreographing animation order, creating timelines, labels, nested timelines, timeline playback, position parameters, staggered sequences, or ordered motion.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `handoff` (repository): Compact the current conversation into a handoff document for another agent to pick up.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `review` (repository): Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/PRD asked for?). Runs both reviews in parallel sub-agents and reports them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to "review since X".
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `skill-router` (repository): Use when choosing which local Codex skill should apply, when many installed skills may match, when routing a request by intent, or when the assistant should select the right process, coding, content, video, animation, document, agent, or security skill.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `subagent-driven-development` (repository): Use when executing an implementation plan that has independent tasks in the current session, parallelizable steps, separable modules, or work that benefits from subagent task execution and review.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `superpowers-gated-planning` (repository): Use when the user asks for planning before action, wait for confirmation, plan first, gated approvals, feature design, creative work, behavior changes, coding tasks with approval gates, or implementation planning.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `to-commerce-prd` (repository): Convert a conversation, feature idea, SEO page request, Shopify App requirement, or Dify customer-service improvement into a commerce PRD with scope, user stories, risks, and acceptance criteria.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `using-git-worktrees` (repository): Use when starting feature work that should be isolated, creating or using git worktrees, protecting a dirty workspace, executing implementation plans safely, or separating branch work from current changes.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `using-superpowers` (repository): Use when starting a conversation or task, deciding whether any skill applies, enforcing skill checks before clarifying questions or actions, or preventing missed skill invocation.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `writing-plans` (repository): Use when a spec, requirements, approved design, or multi-step task needs a written implementation plan before touching code or coordinating execution.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务
- `writing-shape` (repository): Take a markdown file of raw material and shape it into an article through a conversational session — drafting candidate openings, growing the piece paragraph by paragraph, arguing about format (lists, tables, callouts, quotes) at each step. Use when the user has a pile of notes, fragments, or a rough draft and wants help turning it into something publishable.
  - 中文触发: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务

### skill-authoring-local-diagnostics

- `imagegen` (.system): Use when generating or editing raster images, AI-created bitmap visuals, photos, illustrations, textures, sprites, mockups, transparent cutouts, image variants, or reference-based visual assets rather than SVG, vector, code-native, HTML, CSS, or canvas visuals.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `local-skill-enhanced` (repository): Use when the user asks to inspect local project files, list files, scan the workspace, show runtime info, run safe diagnostics, check current directory, whoami, shell routing, or basic local skill package behavior.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `plugin-creator` (.system): Use when creating, scaffolding, validating, or updating Codex plugins, personal plugin folders, .codex-plugin/plugin.json, plugin manifests, marketplace entries, plugin ordering, or plugin availability metadata.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `skill-creator` (.system): Use when creating, updating, designing, packaging, testing, or improving Codex skills, SKILL.md files, skill folders, specialized workflows, knowledge extensions, tool integrations, or trigger descriptions.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `skill-installer` (.system): Use when listing, installing, importing, or updating Codex skills from curated sources, GitHub repositories, private repos, zip packages, local folders, or into $CODEX_HOME/skills.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `teach` (repository): Teach the user a new skill or concept, within this workspace.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `ubiquitous-language` (repository): Extract a DDD-style ubiquitous language glossary from the current conversation, flagging ambiguities and proposing canonical terms. Saves to UBIQUITOUS_LANGUAGE.md. Use when user wants to define domain terms, build a glossary, harden terminology, create a ubiquitous language, or mentions "domain model" or "DDD".
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
- `write-a-skill` (repository): Create new agent skills with proper structure, progressive disclosure, and bundled resources. Use when user wants to create, write, or build a new skill.
  - 中文触发: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境
