---
id: PAT-LOG-001
type: pattern
title: SIEM Log Forwarding
status: approved
version: 1.3
owner: Security Operations
applies_to: {}
implements: [SEC-LOG-001.R1, SEC-LOG-001.R3]
summary: Org-level audit log sinks to central log archive account; application security events via OTel collector to SIEM in the enterprise schema.
---

# PAT-LOG-001 SIEM Log Forwarding

- **Platform logs**: inherited automatically from landing zone org-level sinks — confirm the account/subscription is enrolled.
- **Application security events**: emit JSON in enterprise schema → OTel collector → SIEM ingestion endpoint.
- Archive bucket is in the security log account; workload identities have no delete permission.
