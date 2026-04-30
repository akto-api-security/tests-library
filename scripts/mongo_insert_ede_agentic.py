#!/usr/bin/env python3
"""
Insert agentic copies of MongoDB yaml_templates where info.category.name is EDE.

Connects to local Mongo (default mongodb://127.0.0.1:27017/), database 1000000,
collection yaml_templates.

For each template with category EDE, inserts a new document:
  _id: {original_id}_AGENTIC
  content: YAML from build_agentic_doc() (id/category _AGENTIC, POST filter, etc.)
  info.category.name: EDE_AGENTIC (shortName/displayName unchanged)

Skips if {id}_AGENTIC already exists.

Usage:
  python3 scripts/mongo_insert_ede_agentic.py
  MONGO_URI=mongodb://127.0.0.1:27017/ python3 scripts/mongo_insert_ede_agentic.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import yaml
from pymongo import MongoClient

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from generate_agentic_templates import build_agentic_doc, yaml_dump


def main() -> int:
    uri = os.environ.get("MONGO_URI", "mongodb://127.0.0.1:27017/")
    db_name = os.environ.get("MONGO_DB", "1000000")
    coll_name = os.environ.get("MONGO_COLLECTION", "yaml_templates")

    client = MongoClient(uri, serverSelectionTimeoutMS=8000)
    client.admin.command("ping")
    col = client[db_name][coll_name]

    filter_ede = {"info.category.name": "EDE"}
    docs = list(col.find(filter_ede))
    inserted = 0
    skipped = 0
    errors: list[tuple[str, str]] = []

    for doc in docs:
        oid = doc["_id"]
        if str(oid).endswith("_AGENTIC"):
            skipped += 1
            continue
        new_id = f"{oid}_AGENTIC"
        if col.find_one({"_id": new_id}):
            skipped += 1
            continue
        content_str = doc.get("content") or ""
        try:
            parsed = yaml.safe_load(content_str)
        except Exception as e:
            errors.append((str(oid), f"YAML parse: {e}"))
            continue
        if not isinstance(parsed, dict):
            errors.append((str(oid), "content root not a mapping"))
            continue

        new_yaml = build_agentic_doc(parsed)
        new_content = yaml_dump(new_yaml)

        info = yaml.safe_load(yaml.dump(doc["info"]))
        if isinstance(info, dict) and isinstance(info.get("category"), dict):
            n = info["category"].get("name")
            if isinstance(n, str) and not n.endswith("_AGENTIC"):
                info["category"]["name"] = f"{n}_AGENTIC"

        new_doc = {
            "_id": new_id,
            "author": doc.get("author", "AKTO"),
            "content": new_content,
            "createdAt": doc.get("createdAt"),
            "hash": hash(new_content),
            "inactive": doc.get("inactive", False),
            "info": info,
            "source": doc.get("source", "AKTO_TEMPLATES"),
            "updatedAt": doc.get("updatedAt"),
        }
        try:
            col.insert_one(new_doc)
            inserted += 1
        except Exception as e:
            errors.append((str(oid), f"insert: {e}"))

    print(f"Database: {db_name}, collection: {coll_name}")
    print(f"EDE templates found: {len(docs)}")
    print(f"Inserted: {inserted}, skipped (already agentic or exists): {skipped}")
    if errors:
        print("Errors:", file=sys.stderr)
        for oid, msg in errors:
            print(f"  {oid}: {msg}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
