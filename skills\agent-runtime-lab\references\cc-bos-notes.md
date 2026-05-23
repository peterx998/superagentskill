# CC-BOS Defensive Notes

CC-BOS studies classical Chinese jailbreak prompt optimization using a multi-dimensional strategy space and bio-inspired search. For this skill, use the ideas only for defensive analysis and test design.

## Concepts To Reuse Safely

- Multi-dimensional decomposition: classify text across role, behavior, mechanism, metaphor, expression, knowledge, trigger pattern, and context.
- Normalization: translate or paraphrase obscure, archaic, encoded, or metaphorical text before judging intent.
- Search awareness: assume adversarial prompts may use indirect wording, mixed languages, metaphors, or delayed triggers.
- Evaluation loop: score risk, record evidence, and compare behavior across model/runtime versions.

## Do Not Implement

- Do not generate jailbreak prompts.
- Do not optimize prompts for bypass.
- Do not include harmful target responses.
- Do not automate attacks against public models or unauthorized systems.

## Defensive Mapping

- `role`: suspicious authority impersonation or tool impersonation.
- `behavior`: requests to ignore rules, reveal hidden data, or change routing.
- `mechanism`: stepwise evasion, hypothetical framing, or policy inversion.
- `metaphor`: obfuscated sensitive intent through symbolic language.
- `expression`: archaic, encoded, or mixed-language phrasing.
- `knowledge`: security-sensitive procedures, secrets, credentials, or internal configs.
- `trigger`: delayed activation, conditional execution, or hidden instructions.
- `context`: external documents, repo files, web pages, MCP descriptions, or chat history.
