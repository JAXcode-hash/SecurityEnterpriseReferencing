#!/usr/bin/env python3
"""Generate index/context-index.json and index/traceability.md.

The JSON index is what external tooling (an MCP server, a RAG pipeline, the
AaC programme's attestation pipeline) should consume instead of crawling the repo.
The traceability matrix links requirement -> standard -> controls -> patterns -> guardrails -> AaC rules.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from hub import ROOT, load_docs  # noqa: E402


def main() -> int:
    docs = load_docs()
    out = ROOT / "index"
    out.mkdir(exist_ok=True)
    index = [{"id": d.id, "type": d.type, "title": d.title, "status": d.status, "path": d.path,
              "summary": d.summary, "applies_to": d.applies_to, "load_always": d.load_always,
              "refs": d.refs(), "est_tokens": d.tokens} for d in docs]
    (out / "context-index.json").write_text(json.dumps(index, indent=2, default=str) + "\n")

    implemented_by, guarded_by, waived_by = defaultdict(list), defaultdict(list), defaultdict(list)
    for d in docs:
        for r in d.meta.get("implements") or []:
            implemented_by[r].append(d.id)
        for r in d.meta.get("waives") or []:
            waived_by[r].append(d.id)
        if d.type == "guardrail":
            rules = [f"{k}:{x}" for k, v in (d.meta.get("aac_rules") or {}).items() for x in v]
            guarded_by[d.meta["requirement"]].append(f"{d.id} ({', '.join(rules)})")

    rows = ["# Traceability matrix (generated — do not edit)", "",
            "| Requirement | Standard | Controls | Patterns | Guardrails → AaC rules | Exceptions |",
            "|---|---|---|---|---|---|"]
    total = automated = 0
    for d in sorted((d for d in docs if d.type == "standard"), key=lambda d: d.id):
        for r in d.meta.get("requirements") or []:
            total += 1
            automated += bool(guarded_by[r])
            rows.append(f"| {r} | {d.id} | {', '.join(d.meta.get('controls') or [])} | "
                        f"{', '.join(implemented_by[r]) or '—'} | {'; '.join(guarded_by[r]) or 'design review'} | "
                        f"{', '.join(waived_by[r]) or '—'} |")
    pct = round(100 * automated / total) if total else 0
    rows += ["", f"**Guardrail automation coverage: {automated}/{total} requirements ({pct}%)** "
             "— tracked against strategy theme T2."]
    (out / "traceability.md").write_text("\n".join(rows) + "\n")
    print(f"index: {len(index)} docs; traceability: {total} requirements, {pct}% automated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
