#!/usr/bin/env python3
"""
Generate *_AGENTIC templates for tests that mutate the request body AND use other execute ops
(e.g. replace_body + modify_url, modify_body_param + add_header).

Uses the same id/category/api_selection_filters transforms as generate_agentic_templates.build_agentic_doc.

Skips if {stem}_AGENTIC.{yml,yaml} already exists (e.g. strict agentic already generated).
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

from generate_agentic_templates import (
    REPO_ROOT,
    SCRIPTS_DIR as G_SCRIPTS,
    build_agentic_doc,
    template_mixed_body_and_other_ops,
    yaml_dump,
)

SKIP_LOG = SCRIPTS_DIR / "agentic_mixed_body_skips.txt"


def iter_base_templates():
    for ext in ("*.yml", "*.yaml"):
        for p in sorted(REPO_ROOT.rglob(ext)):
            if G_SCRIPTS in p.parents or "AI-Agent-tests" in p.parts or ".git" in p.parts:
                continue
            if p.name.startswith("."):
                continue
            if "_AGENTIC." in p.name:
                continue
            yield p


def main() -> int:
    generated = 0
    skips: list[tuple[str, str]] = []

    for path in iter_base_templates():
        rel = path.relative_to(REPO_ROOT)
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception as e:
            skips.append((str(rel), f"YAML parse error: {e}"))
            continue
        if not isinstance(doc, dict):
            skips.append((str(rel), "Root document is not a mapping."))
            continue

        ok, reason = template_mixed_body_and_other_ops(doc)
        if not ok:
            skips.append((str(rel), reason))
            continue

        out_name = f"{path.stem}_AGENTIC{path.suffix}"
        out_path = path.parent / out_name
        if out_path.exists():
            skips.append((str(rel), f"Already exists: {out_name}"))
            continue

        try:
            out_path.write_text(yaml_dump(build_agentic_doc(doc)), encoding="utf-8")
            generated += 1
        except Exception as e:
            skips.append((str(rel), f"Write error: {e}"))

    SKIP_LOG.write_text(
        "\n".join(f"{rel}\t{reason}" for rel, reason in sorted(skips)) + ("\n" if skips else ""),
        encoding="utf-8",
    )
    print(f"Generated {generated} mixed-body agentic template(s).")
    print(f"Skipped / logged: {len(skips)} -> {SKIP_LOG.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
