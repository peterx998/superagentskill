# Skills Classification / Skills 分类索引

EN: This file is the human-facing category map. The generated catalog is useful for machine search; this file is for quickly understanding where each skill belongs.

中文：这个文件是给人看的分类索引。`catalog/` 里的数据库适合机器检索；本文件用于快速理解每个 skill 应该归到哪里、什么时候触发。

## Category Logic / 分类原则

- Route by user intent, not by skill name.
- Process skills come before domain skills.
- The narrower skill wins when several skills match.
- Chinese trigger words are first-class routing signals.

中文原则：

- 按用户意图分类，而不是按 skill 名称硬记。
- 流程类 skill 优先于领域类 skill。
- 多个 skill 命中时，优先选择更窄、更具体的 skill。
- 中文触发词是重要检索信号。

## 1. Routing, Planning, And Execution / 路由、规划与执行

Use when the request is about deciding what to do, designing a feature, planning implementation, splitting work, or executing an approved plan.

中文：用于选择 skill、规划方案、拆任务、执行计划、保护工作区。

| Skill | 中文用途 | Natural-language triggers |
|---|---|---|
| `skill-router` | 总路由入口，用户记不住 skill 名时先用它 | choose skill, 自动触发, 技能路由, 不知道用哪个 |
| `using-superpowers` | 强制先判断是否有合适 skill | start task, skill check, 会话开始 |
| `brainstorming` | 创意、功能、行为变更前先澄清和设计 | 做个功能, 设计一下, 先想方案 |
| `superpowers-gated-planning` | 用户要求先计划、等确认、分阶段推进 | plan first, wait for confirmation, 先别动 |
| `writing-plans` | 把需求或 spec 写成实施计划 | 写计划, implementation plan, 多步骤任务 |
| `executing-plans` | 执行已有书面计划 | 按计划执行, continue plan |
| `subagent-driven-development` | 有独立任务时用子代理推进 | independent tasks, subagents |
| `dispatching-parallel-agents` | 多条独立工作流可并行处理 | parallel, 并行处理, 多任务 |
| `using-git-worktrees` | 需要隔离分支或保护脏工作区 | worktree, isolated feature work |
| `finishing-a-development-branch` | 完成开发后的 merge/PR/清理选择 | finish branch, ready to merge |

## 2. Debugging, Code Quality, And Verification / 调试、代码质量与验收

Use when something is broken, code is changing, review feedback exists, or completion must be proven.

中文：用于报错、修复、测试、代码审查、验收。

| Skill | 中文用途 | Natural-language triggers |
|---|---|---|
| `systematic-debugging` | 系统化排查 bug 和失败根因 | 报错, 跑不起来, 卡住, failure, logs |
| `test-driven-development` | 功能/修复/重构前先定义测试 | bugfix, feature, behavior change |
| `karpathy-guidelines` | 小步、清晰、可验证的工程纪律 | minimal change, surgical edit |
| `receiving-code-review` | 处理 review comments 前先判断是否合理 | review feedback, requested changes |
| `requesting-code-review` | 完成大改后主动审查风险 | review my changes, before merge |
| `verification-before-completion` | 声称完成前必须有验证证据 | done, fixed, passing, ready |

## 3. Skill Management / Skill 创建、安装与维护

Use when the task is about skills themselves.

中文：用于创建、安装、打包、索引、同步、优化 skills。

| Skill | 中文用途 | Natural-language triggers |
|---|---|---|
| `writing-skills` | 编写或改进 skill 文档与触发条件 | SKILL.md, trigger behavior, 写 skill |
| `skill-creator` | 创建或更新 Codex skill | 创建技能, update skill |
| `skill-installer` | 从 GitHub、本地、zip 安装 skill | install skill, 私有库 skill |
| `plugin-creator` | 创建 Codex plugin 结构 | plugin.json, plugin scaffold |
| `local-skill-enhanced` | 本地扫描、运行环境、轻量诊断 | scan workspace, runtime info |

## 4. Agent Runtime And Safety / Agent 运行时与安全

Use when the task involves agent runtime behavior, tool routing, MCP, prompt injection, or safety checks.

中文：用于 MCP、安全审计、提示注入、工具调用、运行时日志。

| Skill | 中文用途 | Natural-language triggers |
|---|---|---|
| `agent-runtime-lab` | 研究和加固本地代理运行时 | MCP 安全, prompt injection, 工具调用日志, policy |

## 5. Content, Marketing, And Knowledge Work / 内容、营销与知识库

Use when the output is copy, hooks, knowledge organization, or specialist role consultation.

中文：用于短视频 hook、广告开头、UGC、Obsidian、知识库、专家角色。

| Skill | 中文用途 | Natural-language triggers |
|---|---|---|
| `hook-skills` | 生成/诊断短视频、广告、落地页开头 | 短视频 hook, UGC, first line, 广告开头 |
| `obsidian-llm-wiki-skill` | 整理 Obsidian 笔记和知识网络 | Obsidian, 双链笔记, 知识库 |
| `agency-agents` | 选择专家角色或专业代理 | specialist, expert role, UI designer |

## 6. HyperFrames Video / HyperFrames 视频制作

Use when creating HTML-based videos, captions, voiceover, website-to-video, or HyperFrames components.

中文：用于视频合成、网页转视频、字幕、配音、HyperFrames 组件。

| Skill | 中文用途 | Natural-language triggers |
|---|---|---|
| `website-to-hyperframes` | 把网站/URL 转成视频 | 网址做成视频, website to video, promo |
| `hyperframes` | 编写完整 HyperFrames 视频 composition | 做视频, HTML video, title card |
| `hyperframes-media` | 配音、转录、字幕、背景移除 | 字幕, 配音, TTS, transcribe |
| `hyperframes-cli` | init/lint/preview/render 等 CLI 流程 | npx hyperframes, render, preview |
| `hyperframes-registry` | 安装和接入 registry blocks/components | hyperframes add, registry |
| `remotion-to-hyperframes` | 明确要求从 Remotion 迁移到 HyperFrames | port Remotion, migrate Remotion |
| `remotion-best-practices` | Remotion/React 视频制作最佳实践 | Remotion, video in React, Remotion 视频 |
| `claude-typer` | Claude 风格提示词打字机视频 | Claude typing animation, 提示词打字机 |
| `procedural-fish-render` | 渲染 procedural fish 动画视频 | procedural fish, 程序鱼视频 |
| `remotion-3d-ticker` | 3D 照片滚动墙/竖向 ticker | 3D ticker, 3D照片滚动墙 |
| `remotion-vinyl-player` | 黑胶唱片/音乐播放器视频组件 | vinyl player, 黑胶唱片, 音乐播放器 |
| `ruler-progress-render` | 尺子进度条动画渲染 | ruler progress, 尺子进度动画 |
| `wechat-2d-render` | 微信风格聊天动效视频渲染 | WeChat 2D, 微信聊天动画 |
| `contribute-catalog` | 向公共 HyperFrames catalog 贡献组件 | upstream catalog, public registry |

## 7. Animation And Rendering / 动画与渲染

Use when the request is specifically about animation libraries, deterministic rendering, 3D, GPU, canvas, or motion.

中文：用于 GSAP、Three.js、WebGPU、Lottie、Anime.js、CSS/WAAPI 动画。

| Skill | 中文用途 | Natural-language triggers |
|---|---|---|
| `gsap` | HyperFrames 中写 GSAP 动画 | GSAP in HyperFrames |
| `gsap-core` | GSAP 基础 tween 和 DOM/SVG 动画 | gsap.to, easing, stagger |
| `gsap-react` | React/Next.js 中使用 GSAP | useGSAP, gsap.context |
| `gsap-frameworks` | Vue/Svelte/Nuxt/SvelteKit 中使用 GSAP | onMounted, onMount |
| `gsap-scrolltrigger` | 滚动动画、pin、scrub、parallax | ScrollTrigger, scroll animation |
| `gsap-timeline` | 动画排序和 timeline 编排 | timeline, sequence |
| `gsap-plugins` | GSAP 插件与注册 | Flip, Draggable, SplitText |
| `gsap-performance` | 优化动画卡顿和 FPS | jank, 60fps, layout thrashing |
| `gsap-utils` | GSAP 工具函数 | clamp, mapRange, snap |
| `three` | Three.js/WebGL 场景 | 3D, WebGL, camera |
| `threejs-earth-render` | Three.js 地球航线/飞线动画渲染 | Three.js Earth, 三维地球航线, 地球飞线 |
| `typegpu` | TypeGPU/WebGPU/WGSL | WebGPU, shader, particles |
| `lottie` | Lottie/dotLottie 动画 | lottie-web, After Effects |
| `animejs` | Anime.js 时间线和动画 | Anime.js timeline |
| `css-animations` | CSS keyframes 和纯 CSS 动画 | keyframes, CSS motion |
| `waapi` | Web Animations API | element.animate, KeyframeEffect |
| `tailwind` | HyperFrames 中的 Tailwind v4 | Tailwind v4, utility classes |
| `light-spotlight-render` | 聚光灯扫字/发光文字揭示 HTML 动画 | spotlight text reveal, 聚光灯扫字 |
| `svg-assembly-animator` | SVG 零件组装动画和透明序列帧导出 | SVG assembly, SVG组装动画 |

## 8. System And OpenAI / 系统与 OpenAI

Use when working with system-level visual generation or OpenAI docs/API guidance.

中文：用于图片生成、OpenAI 官方文档和模型/API 指导。

| Skill | 中文用途 | Natural-language triggers |
|---|---|---|
| `imagegen` | 生成或编辑位图图片 | image generation, mockup, cutout |
| `openai-docs` | OpenAI API/模型/官方文档 | OpenAI API, model, docs |
