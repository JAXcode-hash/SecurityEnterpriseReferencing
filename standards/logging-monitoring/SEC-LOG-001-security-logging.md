---
id: SEC-LOG-001
type: standard
title: Security Logging and SIEM Integration
status: approved
version: 1.6
owner: Security Operations
applies_to: {}
requirements: [SEC-LOG-001.R1, SEC-LOG-001.R2, SEC-LOG-001.R3]
controls: [CTL-NIST-AU-2, CTL-NIST-AU-6, CTL-ISO-A.8.15]
patterns: [PAT-LOG-001]
guardrails: [GR-008]
summary: >
  Platform audit logs and application security events forwarded to SIEM in the
  standard schema, retained 1 year, with detections agreed with SecOps.
---

# SEC-LOG-001 Security Logging and SIEM Integration

| ID | Requirement | Verification |
|----|-------------|--------------|
| **R1** | Cloud control-plane audit logs MUST be enabled and forwarded to SIEM (`PAT-LOG-001`). | Guardrail `GR-008` |
| **R2** | Applications MUST emit authN/authZ events, admin actions and data-export events in the enterprise security event schema. | Design review |
| **R3** | Security logs MUST be retained ≥ 1 year and be immutable to the workload's own identity. | Design review |
