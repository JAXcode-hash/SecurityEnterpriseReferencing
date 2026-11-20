---
id: PAT-IAM-002
type: pattern
title: Service-to-Service Authentication
status: approved
version: 1.0
owner: IAM Security Architecture
applies_to: {}
implements: [SEC-IAM-001.R1, SEC-IAM-001.R4]
summary: Mesh mTLS (Kubernetes) or cloud-signed tokens (serverless) plus receiver-side authorisation policy.
---

# PAT-IAM-002 Service-to-Service Authentication

| Hosting | Mechanism |
|---------|-----------|
| kubernetes | Service mesh mTLS with SPIFFE identities + mesh AuthorizationPolicy |
| serverless / paas | Cloud-issued identity tokens (IAM auth / Entra tokens) validated by receiver |
| vm | mTLS with certificates from enterprise private CA, ≤ 30-day lifetime |

Receiver MUST enforce an allow-list of caller identities.
