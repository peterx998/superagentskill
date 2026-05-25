# superagentSkills

EN: A private, searchable Codex skills library for faster natural-language routing, safer skill selection, and easier restoration of local Codex skills.

中文：这是一个私有的 Codex skills 资料库，目标是让代理能通过自然语言快速判断该调用哪个 skill，而不是等用户记住并点名 skill。

Inspired by the agency-style directory pattern: one clear entrypoint, a categorized roster, quick-start commands, and short role/use-case descriptions.

## What This Repository Contains / 这个仓库包含什么

- `skills/`: installable Codex skill folders.
- `skills/skill-router/`: the main routing skill for choosing the right skill automatically.
- `catalog/`: generated search database and indexes.
- `docs/CLASSIFICATION.md`: bilingual skill category map.
- `docs/USAGE.md`: bilingual installation, query, update, and routing guide.
- `docs/skill-routing-policy.md`: routing policy and tie breakers.
- `scripts/query_skills.py`: local natural-language skill search.
- `scripts/build_skill_catalog.py`: rebuilds the catalog from repo, local, and plugin-cache skills.
- `scripts/sync_skill_descriptions.py`: syncs optimized trigger descriptions from local installed skills.

## Quick Start / 快速开始

Search by natural language:

```powershell
& 'C:\Users\LENOVO\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts\query_skills.py '报错 跑不起来 帮我排查'
```

Example results:

- `报错 跑不起来 帮我排查` -> `systematic-debugging`
- `把这个网址做成产品宣传视频 加字幕和配音` -> `website-to-hyperframes`, then `hyperframes-media`
- `MCP 安全 提示注入 工具调用日志 审计` -> `agent-runtime-lab`
- `做短视频广告开头 UGC first line` -> `hook-skills`

## Recommended First Skill / 推荐优先入口

Use `skill-router` when the user does not remember skill names.

中文：如果用户只是自然描述需求，例如“这个项目跑不起来”、“把网页做成视频”、“整理 Obsidian 笔记”，先让 `skill-router` 判断类别，再读取最具体的 skill。

## Skill Roster / Skills 分类

| Category | 中文分类 | Use for | Skills |
|---|---|---|---|
| Routing and planning | 路由、规划与执行 | Choosing skills, planning work, executing approved plans | `skill-router`, `using-superpowers`, `brainstorming`, `superpowers-gated-planning`, `writing-plans`, `executing-plans`, `subagent-driven-development`, `dispatching-parallel-agents`, `using-git-worktrees`, `finishing-a-development-branch` |
| Debugging and code quality | 调试、代码质量与验收 | Broken behavior, tests, reviews, verification | `systematic-debugging`, `test-driven-development`, `karpathy-guidelines`, `receiving-code-review`, `requesting-code-review`, `verification-before-completion` |
| Skill management | Skill 创建、安装与维护 | Creating, installing, packaging, improving, and indexing skills | `writing-skills`, `skill-creator`, `skill-installer`, `plugin-creator`, `local-skill-enhanced` |
| Agent runtime and safety | Agent 运行时与安全 | MCP, prompt injection, runtime logs, shell hooks, policy checks | `agent-runtime-lab` |
| Content and knowledge | 内容、营销与知识库 | Hooks, UGC scripts, Obsidian, knowledge workflows, specialist agents | `hook-skills`, `obsidian-llm-wiki-skill`, `agency-agents` |
| HyperFrames video | HyperFrames 视频制作 | HTML video, captions, voiceover, website-to-video, registry blocks | `hyperframes`, `hyperframes-cli`, `hyperframes-media`, `hyperframes-registry`, `website-to-hyperframes`, `remotion-to-hyperframes`, `contribute-catalog` |
| Animation and rendering | 动画与渲染 | GSAP, Three.js, WebGPU, Lottie, Anime.js, CSS and WAAPI animation | `gsap`, `gsap-core`, `gsap-react`, `gsap-frameworks`, `gsap-scrolltrigger`, `gsap-timeline`, `gsap-plugins`, `gsap-performance`, `gsap-utils`, `three`, `typegpu`, `lottie`, `animejs`, `css-animations`, `waapi`, `tailwind` |
| System and OpenAI | 系统与 OpenAI | Image generation, OpenAI docs, system skill support | `imagegen`, `openai-docs` |

See [docs/CLASSIFICATION.md](docs/CLASSIFICATION.md) for the full bilingual category map.

See [docs/USAGE.md](docs/USAGE.md) for bilingual installation, search, rebuild, and maintenance instructions.

## Routing Rule / 调用规则

1. Match the user request by intent, symptom, tool, file type, desired output, and Chinese trigger words.
2. Prefer process skills first when the task involves planning, debugging, implementation, review, or verification.
3. Then use the most specific domain skill.
4. Prefer repository skills over duplicated local/plugin-cache copies.
5. If no skill matches strongly, continue normally and add the missing trigger later.

## Catalog Files / 检索数据库

- `catalog/skills.sqlite`: SQLite FTS5 search database.
- `catalog/skills.json`: full database, including repo, local, and plugin-cache sources.
- `catalog/preferred-skills.json`: de-duplicated best source for each skill name.
- `catalog/keyword_index.json`: keyword-to-skill id index.
- `catalog/category_index.md`: generated category index.

## Restore / 恢复到本地 Codex

Copy a folder from `skills/` into:

```powershell
C:\Users\LENOVO\.codex\skills
```

Then restart Codex or open a new session so the runtime rescans skills.
