# Safety Model

Use this model to classify findings and recommend defensive next steps.

## Risk Levels

- `info`: Diagnostic output with no direct security concern.
- `low`: Suspicious but common pattern; recommend review.
- `medium`: Action could expose data, alter state, or widen tool access.
- `high`: Action could delete data, exfiltrate secrets, execute untrusted code, bypass controls, or affect unauthorized systems.
- `blocked`: Do not execute. Explain the risk and suggest a safe alternative.

## Policy Categories

- `destructive`: recursive delete, force clean, disk formatting, destructive resets.
- `secret-access`: `.env`, private keys, token stores, browser cookies, SSH keys, cloud credentials.
- `network-exfil`: upload, webhook, pastebin, public tunnel, unknown remote endpoint.
- `repo-poisoning`: hook changes, dependency confusion, install scripts, CI modifications, hidden generated code.
- `mcp-risk`: broad filesystem tools, shell execution, network tools, tool-name deception, untrusted server paths.
- `prompt-injection`: attempts to override instructions, reveal secrets, disable safety, impersonate tools, or alter routing.
- `lab-target`: DVWA, Juice Shop, PortSwigger Labs, localhost, or explicitly authorized systems.

## Defensive Defaults

- Prefer read-only commands.
- Ask for explicit authorization before global scans or non-local targets.
- Redact secrets in output.
- Log actions with timestamp, cwd, action, status, and policy result.
- Keep exploit research inside lab targets.
