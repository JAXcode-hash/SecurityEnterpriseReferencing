# Traceability matrix (generated — do not edit)

| Requirement | Standard | Controls | Patterns | Guardrails → AaC rules | Exceptions |
|---|---|---|---|---|---|
| SEC-AI-001.R1 | SEC-AI-001 | CTL-NIST-AI-RMF-MAP-1, CTL-ISO-42001-A.6 | — | design review | — |
| SEC-AI-001.R2 | SEC-AI-001 | CTL-NIST-AI-RMF-MAP-1, CTL-ISO-42001-A.6 | — | design review | — |
| SEC-AI-001.R3 | SEC-AI-001 | CTL-NIST-AI-RMF-MAP-1, CTL-ISO-42001-A.6 | — | design review | — |
| SEC-AI-001.R4 | SEC-AI-001 | CTL-NIST-AI-RMF-MAP-1, CTL-ISO-42001-A.6 | — | design review | — |
| SEC-DATA-001.R1 | SEC-DATA-001 | CTL-NIST-SC-8, CTL-NIST-SC-28, CTL-ISO-A.8.24 | — | GR-004 (checkov:CKV_AWS_103, checkov:CKV_AZURE_15, opa:cloud.net.tls_min_1_2) | — |
| SEC-DATA-001.R2 | SEC-DATA-001 | CTL-NIST-SC-8, CTL-NIST-SC-28, CTL-ISO-A.8.24 | — | GR-005 (checkov:CKV_AWS_16, checkov:CKV_AWS_19, checkov:CKV_AZURE_2, opa:cloud.data.encryption_at_rest) | — |
| SEC-DATA-001.R3 | SEC-DATA-001 | CTL-NIST-SC-8, CTL-NIST-SC-28, CTL-ISO-A.8.24 | PAT-DATA-001 | design review | — |
| SEC-DATA-002.R1 | SEC-DATA-002 | CTL-NIST-SC-28, CTL-PCI-3.5, CTL-ISO-A.8.11 | — | design review | — |
| SEC-DATA-002.R2 | SEC-DATA-002 | CTL-NIST-SC-28, CTL-PCI-3.5, CTL-ISO-A.8.11 | — | design review | — |
| SEC-DATA-002.R3 | SEC-DATA-002 | CTL-NIST-SC-28, CTL-PCI-3.5, CTL-ISO-A.8.11 | PAT-DATA-001 | design review | — |
| SEC-DATA-002.R4 | SEC-DATA-002 | CTL-NIST-SC-28, CTL-PCI-3.5, CTL-ISO-A.8.11 | — | design review | — |
| SEC-IAM-001.R1 | SEC-IAM-001 | CTL-NIST-IA-9, CTL-NIST-AC-6, CTL-ISO-A.5.16 | PAT-IAM-002 | GR-001 (checkov:CKV_AWS_273, opa:cloud.iam.no_static_keys) | EXC-2026-001 |
| SEC-IAM-001.R2 | SEC-IAM-001 | CTL-NIST-IA-9, CTL-NIST-AC-6, CTL-ISO-A.5.16 | — | design review | — |
| SEC-IAM-001.R3 | SEC-IAM-001 | CTL-NIST-IA-9, CTL-NIST-AC-6, CTL-ISO-A.5.16 | — | GR-002 (checkov:CKV_AWS_62, checkov:CKV_AWS_63, opa:cloud.iam.no_admin_wildcard) | — |
| SEC-IAM-001.R4 | SEC-IAM-001 | CTL-NIST-IA-9, CTL-NIST-AC-6, CTL-ISO-A.5.16 | PAT-IAM-002 | design review | — |
| SEC-IAM-002.R1 | SEC-IAM-002 | CTL-NIST-IA-2, CTL-NIST-AC-2, CTL-ISO-A.8.2 | PAT-IAM-001 | design review | — |
| SEC-IAM-002.R2 | SEC-IAM-002 | CTL-NIST-IA-2, CTL-NIST-AC-2, CTL-ISO-A.8.2 | PAT-IAM-001 | design review | — |
| SEC-IAM-002.R3 | SEC-IAM-002 | CTL-NIST-IA-2, CTL-NIST-AC-2, CTL-ISO-A.8.2 | — | GR-003 (opa:cloud.iam.prod_admin_via_pam) | — |
| SEC-LOG-001.R1 | SEC-LOG-001 | CTL-NIST-AU-2, CTL-NIST-AU-6, CTL-ISO-A.8.15 | PAT-LOG-001 | GR-008 (opa:cloud.log.org_sink_enrolled) | — |
| SEC-LOG-001.R2 | SEC-LOG-001 | CTL-NIST-AU-2, CTL-NIST-AU-6, CTL-ISO-A.8.15 | — | design review | — |
| SEC-LOG-001.R3 | SEC-LOG-001 | CTL-NIST-AU-2, CTL-NIST-AU-6, CTL-ISO-A.8.15 | PAT-LOG-001 | design review | — |
| SEC-NET-001.R1 | SEC-NET-001 | CTL-NIST-SC-7, CTL-NIST-SI-4, CTL-ISO-A.8.20 | PAT-NET-001 | GR-006 (checkov:CKV2_AWS_28, opa:cloud.net.public_requires_waf) | — |
| SEC-NET-001.R2 | SEC-NET-001 | CTL-NIST-SC-7, CTL-NIST-SI-4, CTL-ISO-A.8.20 | — | GR-007 (checkov:CKV_AWS_88, checkov:CKV_AWS_17, opa:cloud.net.no_public_data_plane) | — |
| SEC-NET-001.R3 | SEC-NET-001 | CTL-NIST-SC-7, CTL-NIST-SI-4, CTL-ISO-A.8.20 | PAT-NET-001 | design review | — |
| SEC-NET-001.R4 | SEC-NET-001 | CTL-NIST-SC-7, CTL-NIST-SI-4, CTL-ISO-A.8.20 | — | design review | — |
| SEC-SEC-001.R1 | SEC-SEC-001 | CTL-NIST-IA-5, CTL-ISO-A.5.17 | PAT-SEC-001 | design review | — |
| SEC-SEC-001.R2 | SEC-SEC-001 | CTL-NIST-IA-5, CTL-ISO-A.5.17 | — | GR-009 (gitleaks:default, checkov:CKV_SECRET_*) | — |
| SEC-SEC-001.R3 | SEC-SEC-001 | CTL-NIST-IA-5, CTL-ISO-A.5.17 | PAT-SEC-001 | design review | — |

**Guardrail automation coverage: 9/28 requirements (32%)** — tracked against strategy theme T2.
