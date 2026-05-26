# Routing Policy / 路由策略

This file is the current public routing policy entrypoint.

The original policy file is preserved at [skill-routing-policy.md](skill-routing-policy.md) so old links continue to work.

## Decision Order

1. Match the user request against category, description, keywords, and Chinese trigger phrases.
2. Prefer process skills first when the request involves planning, debugging, implementation, review, or verification.
3. Then select the most specific domain skill for the tool, file type, framework, or output.
4. If multiple skills tie, choose the narrower skill with the strongest exact keyword overlap.
5. If no skill scores well, proceed normally and record the missing trigger as a future improvement.

## High-Signal Inputs

| Signal | Examples |
|---|---|
| Symptom | broken, failing tests, 报错, 跑不起来, 卡住 |
| Workflow | plan, review, verify, 规划, 代码审查, 验收 |
| Tool or framework | GSAP, HyperFrames, Three.js, OpenAI, Obsidian |
| Output type | video, image, docs, catalog, skill, 视频, 文档, 技能 |
| Safety concern | prompt injection, secret leakage, unsafe shell, 提示注入, 密钥泄露 |

## Tie Breakers

- Prefer the narrowest matching skill.
- Prefer process guidance before domain execution when the task is risky or underspecified.
- Prefer repository skill copies over duplicated local/plugin-cache copies.
- Prefer trigger descriptions that match the user's actual phrasing.

## Maintenance Rule

When a good user phrasing fails to retrieve the expected skill, update the skill description or catalog keywords rather than expecting users to memorize skill names.
