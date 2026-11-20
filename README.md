# SecurityEnterpriseReferencing — Security Context Hub

Enterprise security guidance as **machine-routable context** for AI-assisted
design, architecture review and build workflows.

It is the security counterpart to the CTO/CIO **Architecture-as-Code (AaC)**
programme. AaC checks that code matches cloud patterns and guardrails. This
repo holds the security *intent*: standards, testable requirements and approved
integration patterns. It links each requirement to the AaC rules that enforce it.

## Core idea: an agent only gets what applies to its design

```
design-profile.yaml ──► tools/resolve_context.py ──► briefing: IDs + summaries (small)
 (cloud, exposure,          matches applies_to tags         │
  classification,           on every document               ▼
  components, integrations)                         agent fetches full text with --get <ID>
```

1. **Every document has frontmatter**: `id`, `type`, `status`, `summary` and `applies_to`
   (facets from [`taxonomy/tags.yaml`](taxonomy/tags.yaml)).
2. **Every design declares a profile** ([template](designs/_template/design-profile.yaml)).
3. **The resolver matches profile ↔ tags.** Any facet a document does not declare is unconstrained.
   A facet it does declare must overlap with the profile. Data classification is ordinal:
   a document tagged `confidential` also applies to `restricted`.
4. **Progressive disclosure**: the agent gets a brief first, then fetches full text by ID.
   `--format full --budget N` caps the total size when you need everything in one go.
5. **Exceptions and guardrails** are included only when the requirement they touch is in scope.
   Expired exceptions are dropped automatically.

| Example design | Profile | Docs resolved |
|----------------|---------|---------------|
| `payments-api` | internet + partner, restricted, PCI, k8s | 27 |
| `internal-reporting` | internal, internal data, PaaS | 18 (no edge/PCI/KMS guidance) |
| `ai-assistant` | internal, confidential, AI/ML | AI standard + checklist added, no edge guidance |

## Layout

```
core/                     Always-loaded, kept tiny (<2.5k tokens): principles, ID conventions
taxonomy/tags.yaml        Controlled vocabulary + which doc types each purpose gets
strategy/                 Strategy docs + roadmap.yaml (maturity / progression per theme)
standards/<domain>/       Normative standards; requirements SEC-<DOM>-nnn.Rn
patterns/                 Approved security integration patterns (IdP, KMS, SIEM, edge, secrets)
guardrails/               Requirement → AaC/policy-as-code rule mapping (Checkov, OPA, ...)
controls/                 NIST 800-53 / ISO 27001 / PCI / AI framework references
architecture-reviews/     Process, tag-scoped checklists, review records (ASR-*)
exceptions/               Time-bound risk acceptances (EXC-*), must have expiry
decisions/                Security decision records (SDR-*)
designs/                  _template/ (profile, security design, threat model) + examples
templates/                Authoring templates for new standards, patterns, exceptions, reviews
index/                    GENERATED: context-index.json, traceability.md
tools/                    resolve_context.py, validate.py, build_index.py
AGENTS.md / CLAUDE.md     Agent operating rules; .claude/skills/security-context/ skill
```

## Usage

```bash
pip install -r requirements.txt

# Brief for a design (default purpose: design)
python tools/resolve_context.py --profile designs/examples/payments-api/design-profile.yaml

# Review mode, full text, capped at 15k tokens, with control framework mappings
python tools/resolve_context.py --profile <profile> --purpose review --format full --budget 15000 --with-controls

# Fetch specific documents (requirement IDs resolve to their standard)
python tools/resolve_context.py --get SEC-NET-001.R3 PAT-NET-001

# Machine-readable output for pipelines / MCP servers
python tools/resolve_context.py --profile <profile> --format json

# After any change
python tools/validate.py && python tools/build_index.py
```

## Using it from application / design repos

- **Claude Code / agent workflows:** add this repo as a git submodule or a sibling checkout,
  e.g. `vendor/security-context-hub`. Reference it from the app repo's `CLAUDE.md`/`AGENTS.md`:
  *"For security guidance run `python vendor/security-context-hub/tools/resolve_context.py --profile docs/security/design-profile.yaml`; do not read the hub directly."*
  You can also copy `.claude/skills/security-context/` into the app repo.
- **Keep the design profile with the AaC artefacts** in the app repo. The same facts
  (cloud, exposure, classification) usually exist in AaC metadata already, so derive the profile from them.
- **AaC attestation:** `index/traceability.md` and `guardrails/guardrail-mapping.yaml` show which
  security requirements are already attested by AaC rules. Only the rest needs design-review evidence.
- **MCP:** `--format json` and `--get` map one-to-one onto two MCP tools
  (`resolve_security_context(profile, purpose)`, `get_security_doc(ids)`), so you can wrap them
  in a thin MCP server when you need org-wide access without checkouts.

## Authoring rules

- Use `templates/`. Each document needs a strong 1–3 sentence `summary`, because that is what agents read first.
- **Tag as narrowly as is true.** Use `applies_to: {}` (universal) only for guidance that really applies everywhere.
  Over-broad tags are the main cause of context bloat.
- Requirements are `MUST`/`MUST NOT` statements with an ID and a verification method.
- New facet values go into `taxonomy/tags.yaml` first. The validator rejects unknown tags.
- CI (`.github/workflows/validate.yml`) checks IDs, tags, cross-references, expiry and index freshness.

## Progression

`strategy/roadmap.yaml` tracks maturity per strategic theme.
`index/traceability.md` reports **guardrail automation coverage**: the share of requirements enforced as code.
This is the key metric linking the security strategy (theme T2) to the AaC programme.
