#!/usr/bin/env python3
"""Resolve ONLY the security guidance relevant to one design.

Progressive disclosure for AI agents:
  1. --format brief (default): ids, titles, summaries, paths, why it matched.
     Small enough to put in any prompt.
  2. --get SEC-IAM-001 [...]: full text of the specific docs the agent decides it needs.
  3. --format full: everything that matched, cut at --budget tokens
     (always-load docs first, then most specific matches).

Examples:
  python tools/resolve_context.py --profile designs/examples/payments-api/design-profile.yaml
  python tools/resolve_context.py --profile path/to/design-profile.yaml --purpose review --format full
  python tools/resolve_context.py --get SEC-NET-001 PAT-NET-001
  python tools/resolve_context.py --profile p.yaml --format json   # for MCP / pipeline use
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from hub import Doc, is_expired, load_controls, load_docs, load_taxonomy, match  # noqa: E402


def resolve(profile_doc: dict, purpose: str, taxonomy: dict, docs: list[Doc]):
    profile = profile_doc.get("profile", {})
    types = taxonomy["purposes"][purpose]
    include, exclude = set(profile_doc.get("include") or []), set(profile_doc.get("exclude") or [])
    picked: list[tuple[Doc, int, list[str]]] = []
    for d in docs:
        if d.id in exclude or d.status in ("deprecated", "rejected", "superseded"):
            continue
        if d.id in include:
            picked.append((d, 99, ["explicit include"]))
            continue
        if d.type not in types or (d.type == "exception" and is_expired(d)):
            continue
        if d.load_always:
            picked.append((d, 100, ["always"]))
            continue
        ok, score, why = match(d, profile, taxonomy)
        if ok:
            picked.append((d, score, why))

    # Exceptions/guardrails only matter if the requirement they touch is in scope.
    in_scope_reqs = {r for d, _, _ in picked for r in (d.meta.get("requirements") or [])}
    picked = [
        (d, s, w) for d, s, w in picked
        if d.type not in ("exception", "guardrail") or "explicit include" in w
        or set(d.meta.get("waives") or [d.meta.get("requirement")]) & in_scope_reqs
    ]
    order = {t: i for i, t in enumerate(types)}
    picked.sort(key=lambda x: (-int(x[0].load_always), order.get(x[0].type, 99), -x[1], x[0].id))
    return picked


def render(picked, fmt: str, budget: int, profile_doc: dict, purpose: str, with_controls: bool):
    name = profile_doc.get("name", "design")
    if fmt == "paths":
        return "\n".join(d.path for d, _, _ in picked)
    if fmt == "json":
        return json.dumps({
            "design": name, "purpose": purpose,
            "documents": [{"id": d.id, "type": d.type, "title": d.title, "status": d.status,
                           "path": d.path, "summary": d.summary, "matched_on": w,
                           "refs": d.refs(), "est_tokens": d.tokens} for d, _, w in picked],
        }, indent=2)

    out = [f"# Security context for `{name}` (purpose: {purpose})",
           f"{len(picked)} relevant documents. Cite requirement IDs (e.g. SEC-IAM-001.R1).", ""]
    if fmt == "brief":
        cur = None
        for d, _, why in picked:
            if d.type != cur:
                cur = d.type
                out.append(f"\n## {cur}")
            flag = " **[DRAFT]**" if d.status == "draft" else ""
            out.append(f"- **{d.id}** {d.title}{flag} — {d.summary}\n"
                       f"  `{d.path}` · matched: {', '.join(why)}")
            reqs = d.meta.get("requirements")
            if reqs:
                out.append(f"  requirements: {', '.join(reqs)}")
        out.append("\nFetch full text with: python tools/resolve_context.py --get <ID> [<ID> ...]")
    else:  # full
        used, omitted = 0, []
        for d, _, _ in picked:
            if used + d.tokens > budget and not d.load_always:
                omitted.append(d)
                continue
            used += d.tokens
            out += [f"\n---\n<!-- {d.id} | {d.path} -->", d.body]
        if omitted:
            out.append("\n---\n## Omitted (budget) — fetch with --get if needed")
            out += [f"- {d.id} {d.title} — {d.summary}" for d in omitted]
        out.insert(2, f"~{used} tokens of {budget} budget used.")

    if with_controls:
        ctl = load_controls()
        ids = sorted({c for d, _, _ in picked for c in (d.meta.get("controls") or [])})
        out.append("\n## Control framework mappings")
        out += [f"- {c}: {ctl.get(c, {}).get('framework', '?')} — {ctl.get(c, {}).get('title', '?')}"
                for c in ids]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--profile", help="path to a design-profile.yaml")
    ap.add_argument("--purpose", default="design", help="design | review | strategy | build")
    ap.add_argument("--format", default="brief", choices=["brief", "full", "paths", "json"])
    ap.add_argument("--budget", type=int, default=12000, help="token budget for --format full")
    ap.add_argument("--with-controls", action="store_true", help="append NIST/ISO/PCI mappings")
    ap.add_argument("--get", nargs="+", metavar="ID", help="print full text of specific docs")
    a = ap.parse_args()

    taxonomy, docs = load_taxonomy(), load_docs()
    if a.get:
        by_id = {d.id: d for d in docs}
        for i in a.get:
            base = i.split(".R")[0]  # allow SEC-IAM-001.R2 -> SEC-IAM-001
            d = by_id.get(base)
            print(f"\n---\n<!-- {base} | {d.path} -->\n{d.body}" if d else f"\n[not found: {i}]")
        return 0
    if not a.profile:
        ap.error("--profile or --get is required")
    if a.purpose not in taxonomy["purposes"]:
        ap.error(f"--purpose must be one of {list(taxonomy['purposes'])}")
    profile_doc = yaml.safe_load(Path(a.profile).read_text())
    picked = resolve(profile_doc, a.purpose, taxonomy, docs)
    print(render(picked, a.format, a.budget, profile_doc, a.purpose, a.with_controls))
    return 0


if __name__ == "__main__":
    sys.exit(main())
