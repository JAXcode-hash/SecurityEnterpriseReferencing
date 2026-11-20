---
id: SEC-DATA-002
type: standard
title: Handling Restricted and Regulated Data (PII / PCI / PHI)
status: approved
version: 1.3
owner: Data Security
applies_to:
  data_classification: [confidential]      # ordinal: confidential and above
requirements: [SEC-DATA-002.R1, SEC-DATA-002.R2, SEC-DATA-002.R3, SEC-DATA-002.R4]
controls: [CTL-NIST-SC-28, CTL-PCI-3.5, CTL-ISO-A.8.11]
patterns: [PAT-DATA-001]
guardrails: [GR-005]
summary: >
  Confidential+ data needs data-flow mapping, minimisation, tokenisation for PCI,
  field-level protection for restricted data and no sensitive data in logs.
---

# SEC-DATA-002 Handling Restricted and Regulated Data

| ID | Requirement | Verification |
|----|-------------|--------------|
| **R1** | Designs MUST include a data-flow diagram marking where confidential+ data is stored, processed and transmitted. | Design review |
| **R2** | PCI cardholder data MUST be tokenised via the enterprise tokenisation service; PAN MUST NOT be stored by applications. | Design review |
| **R3** | Restricted data MUST use field-level or application-level encryption in addition to storage encryption. | Design review |
| **R4** | Sensitive data (PII, PCI, credentials) MUST NOT be written to logs; masking MUST be applied at source. | Code scan, `SEC-LOG-001` |
