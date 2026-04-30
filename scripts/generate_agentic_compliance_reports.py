#!/usr/bin/env python3
"""Generate concise compliance/<test_id>.conf for agentic tests."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
GEN_TESTS = REPO_ROOT / "AI-Agent-tests" / "generated_tests"
COMPLIANCE = REPO_ROOT / "compliance"

OWASP_AGENTIC_ASI_BY_SHORTNAME: dict[str, str] = {
    "AGENT_GOAL_HIJACK": "ASI01: Agent Goal Hijack",
    "TOOL_MISUSE_AND_EXPLOITATION": "ASI02: Tool Misuse and Exploitation",
    "IDENTITY_AND_PRIVILEGE_ABUSE": "ASI03: Identity and Privilege Abuse",
    "AGENTIC_SUPPLY_CHAIN": "ASI04: Agentic Supply Chain Vulnerabilities",
    "UNEXPECTED_CODE_EXECUTION": "ASI05: Unexpected Code Execution",
    "MEMORY_AND_CONTEXT_POISONING": "ASI06: Memory and Context Poisoning",
    "INSECURE_INTER_AGENT_COMMUNICATION": "ASI07: Insecure Inter-Agent Communication",
    "CASCADING_FAILURES": "ASI08: Cascading Failures",
    "HUMAN_AGENT_TRUST_EXPLOITATION": "ASI09: Human-Agent Trust Exploitation",
    "ROGUE_AGENTS": "ASI10: Rogue Agents",
}

# Fallback when info.category.shortName is missing or unknown.
DEFAULT_CONTROLS: dict[str, list[str]] = {
    "SOC 2": ["CC6.1", "CC7.2", "CC9.2"],
    "ISO 27001": ["A.5.15", "A.8.28"],
    "NIST 800-53": ["AC-3", "SI-4", "SA-15"],
    "CSA CCM": ["AIS-01", "IAM-01"],
    "CIS Controls": ["IG1 Safeguard 4.2", "IG1 Safeguard 16.8"],
    "FedRAMP": ["AC-3", "SI-4", "SC-7"],
    "NIST 800-171": ["3.1.1", "3.14.3"],
    "FISMA": ["AC-3", "SI-4"],
    "Cybersecurity Maturity Model Certification (CMMC)": ["AC.2.007", "SI.2.216"],
    "OWASP Agentic Top 10": ["ASI: baseline"],
    "EU AI Act": ["Art. 9", "Art. 13", "Art. 15", "Art. 25"],
    "NIST AI Risk Management Framework": ["Govern", "Map", "Measure", "Manage"],
    "MITRE ATLAS": [],
}

# Full row per OWASP Agentic category (info.category.shortName). Concise IDs only.
MATRIX_BY_OWASP_CATEGORY: dict[str, dict[str, list[str]]] = {
    "AGENT_GOAL_HIJACK": {
        "SOC 2": ["CC6.1", "CC7.2"],
        "ISO 27001": ["A.5.15", "A.8.28"],
        "NIST 800-53": ["AC-3", "SI-4"],
        "CSA CCM": ["AIS-01", "IAM-01"],
        "CIS Controls": ["IG1 Safeguard 4.2", "IG1 Safeguard 16.8"],
        "FedRAMP": ["AC-3", "SI-4"],
        "NIST 800-171": ["3.1.1", "3.14.2"],
        "FISMA": ["AC-3", "SI-4"],
        "Cybersecurity Maturity Model Certification (CMMC)": ["AC.2.007", "SI.2.216"],
        "OWASP Agentic Top 10": ["ASI01"],
        "EU AI Act": ["Art. 9", "Art. 13", "Art. 15", "Art. 25"],
        "NIST AI Risk Management Framework": ["Govern", "Map", "Measure", "Manage"],
        "MITRE ATLAS": ["AML.T0051", "AML.T0046"],
    },

    "TOOL_MISUSE_AND_EXPLOITATION": {
        "SOC 2": ["CC6.3", "CC7.2"],
        "ISO 27001": ["A.5.15", "A.8.20"],
        "NIST 800-53": ["CM-7", "SC-7", "SI-4"],
        "CSA CCM": ["AIS-01", "IVS-01"],
        "CIS Controls": ["IG1 Safeguard 4.8", "IG1 Safeguard 6.7"],
        "FedRAMP": ["CM-7", "SC-7"],
        "NIST 800-171": ["3.4.1", "3.13.1"],
        "FISMA": ["CM-7", "SI-4"],
        "Cybersecurity Maturity Model Certification (CMMC)": ["CM.2.062", "SC.3.180"],
        "OWASP Agentic Top 10": ["ASI02"],
        "EU AI Act": ["Art. 9", "Art. 13", "Art. 15", "Art. 25"],
        "NIST AI Risk Management Framework": ["Govern", "Map", "Measure", "Manage"],
        "MITRE ATLAS": ["AML.T0035", "AML.T0029"],
    },

    "IDENTITY_AND_PRIVILEGE_ABUSE": {
        "SOC 2": ["CC6.1", "CC6.2"],
        "ISO 27001": ["A.5.16", "A.5.17"],
        "NIST 800-53": ["IA-2", "IA-5", "AC-3"],
        "CSA CCM": ["IAM-01", "IAM-02"],
        "CIS Controls": ["IG1 Safeguard 5.2", "IG1 Safeguard 5.4"],
        "FedRAMP": ["IA-2", "AC-3"],
        "NIST 800-171": ["3.5.1", "3.5.2"],
        "FISMA": ["IA-2", "AC-3"],
        "Cybersecurity Maturity Model Certification (CMMC)": ["IA.2.083", "AC.2.007"],
        "OWASP Agentic Top 10": ["ASI03"],
        "EU AI Act": ["Art. 9", "Art. 12", "Art. 15", "Art. 25"],
        "NIST AI Risk Management Framework": ["Govern", "Map", "Measure", "Manage"],
        "MITRE ATLAS": ["AML.T0026", "AML.T0005"],
    },

    "AGENTIC_SUPPLY_CHAIN": {
        "SOC 2": ["CC9.2", "CC6.1"],
        "ISO 27001": ["A.5.19", "A.5.21"],
        "NIST 800-53": ["SR-3", "SA-10", "SI-7"],
        "CSA CCM": ["AIS-01", "SEF-01"],
        "CIS Controls": ["IG1 Safeguard 2.5", "IG1 Safeguard 16.4"],
        "FedRAMP": ["SR-3", "SI-7"],
        "NIST 800-171": ["3.4.1", "3.14.6"],
        "FISMA": ["SA-10", "SI-7"],
        "Cybersecurity Maturity Model Certification (CMMC)": ["SA.3.169", "SI.7.216"],
        "OWASP Agentic Top 10": ["ASI04"],
        "EU AI Act": ["Art. 9", "Art. 13", "Art. 25", "Art. 72"],
        "NIST AI Risk Management Framework": ["Govern", "Map", "Measure", "Manage"],
        "MITRE ATLAS": ["AML.T0013", "AML.T0011"],
    },

    "UNEXPECTED_CODE_EXECUTION": {
        "SOC 2": ["CC6.6", "CC7.2"],
        "ISO 27001": ["A.8.28", "A.8.29"],
        "NIST 800-53": ["SI-10", "SC-18", "SI-7"],
        "CSA CCM": ["AIS-01", "IVS-01"],
        "CIS Controls": ["IG1 Safeguard 10.1", "IG1 Safeguard 10.2"],
        "FedRAMP": ["SI-10", "SC-18"],
        "NIST 800-171": ["3.14.1", "3.14.2"],
        "FISMA": ["SI-10", "SC-18"],
        "Cybersecurity Maturity Model Certification (CMMC)": ["SI.2.216", "SI.3.218"],
        "OWASP Agentic Top 10": ["ASI05"],
        "EU AI Act": ["Art. 9", "Art. 13", "Art. 15", "Art. 25"],
        "NIST AI Risk Management Framework": ["Govern", "Map", "Measure", "Manage"],
        "MITRE ATLAS": ["AML.T0053", "AML.T0040"],
    },

    "MEMORY_AND_CONTEXT_POISONING": {
        "SOC 2": ["CC6.1", "CC6.7"],
        "ISO 27001": ["A.5.33", "A.8.13"],
        "NIST 800-53": ["SI-7", "SC-28", "SI-10"],
        "CSA CCM": ["DSP-01", "AIS-01"],
        "CIS Controls": ["IG1 Safeguard 11.2", "IG1 Safeguard 11.3"],
        "FedRAMP": ["SC-28", "SI-7"],
        "NIST 800-171": ["3.8.1", "3.14.6"],
        "FISMA": ["SC-28", "SI-7"],
        "Cybersecurity Maturity Model Certification (CMMC)": ["SC.28.125", "SI.7.216"],
        "OWASP Agentic Top 10": ["ASI06"],
        "EU AI Act": ["Art. 9", "Art. 10", "Art. 13", "Art. 25"],
        "NIST AI Risk Management Framework": ["Govern", "Map", "Measure", "Manage"],
        "MITRE ATLAS": ["AML.T0043", "AML.T0018"],
    },

    "INSECURE_INTER_AGENT_COMMUNICATION": {
        "SOC 2": ["CC6.1", "CC6.7"],
        "ISO 27001": ["A.5.14", "A.8.20"],
        "NIST 800-53": ["SC-8", "SC-13", "AC-4"],
        "CSA CCM": ["IVS-01", "DSP-01"],
        "CIS Controls": ["IG1 Safeguard 13.6", "IG1 Safeguard 13.10"],
        "FedRAMP": ["SC-8", "SC-13"],
        "NIST 800-171": ["3.13.1", "3.13.8"],
        "FISMA": ["SC-8", "AC-4"],
        "Cybersecurity Maturity Model Certification (CMMC)": ["SC.3.180", "SC.8.133"],
        "OWASP Agentic Top 10": ["ASI07"],
        "EU AI Act": ["Art. 9", "Art. 13", "Art. 15", "Art. 25"],
        "NIST AI Risk Management Framework": ["Govern", "Map", "Measure", "Manage"],
        "MITRE ATLAS": ["AML.T0027", "AML.T0030"],
    },

    "CASCADING_FAILURES": {
        "SOC 2": ["CC9.1", "CC7.2"],
        "ISO 27001": ["A.5.29", "A.8.14"],
        "NIST 800-53": ["CP-2", "SC-5", "SI-4"],
        "CSA CCM": ["BCR-01", "SEF-01"],
        "CIS Controls": ["IG1 Safeguard 11.3", "IG1 Safeguard 17.6"],
        "FedRAMP": ["CP-2", "SI-4"],
        "NIST 800-171": ["3.6.1", "3.14.6"],
        "FISMA": ["CP-2", "SI-4"],
        "Cybersecurity Maturity Model Certification (CMMC)": ["CP.2.059", "SI.2.216"],
        "OWASP Agentic Top 10": ["ASI08"],
        "EU AI Act": ["Art. 9", "Art. 13", "Art. 15", "Art. 25"],
        "NIST AI Risk Management Framework": ["Govern", "Map", "Measure", "Manage"],
        "MITRE ATLAS": ["AML.T0034"],
    },

    "HUMAN_AGENT_TRUST_EXPLOITATION": {
        "SOC 2": ["CC2.2", "CC7.2"],
        "ISO 27001": ["A.5.10", "A.6.3"],
        "NIST 800-53": ["AT-2", "PL-4", "SI-4"],
        "CSA CCM": ["AIS-01", "GRM-01"],
        "CIS Controls": ["IG1 Safeguard 14.1", "IG1 Safeguard 14.2"],
        "FedRAMP": ["AT-2", "PL-4"],
        "NIST 800-171": ["3.2.1", "3.2.2"],
        "FISMA": ["AT-2", "SI-4"],
        "Cybersecurity Maturity Model Certification (CMMC)": ["AT.2.056", "PL.4.058"],
        "OWASP Agentic Top 10": ["ASI09"],
        "EU AI Act": ["Art. 9", "Art. 13", "Art. 15", "Art. 25"],
        "NIST AI Risk Management Framework": ["Govern", "Map", "Measure", "Manage"],
        "MITRE ATLAS": ["AML.T0015", "AML.T0021"],
    },

    "ROGUE_AGENTS": {
        "SOC 2": ["CC7.3", "CC7.4"],
        "ISO 27001": ["A.5.24", "A.5.26"],
        "NIST 800-53": ["IR-4", "IR-8", "SI-4"],
        "CSA CCM": ["SEF-01", "IAM-01"],
        "CIS Controls": ["IG1 Safeguard 17.7", "IG1 Safeguard 17.8"],
        "FedRAMP": ["IR-4", "SI-4"],
        "NIST 800-171": ["3.11.1", "3.14.6"],
        "FISMA": ["IR-4", "SI-4"],
        "Cybersecurity Maturity Model Certification (CMMC)": ["IR.2.092", "SI.2.216"],
        "OWASP Agentic Top 10": ["ASI10"],
        "EU AI Act": ["Art. 9", "Art. 15", "Art. 25", "Art. 26"],
        "NIST AI Risk Management Framework": ["Govern", "Map", "Measure", "Manage"],
        "MITRE ATLAS": ["AML.T0036", "AML.T0037"],
    },
}

ORDERED_SECTIONS: list[str] = [
    "SOC 2",
    "ISO 27001",
    "NIST 800-53",
    "CSA CCM",
    "CIS Controls",
    "FedRAMP",
    "NIST 800-171",
    "FISMA",
    "Cybersecurity Maturity Model Certification (CMMC)",
    "OWASP Agentic Top 10",
    "EU AI Act",
    "NIST AI Risk Management Framework",
    "MITRE ATLAS",
]


def _render_section(title: str, items: list[str]) -> str:
    return f"{title}:\n" + "\n".join(f"- {i}" for i in items)


def build_conf(short_key: str, display_name: str) -> str:
    row = MATRIX_BY_OWASP_CATEGORY.get(short_key)
    if row is None:
        sections = {k: list(v) for k, v in DEFAULT_CONTROLS.items()}
        sections["OWASP Agentic Top 10"] = [
            OWASP_AGENTIC_ASI_BY_SHORTNAME.get(short_key, display_name)
        ]
    else:
        sections = {title: list(row[title]) for title in ORDERED_SECTIONS}

    return "\n".join(_render_section(title, sections[title]) for title in ORDERED_SECTIONS) + "\n"


def main() -> int:
    if not GEN_TESTS.is_dir():
        print("Missing generated_tests:", GEN_TESTS, file=sys.stderr)
        return 1
    COMPLIANCE.mkdir(parents=True, exist_ok=True)

    written = 0
    errors: list[str] = []
    for yml in sorted(GEN_TESTS.glob("*.yml")):
        if yml.name.startswith("_"):
            continue
        try:
            doc = yaml.safe_load(yml.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"{yml.name}: parse {e}")
            continue

        info = (doc or {}).get("info") or {}
        test_id = doc.get("id") or yml.stem
        cat = info.get("category") or {}
        short_key = (cat.get("shortName") or cat.get("name") or "").strip()
        display_name = (cat.get("displayName") or cat.get("name") or "").strip() or "OWASP Agentic Category"

        body = build_conf(short_key=short_key, display_name=display_name)
        (COMPLIANCE / f"{test_id}.conf").write_text(body, encoding="utf-8", newline="\n")
        written += 1

    print(f"compliance files written: {written}")
    if errors:
        print("errors:", len(errors), file=sys.stderr)
        for e in errors[:20]:
            print(" ", e, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
