---
id: SEC-IAM-002
type: standard
title: Human Access, SSO and Privileged Access
status: approved
version: 1.4
owner: IAM Security Architecture
applies_to:
  components: [web-app, mobile-app, api]
requirements: [SEC-IAM-002.R1, SEC-IAM-002.R2, SEC-IAM-002.R3]
controls: [CTL-NIST-IA-2, CTL-NIST-AC-2, CTL-ISO-A.8.2]
patterns: [PAT-IAM-001]
guardrails: [GR-003]
summary: >
  All human access via enterprise IdP (OIDC/SAML) with phishing-resistant MFA;
  admin/production access via PAM with just-in-time elevation.
---

# SEC-IAM-002 Human Access, SSO and Privileged Access

| ID | Requirement | Verification |
|----|-------------|--------------|
| **R1** | Workforce users MUST authenticate via the enterprise IdP using OIDC or SAML (`PAT-IAM-001`). Local accounts are prohibited. | Design review |
| **R2** | MFA MUST be phishing-resistant (FIDO2/passkeys) for privileged and restricted-data access. | IdP config |
| **R3** | Production and admin access MUST be just-in-time via PAM, time-bound (≤ 8h) and session-recorded. | Guardrail `GR-003` |
