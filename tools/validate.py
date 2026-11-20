#!/usr/bin/env python3
"""Validate repository integrity so agents can trust the metadata.

Checks: required fields, unique IDs, tags in taxonomy, cross-references resolve,
design profiles use valid tags, exceptions not expired, `load: always` stays small.
Exit code 1 on errors (use in CI / pre-commit).
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from hub import ROOT, is_expired, load_controls, load_docs, load_taxonomy  # noqa: E402

REQUIRED = ("id", "type", "title", "status", "summary")
ALWAYS_BUDGET = 2500  # tokens across all load:always docs


def check_tags(where: str, applies: dict, facets: dict, errors: list[str]):
    for facet, vals in (applies or {}).items():
        if facet not in facets:
            errors.append(f"{where}: unknown facet '{facet}'")
            continue
        vals = vals if isinstance(vals, list) else [vals]
        for v in vals:
            if v not in facets[facet]["values"]:
                errors.append(f"{where}: '{v}' not a valid value for '{facet}'")


def main() -> int:
    tax, docs = load_taxonomy(), load_docs()
    facets, errors, warnings = tax["facets"], [], []

    seen: dict[str, str] = {}
    for d in docs:
        for f in REQUIRED:
            if not getattr(d, f, None) and not d.meta.get(f):
                errors.append(f"{d.path}: missing '{f}'")
        if d.type not in tax["doc_types"]:
            errors.append(f"{d.path}: unknown type '{d.type}'")
        if d.id in seen:
            errors.append(f"{d.path}: duplicate id {d.id} (also {seen[d.id]})")
        seen[d.id] = d.path
        check_tags(d.path, d.applies_to, facets, errors)
        if d.type == "exception":
            if not d.meta.get("expires"):
                errors.append(f"{d.path}: exception without 'expires'")
            elif is_expired(d):
                warnings.append(f"{d.path}: exception {d.id} has EXPIRED")

    # cross references
    ids = set(seen)
    reqs = {r for d in docs for r in (d.meta.get("requirements") or [])}
    controls = set(load_controls())
    for d in docs:
        for r in (d.meta.get("implements") or []) + (d.meta.get("waives") or []):
            if r not in reqs:
                errors.append(f"{d.path}: references unknown requirement {r}")
        if d.type == "guardrail" and d.meta.get("requirement") not in reqs:
            errors.append(f"{d.path}: guardrail maps unknown requirement {d.meta.get('requirement')}")
        for k in ("patterns", "guardrails"):
            for r in d.meta.get(k) or []:
                if r not in ids:
                    errors.append(f"{d.path}: {k} -> unknown id {r}")
        for c in d.meta.get("controls") or []:
            if c not in controls:
                errors.append(f"{d.path}: unknown control {c}")
        for r in d.meta.get("requirements") or []:
            if not r.startswith(d.id + ".R"):
                errors.append(f"{d.path}: requirement {r} must be prefixed {d.id}.R")
            elif r.split(".")[-1] not in d.body:
                warnings.append(f"{d.path}: {r} declared but not found in body")

    always = sum(d.tokens for d in docs if d.load_always)
    if always > ALWAYS_BUDGET:
        warnings.append(f"load:always docs total ~{always} tokens (> {ALWAYS_BUDGET}); keep core small")

    for p in ROOT.glob("designs/**/design-profile.yaml"):
        if "_template" in p.parts:
            continue
        prof = (yaml.safe_load(p.read_text()) or {}).get("profile", {})
        check_tags(p.relative_to(ROOT).as_posix(), prof, facets, errors)

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(docs)} documents, {len(reqs)} requirements, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
