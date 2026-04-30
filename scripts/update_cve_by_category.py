#!/usr/bin/env python3
"""Update only the ``info.cve`` field on every YAML under
AI-Agent-tests/generated_tests/, based on the OWASP Agentic category that is
already set on each template (``info.category.name``).

The CVE list per category is the strict allowlist supplied by the maintainer.
No other CVE is added. Categories not present in the map (or explicitly
mapped to an empty list) get ``cve: []``.

Run from the repo root::

    python3 scripts/update_cve_by_category.py
"""

from __future__ import annotations

import collections
from pathlib import Path

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedSeq


REPO_ROOT = Path(__file__).resolve().parents[1]
GEN_DIR = REPO_ROOT / "AI-Agent-tests" / "generated_tests"


# Strict, maintainer-supplied CVE allowlist keyed by OWASP Agentic category.
# Order is preserved as supplied (caller can re-order here if needed). Any
# category not listed below - or listed with an empty list - clears CVE on
# every template in that category.
CVE_BY_CATEGORY: dict[str, list[str]] = {
    "AGENT_GOAL_HIJACK": [
        "CVE-2025-32711",
        "CVE-2025-53773",
    ],
    "TOOL_MISUSE_AND_EXPLOITATION": [
        "CVE-2025-54795",
        "CVE-2026-30615",
        "CVE-2025-34291",
    ],
    "IDENTITY_AND_PRIVILEGE_ABUSE": [
        "CVE-2025-52882",
        "CVE-2025-54130",
    ],
    "AGENTIC_SUPPLY_CHAIN": [
        "CVE-2025-59828",
    ],
    "MEMORY_AND_CONTEXT_POISONING": [
        "CVE-2026-30615",
    ],
    "INSECURE_INTER_AGENT_COMMUNICATION": [
        "CVE-2025-52882",
    ],
    "UNEXPECTED_CODE_EXECUTION": [
        "CVE-2025-53773",
        "CVE-2025-52882",
        "CVE-2025-34291",
    ],
    # Categories explicitly emptied by the maintainer:
    "ROGUE_AGENTS": [],
    "HUMAN_AGENT_TRUST_EXPLOITATION": [],
    "CASCADING_FAILURES": [],
}


def _category_of(data: dict) -> str:
    info = data.get("info") or {}
    cat = info.get("category") or {}
    if isinstance(cat, dict):
        return str(cat.get("name") or "")
    return ""


def _cve_list_equal(a, b: list[str]) -> bool:
    return list(a or []) == list(b or [])


def main() -> None:
    yl = YAML()
    yl.preserve_quotes = True
    yl.default_flow_style = False
    yl.allow_unicode = True
    yl.width = 4096
    yl.indent(mapping=2, sequence=4, offset=2)
    yl.explicit_start = True

    stats: collections.Counter[str] = collections.Counter()
    cve_per_cat: collections.defaultdict[str, collections.Counter[str]] = (
        collections.defaultdict(collections.Counter)
    )
    unknown_categories: collections.Counter[str] = collections.Counter()

    for path in sorted(GEN_DIR.glob("*.yml")):
        stats["files"] += 1
        with open(path, encoding="utf-8") as f:
            data = yl.load(f)
        if not isinstance(data, dict):
            continue
        info = data.setdefault("info", {})

        cat = _category_of(data)
        if not cat:
            stats["missing_category"] += 1
            continue

        if cat not in CVE_BY_CATEGORY:
            unknown_categories[cat] += 1
            stats["unknown_category"] += 1
            # Defensive: do not silently invent CVEs - leave the file alone.
            continue

        new_cve = CVE_BY_CATEGORY[cat]
        old_cve = info.get("cve")

        if _cve_list_equal(old_cve, new_cve):
            stats["unchanged"] += 1
            cve_per_cat[cat]["unchanged"] += 1
            continue

        if new_cve:
            seq = CommentedSeq(new_cve)
        else:
            seq = []
        info["cve"] = seq
        stats["updated"] += 1
        cve_per_cat[cat]["updated"] += 1

        with open(path, "w", encoding="utf-8") as f:
            yl.dump(data, f)

    print("=== Summary ===")
    for k, v in sorted(stats.items()):
        print(f"  {k:18s} {v}")

    print("\n=== Per-category counts ===")
    for cat in sorted(CVE_BY_CATEGORY):
        cves = ", ".join(CVE_BY_CATEGORY[cat]) or "(empty)"
        c = cve_per_cat.get(cat, collections.Counter())
        print(f"  {cat:35s} updated={c.get('updated', 0):4d}  unchanged={c.get('unchanged', 0):4d}  cve=[{cves}]")

    if unknown_categories:
        print("\n=== Unknown categories (left untouched) ===")
        for cat, n in unknown_categories.most_common():
            print(f"  {cat:40s} {n} files")


if __name__ == "__main__":
    main()
