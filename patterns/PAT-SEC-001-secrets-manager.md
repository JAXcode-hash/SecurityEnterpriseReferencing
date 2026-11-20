---
id: PAT-SEC-001
type: pattern
title: Runtime Secrets Retrieval
status: approved
version: 1.1
owner: Platform Security
applies_to:
  integrations: [secrets-manager]
implements: [SEC-SEC-001.R1, SEC-SEC-001.R3]
summary: Workload identity fetches secrets at runtime (CSI driver on Kubernetes, SDK/extension on serverless); rotation via managed rotation functions.
---

# PAT-SEC-001 Runtime Secrets Retrieval

| Hosting | Mechanism |
|---------|-----------|
| kubernetes | Secrets Store CSI driver, mounted as files, no k8s Secret sync for restricted |
| serverless | Secrets extension / SDK with caching ≤ 5 min |
| vm | Agent-based retrieval via workload identity |
