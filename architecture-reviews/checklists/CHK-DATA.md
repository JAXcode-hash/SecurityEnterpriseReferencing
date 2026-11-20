---
id: CHK-DATA
type: checklist
title: Sensitive Data Review Checklist
status: approved
version: 1.0
owner: Data Security
applies_to:
  data_classification: [confidential]
summary: Reviewer questions for confidential and restricted data.
---
- [ ] Data-flow diagram marks confidential+ data (SEC-DATA-002.R1)
- [ ] CMK per app/env with separated key admin (SEC-DATA-001.R3, PAT-DATA-001)
- [ ] PCI tokenised, no PAN stored (SEC-DATA-002.R2)
- [ ] Field-level encryption for restricted (SEC-DATA-002.R3)
- [ ] Log masking at source (SEC-DATA-002.R4)
