---
id: SEC-NET-001
type: standard
title: Internet-Facing Services
status: approved
version: 2.2
owner: Network Security
applies_to:
  exposure: [internet-facing, partner]
requirements: [SEC-NET-001.R1, SEC-NET-001.R2, SEC-NET-001.R3, SEC-NET-001.R4]
controls: [CTL-NIST-SC-7, CTL-NIST-SI-4, CTL-ISO-A.8.20]
patterns: [PAT-NET-001]
guardrails: [GR-006, GR-007]
summary: >
  Internet/partner-exposed endpoints sit behind the enterprise edge (WAF + DDoS +
  API gateway), never expose compute or data stores directly, and are rate-limited.
---

# SEC-NET-001 Internet-Facing Services

| ID | Requirement | Verification |
|----|-------------|--------------|
| **R1** | All ingress MUST traverse the enterprise edge: WAF and DDoS protection (`PAT-NET-001`). | Guardrail `GR-006` |
| **R2** | Compute, databases and storage MUST NOT have public IPs or public endpoints. | Guardrail `GR-007` |
| **R3** | APIs MUST be published via the enterprise API gateway with authentication, rate limiting and schema validation. | Design review |
| **R4** | Partner connections MUST use mTLS or private connectivity, with per-partner credentials. | Design review |
