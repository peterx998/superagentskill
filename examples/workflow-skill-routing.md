# Workflow: Skill Routing

This example shows structure only. It does not claim a real search result.

## User Request

```text
这个项目跑不起来，日志里有依赖错误，帮我排查根因。
```

## Routing Shape

1. Identify the request language and symptom: Chinese, broken project, dependency error.
2. Search by natural language:

```powershell
python scripts/query_skills.py "项目跑不起来 日志 依赖错误 排查根因"
```

3. Review the top candidates.
4. Select a debugging/process skill first, then any narrower domain skill if the logs point to a specific framework.
5. Read the selected `SKILL.md` before acting.

## Expected Decision Record

```text
Request: project fails to run with dependency logs
Primary category: Debugging, Code Quality, and Verification
Selected skill: <skill-name-from-search>
Reason: matched broken behavior and root-cause investigation language
```
