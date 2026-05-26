# superagentSkills

A searchable Codex skills library for routing, restoring, and maintaining local AI coding skills.

一个面向 Codex 的可检索 skills 库，用于技能路由、本地恢复和技能维护。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Status: Private Preview](https://img.shields.io/badge/Status-Private%20Preview-orange.svg)

## What Is This?

`superagentSkills` is a practical Codex skills library. It keeps installable skill folders, a generated search catalog, routing policy notes, and small maintenance scripts in one repository.

The goal is simple: describe a task in natural language, find the right skill, and restore or maintain that skill locally without relying on memory of exact folder names.

## Why This Exists?

Codex skills are most useful when their trigger descriptions are easy to discover. As the number of local skills grows, manual selection becomes brittle: names overlap, categories blur, and useful skills can sit unused.

This repository gives the collection a public-ready structure:

- searchable catalog files under `catalog/`
- installable skill folders under `skills/`
- bilingual routing and usage docs under `docs/`
- repeatable scripts under `scripts/`
- safe examples and integration notes for future adapters

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
