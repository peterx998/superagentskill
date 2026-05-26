# Security Policy

## Supported Version

| Version | Supported |
|---|---|
| `main` | Yes |

## Reporting Vulnerabilities

Prefer GitHub private vulnerability reporting if it is enabled for this repository.

If private reporting is not available, open a minimal issue that describes the risk without including secrets, exploit payloads that expose private systems, or sensitive local data.

## What Counts as a Security Issue

- Prompt injection in skills
- Unsafe shell command suggestions
- Secret leakage
- Malicious install scripts
- Path traversal
- Unsafe network calls

## What Not to Include in Reports

- API keys
- Private tokens
- Production credentials
- Private customer data

## Maintainer Response

Maintainers should acknowledge the report, reproduce the issue without using private data, patch the affected skill/script/doc, and update examples or validation rules when useful.
