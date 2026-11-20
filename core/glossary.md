---
id: CORE-002
type: core
title: Glossary and ID Conventions
status: approved
version: 1.0
owner: Enterprise Security Architecture
load: always
summary: ID formats used across the repo so agents can trace requirements, controls, patterns and guardrails.
---

# ID conventions

| Prefix | Meaning | Example |
|--------|---------|---------|
| `CORE-nnn` | Always-loaded principles | `CORE-001` |
| `STRAT-nnn` | Strategy documents | `STRAT-001` |
| `SEC-<DOMAIN>-nnn` | Security standard | `SEC-IAM-001` |
| `SEC-<DOMAIN>-nnn.Rn` | Testable requirement inside a standard | `SEC-IAM-001.R2` |
| `PAT-<DOMAIN>-nnn` | Approved security integration pattern | `PAT-IAM-001` |
| `GR-nnn` | Guardrail mapping (security req → policy-as-code rule) | `GR-001` |
| `CHK-<DOMAIN>` | Review checklist | `CHK-IAM` |
| `ASR-yyyy-nnn` | Architecture/security review record | `ASR-2026-001` |
| `EXC-yyyy-nnn` | Risk exception | `EXC-2026-004` |
| `SDR-nnn` | Security decision record (ADR) | `SDR-001` |
| `CTL-<framework>-<id>` | External control framework reference | `CTL-NIST-AC-6` |

Domains: `IAM`, `DATA`, `NET`, `LOG`, `SEC` (secrets), `AI`.
