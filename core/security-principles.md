---
id: CORE-001
type: core
title: Enterprise Security Principles
status: approved
version: 1.2
owner: Enterprise Security Architecture
load: always          # small, universal: always included in resolved context
summary: >
  Eight non-negotiable principles every design must demonstrably satisfy:
  zero trust, least privilege, secure by default, defence in depth, encrypt
  everywhere, observable by design, automate controls, explicit risk ownership.
---

# Enterprise Security Principles

Keep this document short. It is loaded into **every** agent context.

| # | Principle | Design must show |
|---|-----------|------------------|
| P1 | **Zero trust** | Every request is authenticated and authorised. Network location alone grants nothing. |
| P2 | **Least privilege** | Identities (human and workload) have only the permissions they need, scoped and time-bound. |
| P3 | **Secure by default** | Default configuration is the secure one; insecure options need an exception. |
| P4 | **Defence in depth** | No single control failure leads to compromise of restricted data. |
| P5 | **Encrypt everywhere** | TLS 1.2+ in transit; encryption at rest with enterprise-managed keys for confidential+. |
| P6 | **Observable by design** | Security-relevant events are logged centrally (SIEM) and alertable. |
| P7 | **Automate controls** | Controls are enforced as code (guardrails/policy-as-code), not just documented. |
| P8 | **Explicit risk ownership** | Deviations go through `exceptions/` with a named owner and expiry date. |

## How agents should use this repository
1. Cite standard requirement IDs (e.g. `SEC-IAM-001.R2`) when making claims of compliance.
2. Where a requirement cannot be met, propose an exception — never silently omit it.
3. Prefer approved `patterns/` over inventing new integrations.
