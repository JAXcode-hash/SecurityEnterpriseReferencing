---
id: SEC-AI-001
type: standard
title: AI / LLM System Security
status: draft
version: 0.9
owner: Enterprise Security Architecture
applies_to:
  components: [ai-ml]
requirements: [SEC-AI-001.R1, SEC-AI-001.R2, SEC-AI-001.R3, SEC-AI-001.R4]
controls: [CTL-NIST-AI-RMF-MAP-1, CTL-ISO-42001-A.6]
patterns: []
guardrails: []
summary: >
  LLM/ML systems: approved model providers only, prompt-injection defences,
  tool/agent permissions least-privileged, and no restricted data to external models.
---

# SEC-AI-001 AI / LLM System Security

| ID | Requirement | Verification |
|----|-------------|--------------|
| **R1** | Only enterprise-approved model providers/endpoints MAY be used. | Design review |
| **R2** | Untrusted input reaching a model MUST be treated as hostile: prompt-injection mitigations, output validation before action. | Threat model |
| **R3** | Agent tools MUST run with least-privileged, scoped credentials; destructive actions require human approval. | Design review |
| **R4** | Restricted data MUST NOT be sent to externally hosted models without an approved data processing agreement. | Design review |
