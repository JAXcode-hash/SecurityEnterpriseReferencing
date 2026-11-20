# Instructions for AI agents

This repository is the **enterprise security guidance source** (standards,
requirements, patterns, guardrail mappings, review records, exceptions,
strategy). It is large on purpose. **Do not read it wholesale.**

## Rules
1. **Never glob/read the whole repo or whole folders.** Always resolve context first:
   ```bash
   python tools/resolve_context.py --profile <path/to/design-profile.yaml> --purpose <design|review|build|strategy>
   ```
   This returns only the documents whose `applies_to` tags match the design (brief: IDs + summaries).
2. **Open full text only for what you need**:
   `python tools/resolve_context.py --get SEC-NET-001 PAT-NET-001`
3. If the design has no `design-profile.yaml`, create one from
   `designs/_template/design-profile.yaml` using only values from `taxonomy/tags.yaml`,
   and ask the user to confirm the classification and exposure. **Do not guess them.**
4. **Cite requirement IDs** (`SEC-IAM-001.R2`) for every compliance claim. For each
   in-scope requirement state: Met / Partially met / Not met / N/A with evidence.
5. If a requirement has a guardrail (`GR-*`), say it is enforced by the
   Architecture-as-Code pipeline and name the rule IDs; only non-guardrailed
   requirements need design-review evidence.
6. A requirement that cannot be met → propose an exception using `templates/exception.md`.
   Never silently drop a requirement. Respect only **non-expired** exceptions.
7. Documents marked `status: draft` are guidance, not mandatory — flag them as such.
8. Do not edit `standards/`, `patterns/` or `guardrails/` unless explicitly asked
   to author guidance. After any edit run `python tools/validate.py && python tools/build_index.py`.

## Purposes
| Purpose | Use when | Gets |
|---------|----------|------|
| `design` | Writing/updating a security design | core, standards, patterns, guardrails, exceptions, decisions |
| `review` | Reviewing a design / producing an ASR | core, standards, checklists, guardrails, exceptions, prior reviews |
| `build` | Generating IaC / code | core, standards, patterns, guardrails |
| `strategy` | Strategy, roadmap, progression | core, strategy, decisions |
