#!/usr/bin/env python3
"""
Generate *_AGENTIC.{yml,yaml} copies of tests-library templates for agentic testing.

Criteria for inclusion:
- Execute steps only mutate query string or body via: modify_query_param, modify_body_param,
  add_query_param, add_body_param, replace_body (full body, e.g. JSON agent payloads),
  delete_body_param, delete_query_param.
- Still excluded: URL/method/header changes, SSRF harness steps, auth-header tricks, etc.
- api_selection_filters enforce POST only (top-level method eq POST; nested method keys removed).

Mixed-body agentic (body + other execute ops, e.g. replace_body + modify_url): see
`template_mixed_body_and_other_ops` and `scripts/generate_agentic_mixed_body.py`.

Per matching template:
- id -> {id}_AGENTIC
- info.category.name -> {name}_AGENTIC
- shortName and displayName unchanged

Skips are logged to scripts/agentic_template_skips.txt with one line per template.
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = Path(__file__).resolve().parent
SKIP_LOG = SCRIPTS_DIR / "agentic_template_skips.txt"

ALLOWED_OPS = {
    "modify_query_param",
    "modify_body_param",
    "add_query_param",
    "add_body_param",
    "replace_body",
    "delete_body_param",
    "delete_query_param",
}

DISALLOWED_OPS = {
    "modify_url",
    "modify_method",
    "modify_header",
    "add_header",
    "remove_auth_header",
    "replace_auth_header",
    "delete_header",
    "send_ssrf_req",
    "follow_redirect",
}

SKIP_KEYS = {"validate", "success", "failure"}


def _collect_ops_from_value(obj, found: set[str]) -> None:
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in ALLOWED_OPS:
                found.add(k)
            elif k in DISALLOWED_OPS:
                found.add(k)
            elif k in ("for_all", "for_one", "or", "and"):
                _collect_ops_from_value(v, found)
            else:
                _collect_ops_from_value(v, found)
    elif isinstance(obj, list):
        for x in obj:
            _collect_ops_from_value(x, found)


def collect_req_operations(req_steps: list | None) -> set[str]:
    """Collect operation keys from one `req:` list (first level + dynamic/for_all nesting)."""
    found: set[str] = set()
    if not isinstance(req_steps, list):
        return found
    for step in req_steps:
        if not isinstance(step, dict):
            continue
        for k, v in step.items():
            if k in SKIP_KEYS:
                continue
            if k in ALLOWED_OPS:
                found.add(k)
            elif k in DISALLOWED_OPS:
                found.add(k)
            else:
                _collect_ops_from_value(v, found)
    return found


def template_uses_only_allowed_ops(doc: dict) -> tuple[bool, str]:
    ex = doc.get("execute")
    if not isinstance(ex, dict):
        return False, "No execute block."
    requests = ex.get("requests")
    if not isinstance(requests, list) or not requests:
        return False, "No execute.requests."

    all_ops: set[str] = set()
    for block in requests:
        if not isinstance(block, dict) or "req" not in block:
            return False, "Malformed execute.requests entry (missing req)."
        all_ops |= collect_req_operations(block.get("req"))

    if not all_ops:
        return False, "No recognized query/body mutation operations in execute."

    bad = all_ops - ALLOWED_OPS
    if bad:
        return False, f"Uses non-query/body operations: {sorted(bad)}."

    return True, ""


# Body surface ops used for "mixed" agentic templates (body + other execute operations).
BODY_SURFACE_OPS = frozenset(
    {"modify_body_param", "add_body_param", "replace_body", "delete_body_param"}
)


def template_mixed_body_and_other_ops(doc: dict) -> tuple[bool, str]:
    """
    Eligible when the test both touches the request body and uses at least one disallowed
    (non–query-only) execute op — e.g. replace_body + modify_url, modify_body_param + add_header.
    Strict query/body-only templates use template_uses_only_allowed_ops instead.
    """
    ex = doc.get("execute")
    if not isinstance(ex, dict):
        return False, "No execute block."
    requests = ex.get("requests")
    if not isinstance(requests, list) or not requests:
        return False, "No execute.requests."

    all_ops: set[str] = set()
    for block in requests:
        if not isinstance(block, dict) or "req" not in block:
            return False, "Malformed execute.requests entry (missing req)."
        all_ops |= collect_req_operations(block.get("req"))

    if not all_ops:
        return False, "No recognized operations in execute."

    if not (all_ops & BODY_SURFACE_OPS):
        return False, "No body mutation (modify_body_param, add_body_param, replace_body, delete_body_param)."

    if not (all_ops & DISALLOWED_OPS):
        return False, "No additional operations beyond query/body-only; use strict agentic rule instead."

    return True, ""


def deep_strip_method_keys(obj):
    """Remove every `method` key at any depth (used under api_selection_filters)."""
    if isinstance(obj, dict):
        return {k: deep_strip_method_keys(v) for k, v in obj.items() if k != "method"}
    if isinstance(obj, list):
        return [deep_strip_method_keys(x) for x in obj]
    return obj


def enforce_post_only_filters(filters: dict | None) -> dict:
    if not isinstance(filters, dict):
        return {"method": {"eq": "POST"}}
    cleaned = deep_strip_method_keys(copy.deepcopy(filters))
    merged = {"method": {"eq": "POST"}}
    merged.update(cleaned)
    return merged


API_SELECTION_BANNED_CONTENT_KEYS = frozenset({"contains", "not_contains", "contains_either"})


def strip_api_selection_content_filters(filters: dict) -> dict:
    """Remove contains / not_contains / contains_either from api_selection_filters (agentic broadening)."""

    def strip(node):
        if isinstance(node, dict):
            out = {}
            for k, v in node.items():
                if k in API_SELECTION_BANNED_CONTENT_KEYS:
                    continue
                v = strip(v)
                if isinstance(v, dict) and not v:
                    continue
                if isinstance(v, list) and not v:
                    continue
                out[k] = v
            return out
        if isinstance(node, list):
            out = []
            for x in node:
                cx = strip(x)
                if isinstance(cx, dict) and not cx:
                    continue
                if cx is None:
                    continue
                out.append(cx)
            return out
        return node

    return strip(copy.deepcopy(filters))


def strip_modify_method_from_execute(doc: dict) -> None:
    """
    Remove modify_method from execute.requests (in-place). Agentic tests select POST APIs only;
    the replay must not switch HTTP method in execute.
    """

    def _drop(obj):
        if isinstance(obj, dict):
            return {k: _drop(v) for k, v in obj.items() if k != "modify_method"}
        if isinstance(obj, list):
            out = []
            for x in obj:
                cx = _drop(x)
                if isinstance(cx, dict) and not cx:
                    continue
                out.append(cx)
            return out
        return obj

    ex = doc.get("execute")
    if not isinstance(ex, dict):
        return
    requests = ex.get("requests")
    if not isinstance(requests, list):
        return
    for block in requests:
        if not isinstance(block, dict) or "req" not in block:
            continue
        req_steps = block.get("req")
        if isinstance(req_steps, list):
            block["req"] = _drop(req_steps)


def build_agentic_doc(src: dict) -> dict:
    out = copy.deepcopy(src)
    iid = out.get("id")
    if isinstance(iid, str) and not iid.endswith("_AGENTIC"):
        out["id"] = f"{iid}_AGENTIC"
    info = out.get("info")
    if isinstance(info, dict):
        cat = info.get("category")
        if isinstance(cat, dict):
            n = cat.get("name")
            if isinstance(n, str) and not n.endswith("_AGENTIC"):
                cat["name"] = f"{n}_AGENTIC"
    if "api_selection_filters" in out:
        out["api_selection_filters"] = strip_api_selection_content_filters(
            enforce_post_only_filters(out["api_selection_filters"])
        )
    strip_modify_method_from_execute(out)
    return out


def yaml_dump(doc: dict) -> str:
    return yaml.dump(
        doc,
        default_flow_style=False,
        sort_keys=False,
        allow_unicode=True,
        width=120,
    )


def iter_template_files():
    for ext in ("*.yml", "*.yaml"):
        for p in sorted(REPO_ROOT.rglob(ext)):
            if SCRIPTS_DIR in p.parents or "AI-Agent-tests" in p.parts:
                continue
            if p.name.startswith("."):
                continue
            if "_AGENTIC." in p.name:
                continue
            yield p


def main() -> int:
    generated = 0
    skips: list[tuple[str, str]] = []

    for path in iter_template_files():
        rel = path.relative_to(REPO_ROOT)
        try:
            text = path.read_text(encoding="utf-8")
            doc = yaml.safe_load(text)
        except Exception as e:
            skips.append((str(rel), f"YAML parse error: {e}"))
            continue
        if not isinstance(doc, dict):
            skips.append((str(rel), "Root document is not a mapping."))
            continue

        ok, reason = template_uses_only_allowed_ops(doc)
        if not ok:
            skips.append((str(rel), reason))
            continue

        out_doc = build_agentic_doc(doc)
        stem = path.stem
        out_name = f"{stem}_AGENTIC{path.suffix}"
        out_path = path.parent / out_name
        if out_path.exists():
            skips.append((str(rel), f"Target already exists: {out_path.name}"))
            continue

        try:
            out_path.write_text(yaml_dump(out_doc), encoding="utf-8")
            generated += 1
        except Exception as e:
            skips.append((str(rel), f"Write error: {e}"))

    lines = [f"{rel}\t{reason}" for rel, reason in sorted(skips)]
    SKIP_LOG.write_text(
        "\n".join(lines) + ("\n" if lines else ""),
        encoding="utf-8",
    )
    print(f"Generated {generated} agentic template(s).")
    print(f"Skipped {len(skips)} template(s); reasons in {SKIP_LOG.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
