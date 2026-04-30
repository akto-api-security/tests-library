#!/usr/bin/env python3
"""
Refresh OWASP Agentic generated_tests/*.yml:
- Sync category from subCategory prefix rules (agentic_category_mapping.txt).
- Set CWE/CVE from AI-Agent-tests/agentic_cwe_cve_mapping.json (after JSON update).
- Replace boilerplate one-line details; normalize description (fix double periods).

Run from repo root: python3 scripts/enrich_agentic_generated_tests.py
"""
from __future__ import annotations

import json
from pathlib import Path

from ruamel.yaml import YAML


REPO_ROOT = Path(__file__).resolve().parents[1]
GEN_DIR = REPO_ROOT / "AI-Agent-tests" / "generated_tests"
MAP_PATH = REPO_ROOT / "AI-Agent-tests" / "agentic_cwe_cve_mapping.json"

# Prefix -> OWASP Agentic category (longest match wins). Mirrors agentic_category_mapping.txt.
PREFIX_TO_CATEGORY: dict[str, str] = {
    "BUSINESS_ALIGNMENT_COMPETITOR_CHECK_": "AGENT_GOAL_HIJACK",
    "BUSINESS_ALIGNMENT_HUMAN_AGENT_TRUST_EXPLOITATION_": "HUMAN_AGENT_TRUST_EXPLOITATION",
    "BUSINESS_ALIGNMENT_INTENTIONAL_MISUSE_": "TOOL_MISUSE_AND_EXPLOITATION",
    "BUSINESS_ALIGNMENT_LEGALLY_BINDING_": "HUMAN_AGENT_TRUST_EXPLOITATION",
    "BUSINESS_ALIGNMENT_MISALIGNED_AND_DECEPTIVE_BEHAVIORS_": "AGENT_GOAL_HIJACK",
    "BUSINESS_ALIGNMENT_OFF_TOPIC_": "AGENT_GOAL_HIJACK",
    "BUSINESS_ALIGNMENT_OVERWHELMING_HUMAN_IN_THE_LOOP_": "HUMAN_AGENT_TRUST_EXPLOITATION",
    "BUSINESS_ALIGNMENT_ROGUE_AGENTS_": "ROGUE_AGENTS",
    "HALLUCINATION_AND_TRUSTWORTHINESS_RAG_PRECISION_": "MEMORY_AND_CONTEXT_POISONING",
    "HALLUCINATION_AND_TRUSTWORTHINESS_CITATION_AND_SOURCE_VERIFICATION_": "MEMORY_AND_CONTEXT_POISONING",
    "HALLUCINATION_AND_TRUSTWORTHINESS_CONFIDENCE_CALIBRATION_": "MEMORY_AND_CONTEXT_POISONING",
    "HALLUCINATION_AND_TRUSTWORTHINESS_FACTUAL_ACCURACY_BENCHMARKING_": "MEMORY_AND_CONTEXT_POISONING",
    "HALLUCINATION_AND_TRUSTWORTHINESS_HALLUCINATION_PROPAGATION_": "CASCADING_FAILURES",
    "HALLUCINATION_AND_TRUSTWORTHINESS_KNOWLEDGE_CUTOFF_BOUNDARY_TESTING_": "MEMORY_AND_CONTEXT_POISONING",
    "HALLUCINATION_AND_TRUSTWORTHINESS_PARANOID_PROTECTION_": "MEMORY_AND_CONTEXT_POISONING",
    "HALLUCINATION_AND_TRUSTWORTHINESS_Q_A_": "MEMORY_AND_CONTEXT_POISONING",
    "HALLUCINATION_AND_TRUSTWORTHINESS_URL_CHECK_": "MEMORY_AND_CONTEXT_POISONING",
    "SAFETY_AUTOMATED_BIAS_TESTING_": "AGENT_GOAL_HIJACK",
    "SAFETY_BIAS_": "AGENT_GOAL_HIJACK",
    "SAFETY_BOUNDARY_TESTING_": "AGENT_GOAL_HIJACK",
    "SAFETY_CONTENT_GENERATION_VS_INFORMATION_PROVISION_": "AGENT_GOAL_HIJACK",
    "SAFETY_CULTURAL_REPRESENTATION_TESTING_": "AGENT_GOAL_HIJACK",
    "SAFETY_FAIRNESS_METRIC_GENERATION_": "AGENT_GOAL_HIJACK",
    "SAFETY_FEW_SHOT_LEARNING_EXPLOITATION_": "MEMORY_AND_CONTEXT_POISONING",
    "SAFETY_HARMFUL_CONTENT_GENERATION_NIST_AI_RMF_": "AGENT_GOAL_HIJACK",
    "SAFETY_HARMFUL_CONTENT_": "AGENT_GOAL_HIJACK",
    "SAFETY_ILLEGAL_ACTIVITIES_": "AGENT_GOAL_HIJACK",
    "SAFETY_PII_": "IDENTITY_AND_PRIVILEGE_ABUSE",
    "SAFETY_PRIVACY_VIOLATION_": "IDENTITY_AND_PRIVILEGE_ABUSE",
    "SAFETY_PROFANITY_": "AGENT_GOAL_HIJACK",
    "SAFETY_REFUSAL_MECHANISM_VALIDATION_": "AGENT_GOAL_HIJACK",
    "SAFETY_STEREOTYPE_REINFORCEMENT_DETECTION_": "AGENT_GOAL_HIJACK",
    "SAFETY_TOOL_AND_FUNCTION_CALLING_MANIPULATION_": "TOOL_MISUSE_AND_EXPLOITATION",
    "SECURITY_ADVERSARIAL_SUFFIX_ATTACK_": "AGENT_GOAL_HIJACK",
    "SECURITY_AGENT_BEHAVIOR_HIJACK_AND_GOAL_MANIPULATION_": "AGENT_GOAL_HIJACK",
    "SECURITY_AGENTIC_SUPPLY_CHAIN_VULNERABILITIES_": "AGENTIC_SUPPLY_CHAIN",
    "SECURITY_API_CREDENTIAL_AND_CONFIGURATION_EXPOSURE_": "IDENTITY_AND_PRIVILEGE_ABUSE",
    "SECURITY_CANARY_TOKEN_DETECTION_": "MEMORY_AND_CONTEXT_POISONING",
    "SECURITY_CODE_EXECUTION_": "UNEXPECTED_CODE_EXECUTION",
    "SECURITY_CONTEXT_LEAKAGE_": "IDENTITY_AND_PRIVILEGE_ABUSE",
    "SECURITY_CONTEXT_POISONING_": "MEMORY_AND_CONTEXT_POISONING",
    "SECURITY_CROSS_SESSION_LEAKS_": "MEMORY_AND_CONTEXT_POISONING",
    "SECURITY_CROSS_USER_DATA_BLEEDING_": "MEMORY_AND_CONTEXT_POISONING",
    "SECURITY_DATA_EXFILTRATION_": "IDENTITY_AND_PRIVILEGE_ABUSE",
    "SECURITY_DOCUMENT_BASED_INDIRECT_PROMPT_INJECTION_": "AGENT_GOAL_HIJACK",
    "SECURITY_EXCESSIVE_AGENCY_": "TOOL_MISUSE_AND_EXPLOITATION",
    "SECURITY_IDENTITY_SPOOFING_": "IDENTITY_AND_PRIVILEGE_ABUSE",
    "SECURITY_INDIRECT_PROMPT_INJECTION_": "AGENT_GOAL_HIJACK",
    "SECURITY_INSECURE_INTER_AGENT_COMMUNICATION_": "INSECURE_INTER_AGENT_COMMUNICATION",
    "SECURITY_INSECURE_PLUGIN_USE_": "TOOL_MISUSE_AND_EXPLOITATION",
    "SECURITY_INSTRUCTION_HIERARCHY_ATTACK_": "AGENT_GOAL_HIJACK",
    "SECURITY_JAILBREAK_": "AGENT_GOAL_HIJACK",
    "SECURITY_MALICIOUS_RESOURCE_FETCHING_": "TOOL_MISUSE_AND_EXPLOITATION",
    "SECURITY_MANIPULATION_": "AGENT_GOAL_HIJACK",
    "SECURITY_MODEL_DENIAL_OF_SERVICE_": "CASCADING_FAILURES",
    "SECURITY_MODEL_THEFT_": "AGENTIC_SUPPLY_CHAIN",
    "SECURITY_MULTI_TURN_JAILBREAK_SEQUENCES_": "AGENT_GOAL_HIJACK",
    "SECURITY_OVERRELIANCE_": "HUMAN_AGENT_TRUST_EXPLOITATION",
    "SECURITY_PHISHING_": "HUMAN_AGENT_TRUST_EXPLOITATION",
    "SECURITY_PROMPT_INJECTION_": "AGENT_GOAL_HIJACK",
    "SECURITY_RAG_POISONING_": "MEMORY_AND_CONTEXT_POISONING",
    "SECURITY_REPUDIATION_UNTRACEABILITY_": "ROGUE_AGENTS",
    "SECURITY_SENSITIVE_INFORMATION_DISCLOSURE_": "IDENTITY_AND_PRIVILEGE_ABUSE",
    "SECURITY_SINGLE_TURN_DIRECT_PROMPT_INJECTION_": "AGENT_GOAL_HIJACK",
    "SECURITY_SYSTEM_PROMPT_AND_TEMPLATE_EXTRACTION_": "AGENT_GOAL_HIJACK",
    "SECURITY_SYSTEM_PROMPT_OVERRIDE_": "AGENT_GOAL_HIJACK",
    "SECURITY_TOKEN_LEVEL_PERTURBATIONS_": "AGENT_GOAL_HIJACK",
    "SECURITY_TOOL_DISCOVERY_": "TOOL_MISUSE_AND_EXPLOITATION",
    "SECURITY_TOOL_MISUSE_AND_EXPLOITATION_": "TOOL_MISUSE_AND_EXPLOITATION",
    "SECURITY_TRAINING_DATA_POISONING_": "AGENTIC_SUPPLY_CHAIN",
    "SECURITY_UNEXPECTED_CODE_EXECUTION_RCE_": "UNEXPECTED_CODE_EXECUTION",
    "SECURITY_UNICODE_AND_HOMOGLYPH_ATTACKS_": "AGENT_GOAL_HIJACK",
    "SECURITY_WEB_INJECTION_": "TOOL_MISUSE_AND_EXPLOITATION",
    "SECURITY_XSS_": "UNEXPECTED_CODE_EXECUTION",
}

SORTED_PREFIXES = sorted(PREFIX_TO_CATEGORY.keys(), key=len, reverse=True)


# Family + per-template overrides used to live here as Python literals.
# They have moved to AI-Agent-tests/agentic_cwe_cve_mapping.json under the
# "by_family" and "by_template" keys, so the JSON is now the single source of
# truth. The dicts below are kept only as fallback defaults in case the JSON
# omits those sections, and are otherwise unused.
#
# Resolution order (lowest -> highest priority):
#   1. PREFIX_TO_CATEGORY + agentic_cwe_cve_mapping.json `by_category`
#   2. agentic_cwe_cve_mapping.json `by_family` (longest-prefix wins)
#   3. agentic_cwe_cve_mapping.json `by_template`
_FAMILY_OVERRIDES_FALLBACK: dict[str, dict[str, object]] = {
    # ---- IDENTITY / PRIVILEGE: use info-disclosure CWEs, not auth CWEs ----
    "SECURITY_DATA_EXFILTRATION_": {
        "category": "IDENTITY_AND_PRIVILEGE_ABUSE",
        "cwe": ["CWE-200", "CWE-359", "CWE-285"],
        "cve": [],
    },
    "SECURITY_SENSITIVE_INFORMATION_DISCLOSURE_": {
        "category": "IDENTITY_AND_PRIVILEGE_ABUSE",
        "cwe": ["CWE-200", "CWE-359", "CWE-922"],
        "cve": [],
    },
    "SECURITY_API_CREDENTIAL_AND_CONFIGURATION_EXPOSURE_": {
        "category": "IDENTITY_AND_PRIVILEGE_ABUSE",
        "cwe": ["CWE-522", "CWE-200", "CWE-732"],
        "cve": [],
    },
    "SECURITY_CONTEXT_LEAKAGE_": {
        "category": "IDENTITY_AND_PRIVILEGE_ABUSE",
        "cwe": ["CWE-200", "CWE-359", "CWE-285"],
        "cve": [],
    },
    "SAFETY_PII_": {
        "category": "IDENTITY_AND_PRIVILEGE_ABUSE",
        "cwe": ["CWE-359", "CWE-200", "CWE-285"],
        "cve": [],
    },
    "SAFETY_PRIVACY_VIOLATION_": {
        "category": "IDENTITY_AND_PRIVILEGE_ABUSE",
        "cwe": ["CWE-359", "CWE-200", "CWE-285"],
        "cve": [],
    },
    "SECURITY_CROSS_SESSION_LEAKS_": {
        "category": "IDENTITY_AND_PRIVILEGE_ABUSE",
        "cwe": ["CWE-200", "CWE-285", "CWE-359"],
        "cve": [],
    },
    "SECURITY_CROSS_USER_DATA_BLEEDING_": {
        "category": "IDENTITY_AND_PRIVILEGE_ABUSE",
        "cwe": ["CWE-200", "CWE-285", "CWE-359"],
        "cve": [],
    },

    # ---- TOOL MISUSE: pick CWE that matches the actual mechanism ----
    "SECURITY_MALICIOUS_RESOURCE_FETCHING_": {
        "category": "TOOL_MISUSE_AND_EXPLOITATION",
        "cwe": ["CWE-918", "CWE-601", "CWE-94"],
        "cve": [],
    },
    "SECURITY_WEB_INJECTION_": {
        "category": "TOOL_MISUSE_AND_EXPLOITATION",
        "cwe": ["CWE-89", "CWE-79", "CWE-78", "CWE-94"],
        "cve": [],
    },
    "SECURITY_EXCESSIVE_AGENCY_": {
        "category": "TOOL_MISUSE_AND_EXPLOITATION",
        "cwe": ["CWE-269", "CWE-862", "CWE-732"],
        "cve": [],
    },
    "SECURITY_TOOL_DISCOVERY_": {
        "category": "TOOL_MISUSE_AND_EXPLOITATION",
        "cwe": ["CWE-200", "CWE-497", "CWE-749"],
        "cve": [],
    },

    # ---- ROGUE / ACCOUNTABILITY ----
    "SECURITY_REPUDIATION_UNTRACEABILITY_": {
        "category": "ROGUE_AGENTS",
        "cwe": ["CWE-778", "CWE-223", "CWE-117"],
        "cve": [],
    },

    # ---- SUPPLY CHAIN: model theft is exfiltration of model assets ----
    "SECURITY_MODEL_THEFT_": {
        "category": "AGENTIC_SUPPLY_CHAIN",
        "cwe": ["CWE-200", "CWE-1059", "CWE-285"],
        "cve": [],
    },

    # ---- SAFETY: bias / fairness families don't fit CWE-94 ----
    "SAFETY_BIAS_": {
        "category": "AGENT_GOAL_HIJACK",
        "cwe": ["CWE-1039", "CWE-693"],
        "cve": [],
    },
    "SAFETY_AUTOMATED_BIAS_TESTING_": {
        "category": "AGENT_GOAL_HIJACK",
        "cwe": ["CWE-1039", "CWE-693"],
        "cve": [],
    },
    "SAFETY_STEREOTYPE_REINFORCEMENT_DETECTION_": {
        "category": "AGENT_GOAL_HIJACK",
        "cwe": ["CWE-1039", "CWE-693"],
        "cve": [],
    },
    "SAFETY_FAIRNESS_METRIC_GENERATION_": {
        "category": "AGENT_GOAL_HIJACK",
        "cwe": ["CWE-1039", "CWE-693"],
        "cve": [],
    },
    "SAFETY_CULTURAL_REPRESENTATION_TESTING_": {
        "category": "AGENT_GOAL_HIJACK",
        "cwe": ["CWE-1039", "CWE-693"],
        "cve": [],
    },

    # ---- SAFETY harmful-content families ----
    "SAFETY_HARMFUL_CONTENT_": {
        "category": "AGENT_GOAL_HIJACK",
        "cwe": ["CWE-74", "CWE-693"],
        "cve": [],
    },
    "SAFETY_HARMFUL_CONTENT_GENERATION_NIST_AI_RMF_": {
        "category": "AGENT_GOAL_HIJACK",
        "cwe": ["CWE-74", "CWE-693"],
        "cve": [],
    },
    "SAFETY_ILLEGAL_ACTIVITIES_": {
        "category": "AGENT_GOAL_HIJACK",
        "cwe": ["CWE-74", "CWE-693"],
        "cve": [],
    },
    "SAFETY_BOUNDARY_TESTING_": {
        "category": "AGENT_GOAL_HIJACK",
        "cwe": ["CWE-74", "CWE-693"],
        "cve": [],
    },
    "SAFETY_CONTENT_GENERATION_VS_INFORMATION_PROVISION_": {
        "category": "AGENT_GOAL_HIJACK",
        "cwe": ["CWE-74", "CWE-693"],
        "cve": [],
    },
    "SAFETY_REFUSAL_MECHANISM_VALIDATION_": {
        "category": "AGENT_GOAL_HIJACK",
        "cwe": ["CWE-693", "CWE-74"],
        "cve": [],
    },
    "SAFETY_PROFANITY_": {
        "category": "AGENT_GOAL_HIJACK",
        "cwe": ["CWE-74", "CWE-915", "CWE-20"],
        "cve": [],
    },
}

# Per-template overrides used to live here as Python literals; they have moved
# to AI-Agent-tests/agentic_cwe_cve_mapping.json under "by_template". The dict
# below is kept only as fallback defaults if the JSON omits that section.
_TEMPLATE_OVERRIDES_FALLBACK: dict[str, dict[str, object]] = {
    "SECURITY_XSS_MATH_PROBLEM": {
        "category": "UNEXPECTED_CODE_EXECUTION",
        "cwe": ["CWE-79", "CWE-83", "CWE-94"],
        "cve": ["CVE-2019-0221"],
    },
    "SECURITY_XSS_LEETSPEAK": {
        "category": "UNEXPECTED_CODE_EXECUTION",
        "cwe": ["CWE-79", "CWE-83"],
        "cve": ["CVE-2019-0221"],
    },
    "SECURITY_CROSS_SESSION_LEAKS_SEMANTIC_MANIPULATION": {
        "category": "IDENTITY_AND_PRIVILEGE_ABUSE",
        "cwe": ["CWE-200", "CWE-285", "CWE-359"],
        "cve": [],
    },
    "HALLUCINATION_AND_TRUSTWORTHINESS_PARANOID_PROTECTION_INPUT_BYPASS": {
        "category": "MEMORY_AND_CONTEXT_POISONING",
        "cwe": ["CWE-20", "CWE-74", "CWE-693"],
        "cve": [],
    },
    "SECURITY_REPUDIATION_UNTRACEABILITY_PROMPT_INJECTION": {
        "category": "ROGUE_AGENTS",
        "cwe": ["CWE-778", "CWE-223", "CWE-74"],
        "cve": ["CVE-2024-5184"],
    },
    "SECURITY_REPUDIATION_UNTRACEABILITY_PERMISSION_ESCALATION": {
        "category": "ROGUE_AGENTS",
        "cwe": ["CWE-778", "CWE-269", "CWE-862"],
        "cve": [],
    },
    "SECURITY_REPUDIATION_UNTRACEABILITY_MULTILINGUAL": {
        "category": "ROGUE_AGENTS",
        "cwe": ["CWE-778", "CWE-223", "CWE-20"],
        "cve": [],
    },
    "SECURITY_WEB_INJECTION_CONTEXT_POISONING": {
        "category": "TOOL_MISUSE_AND_EXPLOITATION",
        "cwe": ["CWE-89", "CWE-79", "CWE-78", "CWE-94"],
        "cve": [],
    },
    "SECURITY_TOOL_DISCOVERY_SEMANTIC_MANIPULATION": {
        "category": "TOOL_MISUSE_AND_EXPLOITATION",
        "cwe": ["CWE-200", "CWE-497", "CWE-749"],
        "cve": [],
    },
    "SECURITY_TOOL_DISCOVERY_SYSTEM_OVERRIDE": {
        "category": "TOOL_MISUSE_AND_EXPLOITATION",
        "cwe": ["CWE-200", "CWE-497", "CWE-749"],
        "cve": [],
    },
    "SECURITY_TOOL_DISCOVERY_GOAL_REDIRECTION": {
        "category": "TOOL_MISUSE_AND_EXPLOITATION",
        "cwe": ["CWE-200", "CWE-497", "CWE-749"],
        "cve": [],
    },
    "SECURITY_TOOL_DISCOVERY_MULTILINGUAL": {
        "category": "TOOL_MISUSE_AND_EXPLOITATION",
        "cwe": ["CWE-200", "CWE-497", "CWE-749"],
        "cve": [],
    },
    "SECURITY_TOOL_DISCOVERY_CONTEXT_POISONING": {
        "category": "TOOL_MISUSE_AND_EXPLOITATION",
        "cwe": ["CWE-200", "CWE-497", "CWE-749"],
        "cve": [],
    },
    "SAFETY_PROFANITY_CONTEXT_POISONING": {
        "category": "AGENT_GOAL_HIJACK",
        "cwe": ["CWE-74", "CWE-915", "CWE-20"],
        "cve": [],
    },
    "BUSINESS_ALIGNMENT_COMPETITOR_CHECK_INPUT_BYPASS": {
        "category": "AGENT_GOAL_HIJACK",
        "cwe": ["CWE-74", "CWE-20"],
        "cve": ["CVE-2024-5184"],
    },
}

DISPLAY_NAME = {
    "AGENT_GOAL_HIJACK": "Agent Goal Hijack",
    "HUMAN_AGENT_TRUST_EXPLOITATION": "Human-Agent Trust Exploitation",
    "MEMORY_AND_CONTEXT_POISONING": "Memory and Context Poisoning",
    "TOOL_MISUSE_AND_EXPLOITATION": "Tool Misuse and Exploitation",
    "IDENTITY_AND_PRIVILEGE_ABUSE": "Identity and Privilege Abuse",
    "ROGUE_AGENTS": "Rogue Agents",
    "AGENTIC_SUPPLY_CHAIN": "Agentic Supply Chain",
    "CASCADING_FAILURES": "Cascading Failures",
    "INSECURE_INTER_AGENT_COMMUNICATION": "Insecure Inter-Agent Communication",
    "UNEXPECTED_CODE_EXECUTION": "Unexpected Code Execution",
}


def _load_overrides_from_json() -> tuple[dict[str, dict[str, object]], dict[str, dict[str, object]]]:
    """Read by_family / by_template from the mapping JSON and fall back to the
    in-script literals when those sections are missing or unreadable."""
    try:
        with open(MAP_PATH, encoding="utf-8") as f:
            raw = json.load(f)
    except FileNotFoundError:
        return dict(_FAMILY_OVERRIDES_FALLBACK), dict(_TEMPLATE_OVERRIDES_FALLBACK)
    fam = raw.get("by_family") or _FAMILY_OVERRIDES_FALLBACK
    tpl = raw.get("by_template") or _TEMPLATE_OVERRIDES_FALLBACK
    return dict(fam), dict(tpl)


FAMILY_OVERRIDES, TEMPLATE_OVERRIDES = _load_overrides_from_json()
FAMILY_OVERRIDE_PREFIXES = sorted(FAMILY_OVERRIDES.keys(), key=len, reverse=True)


def family_override(sub_category: str) -> dict[str, object] | None:
    for prefix in FAMILY_OVERRIDE_PREFIXES:
        if sub_category.startswith(prefix):
            return FAMILY_OVERRIDES[prefix]
    return None


def category_from_subcategory(sub: str) -> str | None:
    for prefix in SORTED_PREFIXES:
        if sub.startswith(prefix):
            return PREFIX_TO_CATEGORY[prefix]
    return None


def is_xss_variant(tid: str, sub: str) -> bool:
    return "SECURITY_XSS" in tid or "SECURITY_XSS" in sub


def unwrap_item(x) -> str:
    if x is None:
        return ""
    s = str(x).strip()
    if len(s) >= 2 and s[0] == s[-1] == '"':
        return s[1:-1].strip()
    return s


def normalize_periods(text: str) -> str:
    t = " ".join(text.split())
    while ".." in t:
        t = t.replace("..", ".")
    return t.strip()


def build_rich_details(
    *,
    display_name: str,
    sub_category: str,
    base_prompt: str,
    strategy: str,
) -> str:
    return normalize_periods(
        "This test measures how the agent behaves under the OWASP Agentic risk category "
        f"{display_name} (template {sub_category}). "
        "It combines a concrete misuse objective with a jailbreak or obfuscation strategy from the word lists. "
        f"Objective / base scenario: {base_prompt} "
        f"Offensive technique / strategy: {strategy} "
        "The exercise is non-intrusive: it sends policy-stressing prompts and evaluates whether safeguards resist "
        "the paired objective and technique (e.g. leakage, tool abuse, instruction override, or unsafe content)."
    )


def build_description(*, name: str, base_prompt: str, strategy: str) -> str:
    return normalize_periods(
        f"{name} Objective: {base_prompt} Applied technique: {strategy}"
    )


def load_mapping() -> tuple[dict, dict]:
    with open(MAP_PATH, encoding="utf-8") as f:
        raw = json.load(f)
    by_cat = raw.get("by_category") or {}
    uce = raw.get("unexpected_code_execution") or {}
    return by_cat, uce


def _resolve_default_block(
    *, cat: str, sub: str, tid: str, by_cat: dict, uce: dict
) -> dict:
    if cat == "UNEXPECTED_CODE_EXECUTION":
        if is_xss_variant(tid, sub):
            return uce.get("SECURITY_XSS") or {}
        return uce.get("CODE_EXECUTION_OR_RCE") or {}
    return by_cat.get(cat) or {}


VALID_SEVERITIES = ("CRITICAL", "HIGH", "MEDIUM", "LOW")


def main() -> None:
    by_cat, uce = load_mapping()
    yl = YAML()
    yl.preserve_quotes = True
    yl.default_flow_style = False
    yl.allow_unicode = True
    yl.width = 4096
    yl.indent(mapping=2, sequence=4, offset=2)
    yl.explicit_start = True

    stats = {
        "files": 0,
        "category_fixed": 0,
        "cwe_cve_fixed": 0,
        "severity_fixed": 0,
        "details_rewritten": 0,
        "desc_rewritten": 0,
    }

    for path in sorted(GEN_DIR.glob("*.yml")):
        stats["files"] += 1
        with open(path, encoding="utf-8") as f:
            data = yl.load(f)
        if not isinstance(data, dict):
            continue

        info = data.setdefault("info", {})
        sub = str(info.get("subCategory") or "")
        tid = str(data.get("id") or path.stem)

        # 1) Resolve OWASP Agentic category from subCategory prefix rules.
        exp_cat = category_from_subcategory(sub)
        if exp_cat is None:
            raise SystemExit(f"No prefix rule for subCategory: {sub!r} in {path}")

        # 2) Pull defaults (CWE/CVE/severity) from by_category or
        # unexpected_code_execution branch in the JSON.
        default_block = _resolve_default_block(
            cat=exp_cat, sub=sub, tid=tid, by_cat=by_cat, uce=uce
        )
        exp_cwe = list(default_block.get("cwe") or [])
        exp_cve = list(default_block.get("cve") or [])
        exp_sev = str(default_block.get("severity") or "").upper()

        if not exp_cwe:
            raise SystemExit(f"Missing CWE mapping for category {exp_cat} ({path})")

        # 3) Apply family-level overrides per-field.
        fam_ov = family_override(sub) or {}
        if "category" in fam_ov:
            exp_cat = str(fam_ov["category"])
            # Re-resolve the default block if the family override moved the
            # OWASP category, so severity/cwe/cve fall back to the new
            # category's defaults when the family entry omits them.
            default_block = _resolve_default_block(
                cat=exp_cat, sub=sub, tid=tid, by_cat=by_cat, uce=uce
            )
            if not fam_ov.get("cwe"):
                exp_cwe = list(default_block.get("cwe") or exp_cwe)
            if not fam_ov.get("cve") and "cve" not in fam_ov:
                exp_cve = list(default_block.get("cve") or exp_cve)
            if not fam_ov.get("severity"):
                exp_sev = (
                    str(default_block.get("severity") or "").upper() or exp_sev
                )
        if "cwe" in fam_ov:
            exp_cwe = list(fam_ov["cwe"])  # type: ignore[arg-type]
        if "cve" in fam_ov:
            exp_cve = list(fam_ov["cve"])  # type: ignore[arg-type]
        if "severity" in fam_ov:
            exp_sev = str(fam_ov["severity"]).upper()

        # 4) Apply per-template overrides per-field (highest priority).
        override = TEMPLATE_OVERRIDES.get(tid) or {}
        if "category" in override:
            exp_cat = str(override["category"])
        if "cwe" in override:
            exp_cwe = list(override["cwe"])  # type: ignore[arg-type]
        if "cve" in override:
            exp_cve = list(override["cve"])  # type: ignore[arg-type]
        if "severity" in override:
            exp_sev = str(override["severity"]).upper()

        if exp_sev and exp_sev not in VALID_SEVERITIES:
            raise SystemExit(
                f"Invalid severity {exp_sev!r} resolved for {tid} ({path})"
            )

        cat_block = info.setdefault("category", {})
        old_cat = cat_block.get("name")
        if old_cat != exp_cat:
            stats["category_fixed"] += 1
        cat_block["name"] = exp_cat
        cat_block["shortName"] = exp_cat
        cat_block["displayName"] = DISPLAY_NAME.get(
            exp_cat, exp_cat.replace("_", " ").title()
        )

        old_cwe, old_cve = info.get("cwe"), info.get("cve")
        if list(old_cwe or []) != exp_cwe or list(old_cve or []) != exp_cve:
            stats["cwe_cve_fixed"] += 1
        info["cwe"] = exp_cwe
        info["cve"] = exp_cve

        if exp_sev:
            old_sev = str(info.get("severity") or "").upper()
            if old_sev != exp_sev:
                stats["severity_fixed"] += 1
            info["severity"] = exp_sev

        wl = data.get("wordLists") or {}
        bp_list = wl.get("base_prompt") or []
        st_list = wl.get("strategy") or []
        bp0 = unwrap_item(bp_list[0]) if bp_list else ""
        st0 = unwrap_item(st_list[0]) if st_list else ""

        details = str(info.get("details") or "")
        new_display = cat_block["displayName"]

        was_initial_boilerplate = details.startswith("This test combines") and (
            " with the strategy: " in details
        )
        is_rich_boilerplate = details.startswith(
            "This test measures how the agent behaves under the OWASP Agentic risk category"
        )
        # If the previous run baked the rich paragraph but the OWASP category we
        # now resolve has a different displayName, the paragraph is stale.
        category_drifted = is_rich_boilerplate and (
            f" risk category {new_display} " not in details
        )

        if was_initial_boilerplate or category_drifted:
            info["details"] = build_rich_details(
                display_name=new_display,
                sub_category=sub,
                base_prompt=bp0,
                strategy=st0,
            )
            stats["details_rewritten"] += 1
            title = str(info.get("name") or "").strip() or path.stem.replace("_", " ")
            info["description"] = build_description(
                name=title, base_prompt=bp0, strategy=st0
            )
            stats["desc_rewritten"] += 1
        else:
            desc = str(info.get("description") or "")
            if ".." in desc:
                info["description"] = normalize_periods(desc)

        with open(path, "w", encoding="utf-8") as f:
            yl.dump(data, f)

    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
