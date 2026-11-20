---
id: PAT-NET-001
type: pattern
title: Enterprise Edge (WAF + DDoS + API Gateway)
status: approved
version: 1.5
owner: Network Security
applies_to:
  exposure: [internet-facing, partner]
implements: [SEC-NET-001.R1, SEC-NET-001.R3]
summary: Public DNS → CDN/DDoS → managed WAF (enterprise ruleset) → API gateway → private load balancer → workload.
---

# PAT-NET-001 Enterprise Edge

```
Client → Public DNS → CDN + DDoS → WAF (enterprise managed ruleset)
       → API Gateway (authN, rate limit, schema validation) → Private LB → Workload
```
- WAF rules owned by Network Security; app teams may add, not remove.
- Origin only accepts traffic from the edge (private link or origin auth header + IP allow-list).
