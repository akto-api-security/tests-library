#!/usr/bin/env python3
"""
Generate *_AGENTIC templates from the union of templates on git branches, in order:

  master -> standard -> pro

For each relative path, the first branch that contains the file wins; later branches are
skipped for that path (deduplication log).

Reads file contents via `git show <branch>:<path>` so the working tree branch does not matter.

Outputs:
- Agentic YAML next to the logical path under REPO_ROOT (same layout as checkout).
- scripts/agentic_unified_dedup.txt — paths skipped as duplicates of an earlier branch.
- scripts/agentic_template_skips_unified.txt — templates not generated (parse errors, eligibility).

Reuses eligibility and transforms from generate_agentic_templates.py (query/body/replace_body/delete_* ops).

Inventory (git union of master + standard + pro, dedup by path, no *_AGENTIC):
- Total base templates in repo: 932.
- LLM-Security/: 55 and MCP-Security/: 5 (60 total) — typically omitted from the public API
  alongside other LLM/MCP surfaces; base templates outside those folders: 872.
- Dashboard “966 templates” vs git 932: the remaining ~34 is usually version/packaging skew
  (what the dashboard bundle includes), inactive flags, or counting rules — not fully derivable from git alone.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import yaml

from generate_agentic_templates import (
    REPO_ROOT,
    SCRIPTS_DIR,
    build_agentic_doc,
    template_uses_only_allowed_ops,
    yaml_dump,
)

DEFAULT_BRANCHES = ("master", "standard", "pro")

# Prefixes excluded from API-facing template lists (use --api-only when generating agentic for API parity).
API_EXCLUDE_PREFIXES: tuple[str, ...] = ("LLM-Security/", "MCP-Security/")

DEDUP_LOG = SCRIPTS_DIR / "agentic_unified_dedup.txt"
SKIP_LOG = SCRIPTS_DIR / "agentic_template_skips_unified.txt"


def _should_include_path(rel: str) -> bool:
    if not rel.endswith((".yml", ".yaml")):
        return False
    if "_AGENTIC" in rel:
        return False
    if rel.startswith("scripts/") or "/scripts/" in rel:
        return False
    if "AI-Agent-tests" in rel:
        return False
    return True


def list_paths_on_branch(repo: Path, branch: str) -> list[str]:
    r = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", branch],
        cwd=repo,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        raise RuntimeError(f"git ls-tree {branch}: {r.stderr}")
    return sorted(p for p in r.stdout.splitlines() if _should_include_path(p))


def git_show_file(repo: Path, branch: str, path: str) -> str | None:
    r = subprocess.run(
        ["git", "show", f"{branch}:{path}"],
        cwd=repo,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        return None
    return r.stdout


def merge_paths_in_order(
    repo: Path, branches: tuple[str, ...]
) -> tuple[dict[str, tuple[str, str]], list[tuple[str, str, str]]]:
    """
    Returns:
      path -> (source_branch, file_text)
      duplicates: list of (path, skipped_branch, kept_branch)
    """
    first: dict[str, tuple[str, str]] = {}
    dups: list[tuple[str, str, str]] = []

    for branch in branches:
        for rel in list_paths_on_branch(repo, branch):
            if rel in first:
                dups.append((rel, branch, first[rel][0]))
                continue
            text = git_show_file(repo, branch, rel)
            if text is None:
                continue
            first[rel] = (branch, text)
    return first, dups


def filter_by_prefixes(
    merged: dict[str, tuple[str, str]], exclude_prefixes: tuple[str, ...]
) -> dict[str, tuple[str, str]]:
    if not exclude_prefixes:
        return merged
    return {k: v for k, v in merged.items() if not any(k.startswith(p) for p in exclude_prefixes)}


def agentic_out_path(repo: Path, rel: str) -> Path:
    p = Path(rel)
    return repo / p.parent / f"{p.stem}_AGENTIC{p.suffix}"


def delete_existing_agentic(repo: Path) -> int:
    n = 0
    for ext in ("*.yml", "*.yaml"):
        for f in repo.rglob(ext):
            if SCRIPTS_DIR in f.parents or "AI-Agent-tests" in f.parts:
                continue
            if "_AGENTIC." in f.name:
                f.unlink()
                n += 1
    return n


def main() -> int:
    ap = argparse.ArgumentParser(description="Unified agentic template generation across branches.")
    ap.add_argument(
        "--branches",
        default=",".join(DEFAULT_BRANCHES),
        help=f"Comma-separated order (default: {','.join(DEFAULT_BRANCHES)})",
    )
    ap.add_argument(
        "--api-only",
        action="store_true",
        help=f"Exclude paths under {list(API_EXCLUDE_PREFIXES)} (LLM/MCP packs not shown in API).",
    )
    ap.add_argument(
        "--exclude-prefix",
        action="append",
        default=[],
        metavar="PREFIX",
        help="Additional path prefix to exclude (repeatable). Implies filtering merged templates.",
    )
    ap.add_argument(
        "--print-inventory",
        action="store_true",
        help="Print base-template counts from merged branches and exit (no YAML written).",
    )
    ap.add_argument(
        "--delete-existing-agentic",
        action="store_true",
        help="Remove all existing *_AGENTIC.yml/yaml under the repo before generating.",
    )
    args = ap.parse_args()
    branches = tuple(b.strip() for b in args.branches.split(",") if b.strip())
    if not branches:
        print("No branches given.", file=sys.stderr)
        return 1

    repo = REPO_ROOT
    merged, dups = merge_paths_in_order(repo, branches)

    exclude: tuple[str, ...] = tuple(args.exclude_prefix or [])
    if args.api_only:
        exclude = tuple({*API_EXCLUDE_PREFIXES, *exclude})
    merged_for_run = filter_by_prefixes(merged, exclude)

    if args.print_inventory:
        n_llm = sum(1 for p in merged if p.startswith("LLM-Security/"))
        n_mcp = sum(1 for p in merged if p.startswith("MCP-Security/"))
        print(f"Merged base templates (all): {len(merged)}")
        print(f"  LLM-Security/: {n_llm}")
        print(f"  MCP-Security/: {n_mcp}")
        print(f"  Excluding LLM+MCP folders: {len(merged) - n_llm - n_mcp}")
        if exclude:
            print(f"After exclude_prefixes {exclude!r}: {len(merged_for_run)}")
        return 0

    DEDUP_LOG.write_text(
        "\n".join(f"{p}\tskipped_from_{sb}\tkept_from_{kb}" for p, sb, kb in sorted(dups))
        + ("\n" if dups else ""),
        encoding="utf-8",
    )

    if args.delete_existing_agentic:
        removed = delete_existing_agentic(repo)
        print(f"Removed {removed} existing *_AGENTIC file(s).")

    generated = 0
    skips: list[tuple[str, str]] = []

    for rel in sorted(merged_for_run.keys()):
        branch, text = merged_for_run[rel]
        try:
            doc = yaml.safe_load(text)
        except Exception as e:
            skips.append((rel, f"YAML parse error: {e}"))
            continue
        if not isinstance(doc, dict):
            skips.append((rel, "Root document is not a mapping."))
            continue

        ok, reason = template_uses_only_allowed_ops(doc)
        if not ok:
            skips.append((rel, f"[{branch}] {reason}"))
            continue

        out_doc = build_agentic_doc(doc)
        out_path = agentic_out_path(repo, rel)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            out_path.write_text(yaml_dump(out_doc), encoding="utf-8")
            generated += 1
        except Exception as e:
            skips.append((rel, f"Write error: {e}"))

    SKIP_LOG.write_text(
        "\n".join(f"{rel}\t{reason}" for rel, reason in sorted(skips))
        + ("\n" if skips else ""),
        encoding="utf-8",
    )

    print(f"Branches (order): {', '.join(branches)}")
    print(f"Unique template paths after merge: {len(merged)}")
    if exclude:
        print(f"Excluded prefixes {list(exclude)} -> generating from {len(merged_for_run)} base template(s)")
    print(f"Duplicate paths skipped (later branch): {len(dups)}  -> {DEDUP_LOG.relative_to(repo)}")
    print(f"Generated agentic templates: {generated}")
    print(f"Skipped (parse / eligibility / write): {len(skips)}  -> {SKIP_LOG.relative_to(repo)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
