#!/usr/bin/env python3
"""
Remap OWASP Agentic categories and tweak template names for generated tests.

Usage (from repo root):

  cd /Users/karan/akto-repo/tests-library
  python3 scripts/remap_agentic_categories.py

This script applies the refined mapping strategy documented in
`AI-Agent-tests/agentic_category_mapping.txt`, including:

- Treating CASCADING_FAILURES as a specific-scope bucket.
- Moving hallucination correctness families from CASCADING_FAILURES to
  MEMORY_AND_CONTEXT_POISONING.
- Moving certain Safety content/fairness families from CASCADING_FAILURES
  to AGENT_GOAL_HIJACK.
- Keeping Hallucination Propagation tests in CASCADING_FAILURES and
  tagging their `info.name` with "(Cascading Failures)" between the
  vulnerability and strategy segments.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, Tuple

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
GEN_TESTS = REPO_ROOT / "AI-Agent-tests" / "generated_tests"


# Category display metadata: name -> (shortName, displayName)
CATEGORY_META: Dict[str, Tuple[str, str]] = {
    "AGENT_GOAL_HIJACK": ("AGENT_GOAL_HIJACK", "Agent Goal Hijack"),
    "TOOL_MISUSE_AND_EXPLOITATION": ("TOOL_MISUSE_AND_EXPLOITATION", "Tool Misuse and Exploitation"),
    "IDENTITY_AND_PRIVILEGE_ABUSE": ("IDENTITY_AND_PRIVILEGE_ABUSE", "Identity and Privilege Abuse"),
    "AGENTIC_SUPPLY_CHAIN": ("AGENTIC_SUPPLY_CHAIN", "Agentic Supply Chain Vulnerabilities"),
    "UNEXPECTED_CODE_EXECUTION": ("UNEXPECTED_CODE_EXECUTION", "Unexpected Code Execution"),
    "MEMORY_AND_CONTEXT_POISONING": ("MEMORY_AND_CONTEXT_POISONING", "Memory and Context Poisoning"),
    "INSECURE_INTER_AGENT_COMMUNICATION": ("INSECURE_INTER_AGENT_COMMUNICATION", "Insecure Inter-Agent Communication"),
    "CASCADING_FAILURES": ("CASCADING_FAILURES", "Cascading Failures"),
    "HUMAN_AGENT_TRUST_EXPLOITATION": ("HUMAN_AGENT_TRUST_EXPLOITATION", "Human-Agent Trust Exploitation"),
    "ROGUE_AGENTS": ("ROGUE_AGENTS", "Rogue Agents"),
}


# Prefix groups for remapping

# Hallucination families we want in MEMORY_AND_CONTEXT_POISONING
HALLU_TO_MEMORY_PREFIXES = [
    "HALLUCINATION_AND_TRUSTWORTHINESS_Q_A_",
    "HALLUCINATION_AND_TRUSTWORTHINESS_URL_CHECK_",
    "HALLUCINATION_AND_TRUSTWORTHINESS_CITATION_AND_SOURCE_VERIFICATION_",
    "HALLUCINATION_AND_TRUSTWORTHINESS_CONFIDENCE_CALIBRATION_",
    "HALLUCINATION_AND_TRUSTWORTHINESS_FACTUAL_ACCURACY_BENCHMARKING_",
    "HALLUCINATION_AND_TRUSTWORTHINESS_PARANOID_PROTECTION_",
]

# Hallucination families that *stay* in Cascading Failures
HALLU_PROP_PREFIX = "HALLUCINATION_AND_TRUSTWORTHINESS_HALLUCINATION_PROPAGATION_"

# Safety families we want in AGENT_GOAL_HIJACK (not Cascading Failures)
SAFETY_FROM_CASCADING_TO_GOAL = [
    "SAFETY_CONTENT_GENERATION_VS_INFORMATION_PROVISION_",
    "SAFETY_CULTURAL_REPRESENTATION_TESTING_",
    "SAFETY_FAIRNESS_METRIC_GENERATION_",
]


def infer_new_category(sub: str, current_cat: str) -> str:
    """Return the new category name given subCategory and current category."""
    # Hallucination propagation stays in Cascading Failures
    if sub.startswith(HALLU_PROP_PREFIX):
        return "CASCADING_FAILURES"

    # Move other hallucination trustworthiness families from Cascading to Memory
    if any(sub.startswith(p) for p in HALLU_TO_MEMORY_PREFIXES):
        return "MEMORY_AND_CONTEXT_POISONING"

    # Safety content/fairness/cultural from Cascading to Goal Hijack
    if any(sub.startswith(p) for p in SAFETY_FROM_CASCADING_TO_GOAL):
        return "AGENT_GOAL_HIJACK"

    # Default: keep existing
    return current_cat


def maybe_tag_cascade_in_name(info: dict) -> None:
    """
    For genuine Cascading Failures hallu-propagation tests, insert 'Cascading Failures'
    into the name between the vulnerability and strategy segments.

    Example:
      Before: "Hallucination and Trustworthiness - Hallucination Propagation - System Override"
      After:  "Hallucination and Trustworthiness - Hallucination Propagation (Cascading Failures) - System Override"
    """
    name = info.get("name") or ""
    cat = (info.get("category") or {}).get("name") or ""
    sub = info.get("subCategory") or ""

    if cat != "CASCADING_FAILURES":
        return
    if not sub.startswith(HALLU_PROP_PREFIX):
        return

    # Avoid double-tagging
    if "Cascading Failures" in name or "Cascading" in name:
        return

    parts = name.split(" - ")
    if len(parts) >= 3:
        # Insert before the last segment (strategy)
        parts[-2] = f"{parts[-2]} (Cascading Failures)"
        info["name"] = " - ".join(parts)
    else:
        # Fallback: append at the end
        info["name"] = f"{name} (Cascading Failures)"


def main() -> int:
    if not GEN_TESTS.is_dir():
        print(f"Missing generated_tests: {GEN_TESTS}", file=sys.stderr)
        return 1

    counts_before: Dict[str, int] = {}
    counts_after: Dict[str, int] = {}
    changed_files = 0
    renamed_names = 0

    for yml in sorted(GEN_TESTS.glob("*.yml")):
        if yml.name.startswith("_"):
            continue

        try:
            doc = yaml.safe_load(yml.read_text(encoding="utf-8")) or {}
        except Exception as e:
            print(f"{yml.name}: parse error {e}", file=sys.stderr)
            continue

        info = doc.get("info") or {}
        category = info.get("category") or {}
        current_cat = category.get("name") or "UNKNOWN"
        sub = info.get("subCategory") or ""
        old_name = info.get("name") or ""

        counts_before[current_cat] = counts_before.get(current_cat, 0) + 1

        new_cat = infer_new_category(sub, current_cat)

        # After category choice, decide on new name (for cascade tests)
        info_for_name = dict(info)
        info_for_name.setdefault("category", {})["name"] = new_cat
        before_name = old_name
        maybe_tag_cascade_in_name(info_for_name)
        new_name = info_for_name.get("name") or old_name

        # Track counts after logically (do not depend on file text)
        counts_after[new_cat] = counts_after.get(new_cat, 0) + 1

        if new_cat == current_cat and new_name == old_name:
            continue  # nothing to change in this file

        # From here on, we patch the original text surgically.
        text = yml.read_text(encoding="utf-8")
        lines = text.splitlines()

        meta_old = CATEGORY_META.get(current_cat, (current_cat, current_cat))
        old_short, old_display = meta_old
        meta_new = CATEGORY_META.get(new_cat, (new_cat, new_cat))
        new_short, new_display = meta_new

        def replace_scalar(line: str, key: str, old_val: str, new_val: str) -> str:
            """Replace YAML scalar value for a given key when it matches old_val.

            Preserves existing quoting style and leading whitespace.
            """
            m = re.match(rf"^(\s*{re.escape(key)}:\s*)(.*)$", line)
            if not m:
                return line
            prefix, value = m.groups()
            raw = value.strip()
            if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
                inner = raw[1:-1]
                quote = raw[0]
            else:
                inner = raw
                quote = ""
            if inner != old_val:
                return line
            if quote:
                return f"{prefix}{quote}{new_val}{quote}"
            return f"{prefix}{new_val}"

        new_lines = []
        for line in lines:
            orig = line
            if new_cat != current_cat:
                line = replace_scalar(line, "name", current_cat, new_cat)
                line = replace_scalar(line, "shortName", old_short, new_short)
                line = replace_scalar(line, "displayName", old_display, new_display)
            if new_name != old_name:
                line = replace_scalar(line, "name", old_name, new_name)
            new_lines.append(line)

        new_text = "\n".join(new_lines) + ("\n" if text.endswith("\n") else "")
        if new_text != text:
            try:
                yml.write_text(new_text, encoding="utf-8")
            except Exception as e:
                print(f"{yml.name}: write error {e}", file=sys.stderr)
            if new_cat != current_cat:
                changed_files += 1
            if new_name != old_name:
                renamed_names += 1

    print("Category counts BEFORE remap:")
    for k in sorted(counts_before):
        print(f"- {k}: {counts_before[k]}")

    print("\nCategory counts AFTER remap:")
    for k in sorted(counts_after):
        print(f"- {k}: {counts_after[k]}")

    print(f"\nYAML files with category changes: {changed_files}")
    print(f"Templates with name updated for cascades: {renamed_names}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

