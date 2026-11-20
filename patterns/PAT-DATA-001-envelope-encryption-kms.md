---
id: PAT-DATA-001
type: pattern
title: Envelope Encryption with Enterprise KMS
status: approved
version: 2.0
owner: Data Security
applies_to:
  data_classification: [confidential]
  integrations: [kms]
implements: [SEC-DATA-001.R3, SEC-DATA-002.R3]
summary: Per-application CMKs in enterprise KMS, key policy scoped to workload identity, automatic rotation, separation of key admins from key users.
---

# PAT-DATA-001 Envelope Encryption with Enterprise KMS

1. Request a CMK per application per environment (key alias `app/<name>/<env>`).
2. Key policy: workload identity = *use*; security key-admin role = *manage*. Never both.
3. Enable automatic annual rotation.
4. For restricted data, encrypt fields in the application with data keys from KMS (envelope).
5. Key usage logged to SIEM (`PAT-LOG-001`).
