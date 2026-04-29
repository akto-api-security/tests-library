#!/usr/bin/env python3
"""
Rewrite info.cwe / info.cve in AI-Agent-tests/generated_tests/*.yml from
agentic_cwe_cve_mapping.json (category + UNEXPECTED_CODE_EXECUTION sub-type).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAPPING_PATH = ROOT / "agentic_cwe_cve_mapping.json"
GENERATED = ROOT / "generated_tests"

SHORTNAME_RE = re.compile(
    r"^(\s+)shortName:\s*(\S+)\s*$",
    re.MULTILINE,
)
SUBCAT_RE = re.compile(
    r"^(\s+)subCategory:\s*(\S+)\s*$",
    re.MULTILINE,
)
CWE_BLOCK_RE = re.compile(
    r"^(\s+)cwe:\s*\n(?:\1- [^\n]+\n)+",
    re.MULTILINE,
)
CVE_BLOCK_RE = re.compile(
    r"^(\s+)cve:\s*\n(?:\1- [^\n]+\n)+",
    re.MULTILINE,
)


def load_mapping() -> dict:
    with open(MAPPING_PATH, encoding="utf-8") as f:
        return json.load(f)


def yaml_list_block(indent: str, key: str, items: list[str]) -> str:
    lines = [f"{indent}{key}:"]
    for x in items:
        lines.append(f"{indent}- {x}")
    lines.append("")
    return "\n".join(lines)


def resolve_entry(
    mapping: dict,
    short_name: str,
    sub_category: str,
) -> tuple[list[str], list[str]]:
    if short_name == "UNEXPECTED_CODE_EXECUTION":
        u = mapping["unexpected_code_execution"]
        if sub_category.startswith("SECURITY_XSS"):
            e = u["SECURITY_XSS"]
        else:
            e = u["CODE_EXECUTION_OR_RCE"]
        return list(e["cwe"]), list(e["cve"])
    by_cat = mapping["by_category"]
    if short_name not in by_cat:
        raise KeyError(f"Unknown category shortName: {short_name}")
    e = by_cat[short_name]
    return list(e["cwe"]), list(e["cve"])


def replace_cwe_cve(text: str, cwes: list[str], cves: list[str]) -> str:
    m_cwe = CWE_BLOCK_RE.search(text)
    m_cve = CVE_BLOCK_RE.search(text)
    if not m_cwe or not m_cve:
        raise ValueError("Could not find cwe:/cve: blocks")
    indent_cwe = m_cwe.group(1)
    indent_cve = m_cve.group(1)
    new_cwe = yaml_list_block(indent_cwe, "cwe", cwes).rstrip("\n")
    new_cve = yaml_list_block(indent_cve, "cve", cves).rstrip("\n")
    text = CWE_BLOCK_RE.sub(new_cwe + "\n", text, count=1)
    text = CVE_BLOCK_RE.sub(new_cve + "\n", text, count=1)
    return text


def patch_file(path: Path, mapping: dict, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    sm = SHORTNAME_RE.search(text)
    subm = SUBCAT_RE.search(text)
    if not sm or not subm:
        print(f"skip (missing shortName/subCategory): {path.name}", file=sys.stderr)
        return False
    short_name = sm.group(2)
    sub_category = subm.group(2)
    cwes, cves = resolve_entry(mapping, short_name, sub_category)
    new_text = replace_cwe_cve(text, cwes, cves)
    if new_text == text:
        return False
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print how many files would change without writing",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="YAML files to patch (default: all in generated_tests/)",
    )
    args = parser.parse_args()
    mapping = load_mapping()
    paths = list(args.paths) if args.paths else sorted(GENERATED.glob("*.yml"))
    changed = 0
    for p in paths:
        if patch_file(p, mapping, args.dry_run):
            changed += 1
    print(f"{'Would patch' if args.dry_run else 'Patched'} {changed} / {len(paths)} files")


if __name__ == "__main__":
    main()
