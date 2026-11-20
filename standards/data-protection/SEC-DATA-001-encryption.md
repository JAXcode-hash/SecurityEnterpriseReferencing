---
id: SEC-DATA-001
type: standard
title: Encryption in Transit and at Rest
status: approved
version: 3.1
owner: Data Security
applies_to: {}
requirements: [SEC-DATA-001.R1, SEC-DATA-001.R2, SEC-DATA-001.R3]
controls: [CTL-NIST-SC-8, CTL-NIST-SC-28, CTL-ISO-A.8.24]
patterns: [PAT-DATA-001]
guardrails: [GR-004, GR-005]
summary: TLS 1.2+ everywhere; all storage encrypted at rest; confidential+ uses enterprise CMKs.
---

# SEC-DATA-001 Encryption in Transit and at Rest

| ID | Requirement | Verification |
|----|-------------|--------------|
| **R1** | All network traffic MUST use TLS 1.2+ (1.3 preferred). Plaintext listeners prohibited. | Guardrail `GR-004` |
| **R2** | All persistent storage MUST be encrypted at rest. | Guardrail `GR-005` |
| **R3** | Confidential and restricted data MUST be encrypted with enterprise customer-managed keys (`PAT-DATA-001`). | Design review |
