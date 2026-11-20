---
id: PAT-IAM-001
type: pattern
title: OIDC Federation with Enterprise IdP
status: approved
version: 1.2
owner: IAM Security Architecture
applies_to:
  components: [web-app, mobile-app, api]
  integrations: [enterprise-idp]
implements: [SEC-IAM-002.R1, SEC-IAM-002.R2]
summary: Authorization Code + PKCE against the enterprise IdP; group-to-role mapping in IdP; tokens validated at gateway and service.
---

# PAT-IAM-001 OIDC Federation with Enterprise IdP

## When to use
Any application with workforce or customer sign-in.

## Integration
1. Register the app in the enterprise IdP (request via IAM onboarding).
2. Use **Authorization Code + PKCE**; implicit flow prohibited.
3. Map IdP groups → application roles in the IdP, not in app code.
4. Validate `iss`, `aud`, `exp` and signature at the API gateway **and** the service.
5. Access tokens ≤ 15 min; refresh tokens rotated and bound to client.

## Anti-patterns
- Storing tokens in browser localStorage.
- Application-managed passwords.
