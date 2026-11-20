---
id: CHK-NET
type: checklist
title: Internet / Partner Exposure Review Checklist
status: approved
version: 1.0
owner: Network Security
applies_to:
  exposure: [internet-facing, partner]
summary: Reviewer questions for externally exposed services.
---
- [ ] Ingress path matches PAT-NET-001 (SEC-NET-001.R1)
- [ ] No public endpoints on compute/data (SEC-NET-001.R2)
- [ ] API gateway authN, rate limiting, schema validation (SEC-NET-001.R3)
- [ ] Partner mTLS/private connectivity, per-partner credentials (SEC-NET-001.R4)
