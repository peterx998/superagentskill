# superagentSkills

A production-oriented Codex skills library for teams and individual developers who want repeatable AI coding workflows: skill routing, debugging discipline, implementation planning, video and animation production, knowledge work, OpenAI guidance, and local skill restore all organized in one searchable repository.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Status: Private Preview](https://img.shields.io/badge/Status-Private%20Preview-orange.svg)

## English Overview

`superagentSkills` is a searchable, installable Codex skills library for turning natural-language requests into the right AI coding workflow. Instead of asking users to remember exact skill names, the repository provides a catalog, routing policy, category map, examples, and restore instructions so Codex can choose the most relevant `SKILL.md` for the job.

The library includes production-useful skills across several practical domains:

- **Routing and planning**: choose the right skill, clarify ambiguous requests, write implementation plans, execute approved plans, split parallel work, and protect dirty worktrees.
- **Debugging and verification**: investigate broken projects, isolate root causes, use test-driven changes, request or process code review, and verify completion before claiming a task is done.
- **Skill maintenance**: create, install, package, index, synchronize, and improve Codex skills with trigger-focused descriptions.
- **Agent runtime and security**: inspect local agent runtime behavior, audit MCP-style tool surfaces, reason about prompt injection, and avoid unsafe shell or secret-handling patterns.
- **Content and knowledge work**: route marketing hooks, UGC copy, specialist-agent prompts, Obsidian-style knowledge workflows, and structured research notes.
- **Video and motion production**: support HyperFrames video workflows, website-to-video conversion, captions, voiceover, registry components, Remotion migration, GSAP, Three.js, Lottie, Anime.js, WAAPI, CSS animation, Tailwind, and WebGPU-oriented rendering.
- **OpenAI and system guidance**: route OpenAI API documentation requests and system-level image generation or editing tasks.

The project helps solve a common scaling problem in AI-assisted development: once a local skills folder grows beyond a handful of entries, the hard part is no longer writing a skill; it is selecting, maintaining, and restoring the right skill at the right time. This repository makes that operational layer explicit.

Use it when you want to:

- Build a reusable Codex skill library instead of a private pile of prompts.
- Help Codex route vague requests such as "this project is broken", "turn this website into a product video", or "write a safer implementation plan" to the right workflow.
- Recover local skills after a machine change, Codex reset, or plugin/cache cleanup.
- Keep skill metadata searchable, reviewable, and safe for public release.
- Give contributors a clear structure for new skills, examples, validation, security review, and catalog rebuilds.

## 中文介绍

`superagentSkills` 是一个面向 Codex 的生产级 skills 库，目标不是简单堆放提示词，而是把本地 AI 编程工作流做成可检索、可恢复、可维护、可贡献的工程化资产。用户只需要用自然语言描述任务，Codex 就可以通过 catalog、routing policy、分类文档和 `SKILL.md` 内容，判断应该使用哪个 skill。

这个仓库目前覆盖的 skills 内容包括：

- **路由、规划与执行**：帮助 Codex 判断该用哪个 skill，澄清需求，写实施计划，执行已确认计划，拆分并行任务，保护未提交工作区。
- **调试、测试与验收**：用于项目跑不起来、测试失败、线上/本地报错、代码审查、修复验证、完成前自检等场景。
- **Skill 创建与维护**：用于创建新 skill、优化触发描述、安装本地 skill、同步描述、重建 catalog、维护可搜索索引。
- **Agent 运行时与安全**：用于 MCP 工具面审计、prompt injection 风险识别、工具调用日志分析、危险 shell 建议识别、密钥泄露防护。
- **内容与知识工作流**：用于短视频 hook、UGC 文案、专家角色选择、Obsidian 知识库整理、结构化研究和笔记工作流。
- **视频、动画与渲染**：用于 HyperFrames 视频合成、网页转视频、字幕、配音、组件 registry、Remotion 迁移、GSAP、Three.js、Lottie、Anime.js、WAAPI、CSS 动效、Tailwind、WebGPU 等前端动画/视频生产场景。
- **OpenAI 与系统能力**：用于 OpenAI API/模型文档查询，以及系统级图片生成或编辑任务。

它能帮助开发者和团队解决几个具体问题：

- 本地 skills 越来越多，但用户记不住 skill 名称，导致好用的 skill 无法稳定触发。
- 同类 skill 边界不清，调试、计划、执行、验收、视频、动画、安全等工作流容易混在一起。
- 换机器、清理缓存、重装 Codex 后，缺少一套可恢复的 skills 来源。
- 私有仓库准备公开时，缺少 README、贡献指南、安全策略、示例、CI、验证脚本和公开发布检查表。
- catalog 里容易混入本机绝对路径、plugin cache、本地用户目录等不适合公开的信息。

推荐的落地方式：

1. 把 `skills/` 作为可安装 skill 的源目录。
2. 用 `scripts/query_skills.py` 根据自然语言请求检索候选 skill。
3. 用 `docs/ROUTING_POLICY.md` 和 `docs/CLASSIFICATION.md` 明确路由规则和分类边界。
4. 增删改 skill 后运行 `scripts/build_skill_catalog.py` 重建 catalog。
5. 发布前运行 `scripts/validate_repo.py`，并按 `docs/PUBLIC_RELEASE_CHECKLIST.md` 检查安全、隐私、许可证和示例内容。

## What Is This?

This repository keeps installable Codex skill folders, a generated search catalog, routing policy notes, examples, integration notes, and small maintenance scripts in one place.

The goal is operational: make AI coding skills easy to discover, safe to share, simple to restore, and practical to maintain as the library grows.

## Why This Exists?

Codex skills are most useful when their trigger descriptions are easy to discover and their workflows are clearly separated. As the number of local skills grows, manual selection becomes brittle: names overlap, categories blur, private paths leak into generated files, and useful skills can sit unused.

This repository gives the collection a public-ready structure with searchable catalog files, installable skills, bilingual docs, examples, CI, validation, and release hygiene.

## Repository Structure

| Path | Purpose |
|---|---|
| `skills/` | Installable Codex skill folders. Each installable skill should contain `SKILL.md`. |
| `catalog/` | Generated JSON, JSONL, CSV, Markdown, and SQLite indexes for search and routing. |
| `scripts/` | Local maintenance scripts for catalog rebuilds, querying, description sync, and validation. |
| `docs/` | Human-readable architecture, classification, routing, usage, and release docs. |
| `examples/` | Generic workflow examples that show structure without private results. |
| `integrations/` | README-only integration notes for Codex and planned external targets. |
| `.github/` | Pull request template, issue forms, and lightweight CI. |

## Quick Start

### Search by natural language

```powershell
python scripts/query_skills.py "报错 跑不起来 帮我排查根因"
```

The query script reads the generated catalog and returns likely skills for the request.

### Rebuild catalog

```powershell
python scripts/build_skill_catalog.py
```

Run this after adding, removing, renaming, or materially changing skill metadata.

### Restore skills locally

```powershell
Copy-Item -Recurse .\skills\systematic-debugging "$env:USERPROFILE\.codex\skills\systematic-debugging"
```

Restart Codex or open a new session after restoring a skill so the runtime can rescan local skills.

## Skill Categories / Roster

This roster is generated from the existing classification docs and README content. See [docs/CLASSIFICATION.md](docs/CLASSIFICATION.md) for the fuller bilingual category map.

| Category | 中文分类 | Use for | Key skills |
|---|---|---|---|
| Routing, Planning, and Execution | 路由、规划与执行 | Choosing skills, planning implementation, splitting work, executing approved plans, and protecting workspace state. | `skill-router`, `using-superpowers`, `brainstorming`, `writing-plans`, `executing-plans`, `subagent-driven-development`, `dispatching-parallel-agents`, `using-git-worktrees` |
| Debugging, Code Quality, and Verification | 调试、代码质量与验收 | Broken behavior, failing tests, code review, risk checks, and proof that work is complete. | `systematic-debugging`, `test-driven-development`, `karpathy-guidelines`, `receiving-code-review`, `requesting-code-review`, `verification-before-completion` |
| Skill Management | Skill 创建、安装与维护 | Creating, installing, packaging, improving, indexing, and maintaining Codex skills. | `writing-skills`, `skill-creator`, `skill-installer`, `plugin-creator`, `local-skill-enhanced` |
| Agent Runtime and Safety | Agent 运行时与安全 | MCP, prompt injection, runtime behavior, shell/tool safety, and security-oriented checks. | `agent-runtime-lab` |
| Content, Marketing, and Knowledge Work | 内容、营销与知识库 | Hooks, UGC scripts, specialist roles, Obsidian notes, and knowledge workflows. | `hook-skills`, `obsidian-llm-wiki-skill`, `agency-agents` |
| HyperFrames Video | HyperFrames 视频制作 | HTML video, captions, voiceover, website-to-video, registry components, and Remotion migration. | `hyperframes`, `hyperframes-cli`, `hyperframes-media`, `hyperframes-registry`, `website-to-hyperframes`, `remotion-to-hyperframes`, `contribute-catalog` |
| Animation and Rendering | 动画与渲染 | GSAP, Three.js, WebGPU, Lottie, Anime.js, CSS animation, WAAPI, and motion performance. | `gsap`, `gsap-core`, `gsap-react`, `gsap-scrolltrigger`, `gsap-timeline`, `gsap-plugins`, `gsap-performance`, `three`, `typegpu`, `lottie`, `animejs`, `css-animations`, `waapi`, `tailwind` |
| System and OpenAI | 系统与 OpenAI | System-level image generation and OpenAI docs/API guidance. | `imagegen`, `openai-docs` |

## Usage with Codex

Use `skill-router` when the user describes a task but does not remember a skill name. Route by intent, symptom, tool, file type, desired output, and Chinese trigger phrases.

Recommended flow:

1. Search the catalog with the user's natural-language request.
2. Read the most specific matching `SKILL.md`.
3. Prefer process skills first for planning, debugging, implementation, review, or verification.
4. Prefer the narrowest domain skill once the workflow type is clear.
5. Restore missing local skills from `skills/` when needed.

## Integrations

Codex is the primary target. Other assistant environments are tracked as planned integration notes only.

| Target | Status | Notes |
|---|---|---|
| Codex | Supported | Skills can be restored manually into the local Codex skills directory. |
| Cursor | Planned | Future converter may map skill descriptions into Cursor rules or docs. |
| Claude Code | Planned | Future converter may map selected guidance into `CLAUDE.md` style project memory. |
| Gemini CLI | Planned | Future converter may map selected skills into Gemini-compatible local guidance. |

See [integrations/README.md](integrations/README.md).

## Examples

- [Skill routing workflow](examples/workflow-skill-routing.md)
- [Catalog rebuild workflow](examples/workflow-catalog-rebuild.md)
- [Local restore workflow](examples/workflow-local-restore.md)

## Contributing

Contributions are welcome when they improve the library without introducing private data, unsafe scripts, or copied copyrighted content. Start with [CONTRIBUTING.md](CONTRIBUTING.md).

Useful contribution types include new skills, better trigger descriptions, routing improvements, catalog/search fixes, examples, and documentation updates.

## Security

Treat skills as executable operating instructions for agents. Review them for prompt injection, unsafe shell suggestions, secret leakage, malicious install scripts, path traversal, and unsafe network calls.

Report security concerns through GitHub private vulnerability reporting if enabled. Otherwise open a minimal public issue without secrets. See [SECURITY.md](SECURITY.md).

## License

MIT License. See [LICENSE](LICENSE).

## Roadmap

- Keep the public-release documentation complete and honest.
- Improve catalog validation without requiring private local cache files.
- Add safer examples for common Chinese and English routing flows.
- Document a repeatable skill review process.
- Explore README-only integration plans before implementing converters.
