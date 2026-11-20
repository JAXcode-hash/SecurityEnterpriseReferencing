"""Shared loader and matching logic for the Security Context Hub.

Every piece of guidance is turned into a `Doc` with:
  id, type, title, status, summary, applies_to, refs, path, body
so the resolver, validator and index builder all see the same model.
"""
from __future__ import annotations

import datetime as dt
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.S)
SKIP_DIRS = {"templates", "designs", "index", "tools", ".git", ".github", ".claude"}
REF_FIELDS = ("requirements", "controls", "patterns", "guardrails", "implements", "waives")


@dataclass
class Doc:
    id: str
    type: str
    title: str
    path: str
    status: str = "approved"
    summary: str = ""
    applies_to: dict = field(default_factory=dict)
    load_always: bool = False
    meta: dict = field(default_factory=dict)
    body: str = ""

    @property
    def tokens(self) -> int:  # rough estimate, good enough for budgeting
        return max(1, len(self.body) // 4)

    def refs(self) -> dict[str, list[str]]:
        return {k: list(self.meta.get(k) or []) for k in REF_FIELDS if self.meta.get(k)}


def load_taxonomy() -> dict:
    return yaml.safe_load((ROOT / "taxonomy" / "tags.yaml").read_text())


def _rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def load_docs() -> list[Doc]:
    docs: list[Doc] = []
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or set(p.relative_to(ROOT).parts) & SKIP_DIRS:
            continue
        if p.suffix == ".md" and p.name != "README.md":
            m = FRONTMATTER.match(p.read_text())
            if not m:
                continue
            fm, body = yaml.safe_load(m.group(1)) or {}, m.group(2).strip()
            docs.append(_doc_from(fm, _rel(p), body))
        elif p.suffix in (".yaml", ".yml") and p.parent.name != "taxonomy":
            data = yaml.safe_load(p.read_text()) or {}
            if "guardrails" in data:  # one file -> many guardrail docs
                for g in data["guardrails"]:
                    body = yaml.safe_dump(g, sort_keys=False)
                    docs.append(Doc(
                        id=g["id"], type="guardrail", title=g["description"],
                        path=f"{_rel(p)}#{g['id']}", summary=g["description"]
                        + f" (enforces {g['requirement']}, {g['enforcement']})",
                        applies_to=g.get("applies_to") or {}, meta=g, body=body))
            elif data.get("type") == "strategy":
                docs.append(_doc_from(data, _rel(p), yaml.safe_dump(data, sort_keys=False)))
    return docs


def _doc_from(fm: dict, path: str, body: str) -> Doc:
    return Doc(
        id=str(fm.get("id", path)), type=fm.get("type", "unknown"),
        title=fm.get("title", path), path=path, status=str(fm.get("status", "approved")),
        summary=" ".join(str(fm.get("summary", "")).split()),
        applies_to=fm.get("applies_to") or {}, load_always=fm.get("load") == "always",
        meta=fm, body=body)


def load_controls() -> dict:
    return yaml.safe_load((ROOT / "controls" / "framework-mappings.yaml").read_text())["controls"]


# ---------------------------------------------------------------- matching ---

def _as_list(v) -> list:
    if v is None:
        return []
    return list(v) if isinstance(v, (list, tuple, set)) else [v]


def match(doc: Doc, profile: dict, taxonomy: dict) -> tuple[bool, int, list[str]]:
    """Return (applies, specificity, reasons).

    A facet the doc does not declare is unconstrained. Each declared facet must
    overlap with the profile. Ordinal facets match when the profile is at or
    above the doc's lowest declared level.
    """
    facets = taxonomy["facets"]
    reasons, score = [], 0
    for facet, wanted in (doc.applies_to or {}).items():
        wanted = _as_list(wanted)
        if not wanted:
            continue
        have = _as_list(profile.get(facet))
        spec = facets.get(facet, {})
        if spec.get("ordinal"):
            order = spec["values"]
            levels = [order.index(v) for v in have if v in order]
            floor = min(order.index(v) for v in wanted if v in order)
            if not levels or max(levels) < floor:
                return False, 0, []
            reasons.append(f"{facet}>={order[floor]}")
        else:
            hit = sorted(set(wanted) & set(have))
            if not hit:
                return False, 0, []
            reasons.append(f"{facet}:{','.join(hit)}")
        score += 1
    return True, score, reasons or ["universal"]


def is_expired(doc: Doc, today: dt.date | None = None) -> bool:
    exp = doc.meta.get("expires")
    if not exp:
        return False
    exp = exp if isinstance(exp, dt.date) else dt.date.fromisoformat(str(exp))
    return exp < (today or dt.date.today())
