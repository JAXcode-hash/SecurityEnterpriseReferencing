---
id: SEC-IAM-001
type: standard
title: Workload Identity and Service Authentication
status: approved
version: 2.0
owner: IAM Security Architecture
applies_to: {}                  # universal: every design with workloads
requirements: [SEC-IAM-001.R1, SEC-IAM-001.R2, SEC-IAM-001.R3, SEC-IAM-001.R4]
controls: [CTL-NIST-IA-9, CTL-NIST-AC-6, CTL-ISO-A.5.16]
patterns: [PAT-IAM-002]
guardrails: [GR-001, GR-002]
summary: >
  Workloads authenticate with platform-issued, short-lived identities (no static
  keys), are scoped per service, and authorise every call.
---

# SEC-IAM-001 Workload Identity and Service Authentication

## Requirements
| ID | Requirement | Verification |
|----|-------------|--------------|
| **R1** | Workloads MUST use platform-native identity (IRSA / Workload Identity / Managed Identity). Long-lived access keys are prohibited. | Guardrail `GR-001` |
| **R2** | Each service MUST have its own identity; identities MUST NOT be shared across services or environments. | Design review |
| **R3** | IAM policies MUST NOT use wildcard actions on wildcard resources. | Guardrail `GR-002` |
| **R4** | Service-to-service calls MUST be authenticated (mTLS or signed tokens) and authorised at the receiver. | Design review, `PAT-IAM-002` |

## Design evidence expected
- Identity diagram showing each workload identity and its trust policy.
- Permission set per identity with justification.
