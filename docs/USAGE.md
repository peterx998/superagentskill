# Usage Guide / 使用说明

EN: This guide explains how to install, search, rebuild, and maintain the skills library.

中文：本说明解释如何安装、检索、重建和维护这个 skills 库。

## 1. Install A Skill / 安装单个 Skill

Copy a skill folder from this repository:

```powershell
Copy-Item -Recurse .\skills\systematic-debugging C:\Users\LENOVO\.codex\skills\systematic-debugging
```

中文：把 `skills/` 下的某个 skill 文件夹复制到本机 Codex skills 目录。

After copying, restart Codex or open a new session.

中文：复制后需要重启 Codex 或开新会话，当前会话通常不会热加载新 skill。

## 2. Recommended Router Flow / 推荐路由流程

When the user does not name a skill, start with intent:

1. Is it broken? Use `systematic-debugging`.
2. Is it a new feature or behavior change? Use `brainstorming`, then `writing-plans`.
3. Is code going to change? Use `test-driven-development`.
4. Is the work complete? Use `verification-before-completion`.
5. Is it video, animation, knowledge, GitHub, OpenAI, or safety? Use the narrow domain skill.

中文路由：

1. 报错/失败/跑不起来：`systematic-debugging`
2. 新功能/改行为/创意设计：`brainstorming`，然后 `writing-plans`
3. 要改代码：`test-driven-development`
4. 要说完成/修好了：`verification-before-completion`
5. 视频、动画、知识库、GitHub、OpenAI、安全审计：选更具体的领域 skill

## 3. Search By Natural Language / 自然语言检索

Use the bundled Python runtime:

```powershell
& 'C:\Users\LENOVO\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts\query_skills.py 'MCP 安全 提示注入 工具调用日志 审计'
```

More examples:

```powershell
& 'C:\Users\LENOVO\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts\query_skills.py '报错 跑不起来 帮我排查根因'
& 'C:\Users\LENOVO\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts\query_skills.py '做短视频广告开头 UGC first line'
& 'C:\Users\LENOVO\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts\query_skills.py '把这个网址做成产品宣传视频 加字幕和配音'
```

中文：脚本会读取 `catalog/skills.sqlite` 和 `catalog/skills.json`，结合全文检索、关键词、中文触发词和专属触发短语排序。

## 4. Rebuild Catalog / 重建检索数据库

Run:

```powershell
& 'C:\Users\LENOVO\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts\build_skill_catalog.py
```

It scans:

- repository skills under `skills/`
- local installed skills under `C:\Users\LENOVO\.codex\skills`
- plugin-cache skills under `C:\Users\LENOVO\.codex\plugins\cache`

中文：重建会扫描仓库、本机已安装 skills、插件缓存，并生成 `catalog/` 下的 JSON/CSV/SQLite/Markdown 索引。

## 5. Sync Trigger Descriptions / 同步触发描述

Run:

```powershell
& 'C:\Users\LENOVO\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts\sync_skill_descriptions.py
```

中文：这个脚本会把本机已优化的 `description` 同步到仓库内同名 skill。适合本地先调好触发词，再回写仓库。

## 6. File Roles / 文件用途

| File | 中文说明 |
|---|---|
| `README.md` | 仓库首页，说明用途、快速开始和总分类 |
| `docs/CLASSIFICATION.md` | 人工整理的中英文分类索引 |
| `docs/USAGE.md` | 安装、检索、重建、维护说明 |
| `docs/skill-routing-policy.md` | 机器/代理可读的路由策略 |
| `catalog/preferred-skills.json` | 去重后的首选 skill 列表 |
| `catalog/skills.sqlite` | 快速全文检索数据库 |
| `scripts/query_skills.py` | 自然语言查询入口 |
| `scripts/build_skill_catalog.py` | 重新生成 catalog |

## 7. Maintenance Rules / 维护规则

- Keep skill folders readable and diffable; avoid storing duplicate zip archives when expanded folders exist.
- Keep `description` trigger-focused and start with `Use when`.
- Add Chinese trigger words for common local usage.
- Prefer narrow skills over broad skills.
- Rebuild `catalog/` after adding, deleting, or renaming skills.

中文：

- 有展开目录时，不再保留重复 zip。
- `description` 必须写成触发条件，尽量以 `Use when` 开头。
- 常见中文说法要写入触发词。
- 能用窄 skill 就不要用宽 skill。
- 增删改 skill 后要重建 `catalog/`。
