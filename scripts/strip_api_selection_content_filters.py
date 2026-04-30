#!/usr/bin/env python3
"""Remove contains / not_contains / contains_either from api_selection_filters in *_AGENTIC templates."""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import yaml

from generate_agentic_templates import strip_api_selection_content_filters, yaml_dump

REPO_ROOT = SCRIPTS_DIR.parent


def process_doc(doc: dict) -> tuple[dict, bool]:
    if not isinstance(doc, dict) or "api_selection_filters" not in doc:
        return doc, False
    before = yaml.dump(doc.get("api_selection_filters"), default_flow_style=False, sort_keys=True)
    filt = doc["api_selection_filters"]
    if isinstance(filt, dict):
        doc["api_selection_filters"] = strip_api_selection_content_filters(filt)
    after = yaml.dump(doc.get("api_selection_filters"), default_flow_style=False, sort_keys=True)
    return doc, before != after


def main() -> int:
    changed = 0
    errors = 0
    for ext in ("*_AGENTIC.yml", "*_AGENTIC.yaml"):
        for path in sorted(REPO_ROOT.rglob(ext)):
            if SCRIPTS_DIR in path.parents or ".git" in path.parts:
                continue
            try:
                text = path.read_text(encoding="utf-8")
                doc = yaml.safe_load(text)
            except Exception as e:
                print(f"{path}: load error {e}", file=sys.stderr)
                errors += 1
                continue
            if not isinstance(doc, dict):
                continue
            new_doc, did = process_doc(doc)
            if not did:
                continue
            try:
                path.write_text(yaml_dump(new_doc), encoding="utf-8")
                changed += 1
            except Exception as e:
                print(f"{path}: write error {e}", file=sys.stderr)
                errors += 1
    print(f"Updated {changed} file(s). Errors: {errors}.")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
