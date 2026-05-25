# Skill Routing Policy

## Decision Order

1. Match the user request against category, description, keywords, and Chinese trigger phrases.
2. Prefer process skills first when the request involves planning, debugging, implementation, review, or verification.
3. Then select the most specific domain skill for the tool, file type, framework, or output.
4. If multiple skills tie, choose the narrower skill with the strongest exact keyword overlap.
5. If no skill scores well, proceed normally and record the missing trigger as a future improvement.

## High-Signal Chinese Triggers

- `routing-process`: 规划, 计划, 先想方案, 设计一下, 按计划执行, 拆任务, 并行处理, 新功能, 改行为
- `debugging-code-quality`: 报错, 修复, 排查, 跑不起来, 失败, 崩溃, 卡住, 测试失败, 代码审查, 验收
- `skill-authoring-local-diagnostics`: 创建技能, 修改技能, 技能触发, 本地诊断, 扫描目录, 运行环境, 技能打包
- `agent-security-runtime`: MCP安全, 提示注入, 代理运行时, 工具调用, 策略检查, 安全审计
- `content-knowledge-marketing`: 短视频hook, 广告开头, UGC脚本, 知识库, 双链笔记, Obsidian, SEO, GEO
- `hyperframes-video`: 做视频, 字幕, 配音, 视频合成, 网页转视频, 网址做成视频, 链接做视频, 宣传片, 产品视频, 产品宣传视频
- `animation-rendering`: 动画, 滚动动画, 三维, WebGL, WebGPU, 粒子, 着色器, 动效
- `documents-data-presentations`: 表格, 文档, PPT, 幻灯片, 演示文稿, Figma, Canva
- `github-project-workflows`: 上传GitHub, 私有库, 提交, 推送, PR, issue, 仓库
- `openai-api-apps`: OpenAI接口, API key, 智能体, 模型, ChatGPT应用, 评测
