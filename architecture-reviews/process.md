---
id: CORE-003
type: core
title: Security Architecture Review Process
status: approved
version: 1.1
owner: Enterprise Security Architecture
load: always
summary: Review tiers by classification/exposure, required artefacts, outcomes (Approved / Approved-with-conditions / Rejected) and where records live.
---

# Security Architecture Review Process

| Tier | Trigger | Reviewer |
|------|---------|----------|
| T1 Self-attest | internal + ≤ internal data | Team + AI-assisted check against resolved context |
| T2 Peer review | confidential data OR partner exposure | Security architect |
| T3 Board | restricted data OR internet-facing with confidential+ OR new pattern | Security Design Authority |

**Required artefacts**: `design-profile.yaml`, `security-design.md`, threat model, requirement compliance table.

**Outcomes** recorded in `architecture-reviews/records/ASR-yyyy-nnn.md`: Approved, Approved with conditions (each condition has owner + date), Rejected.
