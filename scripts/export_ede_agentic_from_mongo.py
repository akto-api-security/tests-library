#!/usr/bin/env python3
"""
Write EDE templates from MongoDB to Excessive-Data-Exposure/*_AGENTIC.yml in this repo.

Reads yaml_templates where info.category.name is EDE (originals only), applies
build_agentic_doc(), writes one file per template.

Env: MONGO_URI (default mongodb://127.0.0.1:27017/), MONGO_DB (1000000), MONGO_COLLECTION (yaml_templates)
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import yaml
from pymongo import MongoClient

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

from generate_agentic_templates import build_agentic_doc, yaml_dump

REPO_ROOT = SCRIPTS_DIR.parent
OUT_DIR = REPO_ROOT / "Excessive-Data-Exposure"


def main() -> int:
    uri = os.environ.get("MONGO_URI", "mongodb://127.0.0.1:27017/")
    db_name = os.environ.get("MONGO_DB", "1000000")
    coll_name = os.environ.get("MONGO_COLLECTION", "yaml_templates")

    client = MongoClient(uri, serverSelectionTimeoutMS=8000)
    client.admin.command("ping")
    col = client[db_name][coll_name]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    docs = list(col.find({"info.category.name": "EDE"}))
    written = 0
    errors = 0
    for doc in docs:
        oid = doc["_id"]
        if str(oid).endswith("_AGENTIC"):
            continue
        try:
            parsed = yaml.safe_load(doc.get("content") or "")
        except Exception:
            errors += 1
            continue
        if not isinstance(parsed, dict):
            errors += 1
            continue
        new_yaml = build_agentic_doc(parsed)
        out_path = OUT_DIR / f"{oid}_AGENTIC.yml"
        out_path.write_text(yaml_dump(new_yaml), encoding="utf-8")
        written += 1

    print(f"Wrote {written} file(s) to {OUT_DIR.relative_to(REPO_ROOT)}/")
    if errors:
        print(f"Skipped (parse/errors): {errors}", file=sys.stderr)
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
