---
id: STRAT-001
type: strategy
title: Enterprise Security Architecture Strategy 2026–2028
status: approved
version: 1.0
owner: CISO Office
applies_to: {}
summary: >
  Three-year direction: identity as the perimeter, controls-as-code aligned to
  the AaC programme, central SIEM/detection coverage, and secure AI adoption.
---

# Enterprise Security Architecture Strategy 2026–2028

## Strategic themes
| Theme | Outcome by 2028 | Linked standards |
|-------|-----------------|------------------|
| T1 Identity is the perimeter | 100% workloads on federated workload identity; zero static keys | SEC-IAM-001, SEC-IAM-002 |
| T2 Controls as code | ≥ 80% of security requirements enforced by AaC guardrails | `guardrails/` |
| T3 Detect everything that matters | All production accounts in SIEM; detection coverage mapped to ATT&CK | SEC-LOG-001 |
| T4 Secure AI adoption | All AI use cases through SEC-AI-001 review | SEC-AI-001 |

## Progression tracking
Maturity of each theme is tracked in `strategy/roadmap.yaml`.
