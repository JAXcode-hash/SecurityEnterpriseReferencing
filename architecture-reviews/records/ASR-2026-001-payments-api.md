---
id: ASR-2026-001
type: review-record
title: Review — Payments API v2
status: approved-with-conditions
version: 1.0
owner: Enterprise Security Architecture
design: designs/examples/payments-api
date: 2026-10-14
applies_to:
  components: [api]
  data_types: [pci]
summary: Tier 3 review of Payments API v2. Approved with 2 conditions (CMK rollout, partner mTLS) — EXC-2026-001 granted for legacy batch key.
---

# ASR-2026-001 Payments API v2

**Tier**: T3 · **Outcome**: Approved with conditions

| # | Condition | Requirement | Owner | Due |
|---|-----------|-------------|-------|-----|
| C1 | Migrate DB encryption to app-specific CMK | SEC-DATA-001.R3 | Payments platform lead | 2026-12-31 |
| C2 | Enforce mTLS for acquirer partner connection | SEC-NET-001.R4 | Payments platform lead | 2027-01-31 |

Exceptions: `EXC-2026-001`.
