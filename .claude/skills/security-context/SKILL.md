---
name: security-context
description: Load ONLY the enterprise security standards, requirements, patterns, guardrails and exceptions relevant to a specific design. Use when writing a security design, threat model, architecture/security review, IaC that must meet security controls, or when asked whether a design complies with security standards.
---

# Security context retrieval

1. Locate the design's `design-profile.yaml` (in the design folder or the app repo).
   If missing, draft one from `designs/_template/design-profile.yaml` with values from
   `taxonomy/tags.yaml`; confirm `data_classification` and `exposure` with the user.
2. Resolve the briefing (choose the purpose that fits the task):
   ```bash
   python tools/resolve_context.py --profile <profile> --purpose design
   ```
3. Read the summaries. Fetch full text only for the docs you need:
   ```bash
   python tools/resolve_context.py --get <ID> [<ID> ...]
   ```
4. Produce output using `designs/_template/security-design.md` (designs) or
   `templates/review-record.md` (reviews). Every requirement in scope gets a row
   with status + evidence; name guardrail rule IDs where enforcement is automated.
5. For gaps, draft exceptions from `templates/exception.md` — never drop requirements.

If the resolver lists more than ~30 docs, the profile is probably too broad: check
that `components`/`integrations` only list what the design actually uses.
