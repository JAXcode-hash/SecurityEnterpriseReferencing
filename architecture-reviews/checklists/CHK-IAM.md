---
id: CHK-IAM
type: checklist
title: Identity & Access Review Checklist
status: approved
version: 1.0
owner: Enterprise Security Architecture
applies_to: {}
summary: Reviewer questions for workload and human identity.
---
- [ ] Each workload has its own platform identity (SEC-IAM-001.R1, R2)
- [ ] Permission sets justified, no wildcards (SEC-IAM-001.R3)
- [ ] Service-to-service calls authenticated and authorised at receiver (SEC-IAM-001.R4)
- [ ] Human access via enterprise IdP; no local accounts (SEC-IAM-002.R1)
- [ ] Admin access via PAM JIT (SEC-IAM-002.R3)
