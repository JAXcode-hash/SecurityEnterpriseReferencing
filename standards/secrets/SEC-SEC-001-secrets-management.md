---
id: SEC-SEC-001
type: standard
title: Secrets Management
status: approved
version: 1.1
owner: Platform Security
applies_to: {}
requirements: [SEC-SEC-001.R1, SEC-SEC-001.R2, SEC-SEC-001.R3]
controls: [CTL-NIST-IA-5, CTL-ISO-A.5.17]
patterns: [PAT-SEC-001]
guardrails: [GR-009]
summary: Secrets only in the enterprise secrets manager, fetched at runtime, rotated automatically; none in code, images or IaC state.
---

# SEC-SEC-001 Secrets Management

| ID | Requirement | Verification |
|----|-------------|--------------|
| **R1** | Secrets MUST be stored in the enterprise secrets manager and retrieved at runtime via workload identity (`PAT-SEC-001`). | Design review |
| **R2** | Secrets MUST NOT appear in source, container images, env files committed to VCS, or IaC state. | Guardrail `GR-009`, secret scanning |
| **R3** | Secrets MUST be rotated automatically (≤ 90 days; ≤ 30 days for restricted). | Secrets manager policy |
