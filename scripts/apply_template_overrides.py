#!/usr/bin/env python3
"""
Apply per-template CWE / CVE / category overrides to a hand-picked set of
agentic generated_tests/*.yml. Reuses TEMPLATE_OVERRIDES + DISPLAY_NAME from
scripts/enrich_agentic_generated_tests.py so the two stay in sync.

Run from repo root:  python3 scripts/apply_template_overrides.py
"""
from __future__ import annotations

import json
from pathlib import Path

from ruamel.yaml import YAML

from enrich_agentic_generated_tests import (  # type: ignore[import-not-found]
    DISPLAY_NAME,
    GEN_DIR,
    TEMPLATE_OVERRIDES,
)


def main() -> None:
    yl = YAML()
    yl.preserve_quotes = True
    yl.default_flow_style = False
    yl.allow_unicode = True
    yl.width = 4096
    yl.indent(mapping=2, sequence=4, offset=2)
    yl.explicit_start = True

    summary = {"updated": 0, "missing": [], "unchanged": 0}

    for tid, override in TEMPLATE_OVERRIDES.items():
        path = GEN_DIR / f"{tid}.yml"
        if not path.exists():
            summary["missing"].append(tid)
            continue

        with open(path, encoding="utf-8") as f:
            data = yl.load(f)

        info = data.setdefault("info", {})
        cat_block = info.setdefault("category", {})
        new_cat = override["category"]
        cat_block["name"] = new_cat
        cat_block["shortName"] = new_cat
        cat_block["displayName"] = DISPLAY_NAME.get(
            new_cat, str(new_cat).replace("_", " ").title()
        )

        info["cwe"] = list(override["cwe"])
        info["cve"] = list(override["cve"])

        with open(path, "w", encoding="utf-8") as f:
            yl.dump(data, f)
        summary["updated"] += 1

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
