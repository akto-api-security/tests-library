#!/usr/bin/env python3
"""
Update category.name, shortName, displayName in generated_tests/ YAML files.

All 3,822 tests are agent tests generated from:
  49 subcategories  (subcategory_meta_prompts.csv)
  × 13 strategies   (strategy_meta_prompts.csv)
  × 6 template runs (template.yml + 5 jailbreaking variants)
  = 3,822 files

All tests map to OWASP Top 10 for Agentic Applications 2026 (ASI01-ASI10).
https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

Mapping is derived from each subcategory's MetaPrompt in subcategory_meta_prompts.csv.
"""

import os
import re

GENERATED_DIR = os.path.join(os.path.dirname(__file__), "generated_tests")

# ─────────────────────────────────────────────────────────────────────────────
# OWASP Top 10 for Agentic Applications 2026
# Format: (filename_prefix_patterns, name, shortName, displayName)
# displayName format: "ASI0X - <Title>"
# ─────────────────────────────────────────────────────────────────────────────
CATEGORY_MAP = [

    # ASI01 - Agent Goal Hijacking
    # Covers any attack that redirects or overrides an agent's goals/instructions:
    # - Direct/indirect prompt injection, system-prompt override, jailbreaks,
    #   semantic manipulation, goal-redirection chains
    # - Making the agent reveal context/sensitive data by hijacking its response
    # - Tricking the agent into producing disallowed content (illegal advice, PII,
    #   privacy violations, profanity, harmful content) via framing/injections
    # - Competitor-check, off-topic, legally-binding, intentional-misuse tests
    #   all work by overriding the agent's intended business-scope instructions
    # - Paranoid-protection tests manipulate agent behavior via adversarial prompts
    # - Phishing tests trick the agent (via social-engineering prompts) into
    #   suggesting malicious links / fake login pages
    (
        [
            "SECURITY_AGENT_BEHAVIOR_HIJACK_AND_GOAL_MANIPULATION_",
            "SECURITY_PROMPT_INJECTION_",
            "SECURITY_INDIRECT_PROMPT_INJECTION_",
            "SECURITY_SYSTEM_PROMPT_OVERRIDE_",
            "SECURITY_JAILBREAK_",
            "SECURITY_MANIPULATION_",
            "SECURITY_CONTEXT_LEAKAGE_",          # achieved via prompt injection / roleplay
            "SECURITY_SENSITIVE_INFORMATION_DISCLOSURE_",  # tricking agent to reveal data
            "SECURITY_PHISHING_",                  # social-engineering the agent's outputs
            "SAFETY_ILLEGAL_ACTIVITIES_",          # overriding legal/ethical constraints
            "SAFETY_PII_",                         # tricking agent to reveal PII
            "SAFETY_PRIVACY_VIOLATION_",           # tricking agent into privacy disclosure
            "SAFETY_PROFANITY_",                   # bypassing content filters via prompts
            "SAFETY_HARMFUL_CONTENT_",             # framing/injection to elicit harmful output
            "BUSINESS_ALIGNMENT_COMPETITOR_CHECK_",   # breaching business scope constraints
            "BUSINESS_ALIGNMENT_INTENTIONAL_MISUSE_", # manipulating agent beyond intended use
            "BUSINESS_ALIGNMENT_LEGALLY_BINDING_",    # tricking agent into unauthorized role
            "BUSINESS_ALIGNMENT_OFF_TOPIC_",          # redirecting agent from its purpose
            "HALLUCINATION_AND_TRUSTWORTHINESS_PARANOID_PROTECTION_",  # behavioral manipulation
        ],
        "ASI01", "ASI01", "ASI01 - Agent Goal Hijacking",
    ),

    # ASI02 - Tool Misuse and Exploitation
    # Covers any attack exploiting the agent's connected tools, plugins, or APIs:
    # - Direct tool misuse, insecure plugin exploitation, malicious resource fetching
    # - Data exfiltration via agent's API/communication tools (reverse shells,
    #   HTTP exfil, misuse of agent messaging tools per the metaprompt)
    # - Tool discovery / enumeration (reconnaissance that enables tool exploitation)
    # - URL-check tests: malicious URLs that exploit the agent's URL-fetching tool
    (
        [
            "SECURITY_TOOL_MISUSE_AND_EXPLOITATION_",
            "SECURITY_INSECURE_PLUGIN_USE_",
            "SECURITY_MALICIOUS_RESOURCE_FETCHING_",
            "SECURITY_DATA_EXFILTRATION_",         # misuses agent's API/communication tools
            "SECURITY_TOOL_DISCOVERY_",            # reconnaissance precursor to tool misuse
            "HALLUCINATION_AND_TRUSTWORTHINESS_URL_CHECK_",  # malicious URL tool exploitation
        ],
        "ASI02", "ASI02", "ASI02 - Tool Misuse and Exploitation",
    ),

    # ASI03 - Identity and Privilege Abuse
    # Covers attacks on agent identity and authorization boundaries:
    # - Identity spoofing: impersonation, token replay, role-swap across agents/MCPs
    # - Repudiation/untraceability: hiding/altering audit traces to evade accountability
    # - Excessive agency: agent granted/claiming permissions beyond its authorized scope
    (
        [
            "SECURITY_IDENTITY_SPOOFING_",
            "SECURITY_REPUDIATION_UNTRACEABILITY_",
            "SECURITY_EXCESSIVE_AGENCY_",          # operating beyond authorized scope/privilege
        ],
        "ASI03", "ASI03", "ASI03 - Identity and Privilege Abuse",
    ),

    # ASI04 - Agentic Supply Chain Vulnerabilities
    # Covers attacks on the agent's upstream artifacts and model assets:
    # - Unverified/tampered models, plugins, dependency artifacts at onboarding
    # - Training data poisoning: malicious fine-tuning samples alter the model (supply chain)
    # - Model theft: query-based reconstruction / extraction of model parameters (IP theft)
    (
        [
            "SECURITY_AGENTIC_SUPPLY_CHAIN_VULNERABILITIES_",
            "SECURITY_TRAINING_DATA_POISONING_",   # model-level supply-chain attack
            "SECURITY_MODEL_THEFT_",               # stealing the model asset itself
        ],
        "ASI04", "ASI04", "ASI04 - Agentic Supply Chain Vulnerabilities",
    ),

    # ASI05 - Unexpected Code Execution
    # Covers agent outputs/tool calls triggering unsafe command execution:
    # - RCE via agent tool calls or natural-language execution paths
    # - General code execution through agent interfaces
    # - Web injection (SQLi, command injection) leading to server-side code execution
    # - XSS: script injection in agent output executed client-side
    (
        [
            "SECURITY_UNEXPECTED_CODE_EXECUTION_RCE_",
            "SECURITY_CODE_EXECUTION_",
            "SECURITY_WEB_INJECTION_",             # SQLi/command injection → code execution
            "SECURITY_XSS_",                       # script injection → browser code execution
        ],
        "ASI05", "ASI05", "ASI05 - Unexpected Code Execution",
    ),

    # ASI06 - Memory and Context Poisoning
    # Covers injection of adversarial data into agent memory, RAG, or context:
    # - Context poisoning: adversarial docs/session data in memory/RAG
    # - RAG poisoning: injecting misleading content into the retrieval store
    # - Cross-session leaks: failure of memory isolation across user sessions
    # - RAG precision: hallucinated/fabricated content injected into RAG responses
    (
        [
            "SECURITY_CONTEXT_POISONING_",
            "SECURITY_RAG_POISONING_",
            "SECURITY_CROSS_SESSION_LEAKS_",       # cross-session memory isolation failure
            "HALLUCINATION_AND_TRUSTWORTHINESS_RAG_PRECISION_",  # RAG store integrity issues
        ],
        "ASI06", "ASI06", "ASI06 - Memory and Context Poisoning",
    ),

    # ASI07 - Insecure Inter-Agent Communication
    # Covers attacks on message channels between agents in multi-agent systems:
    # - Forged, replayed, or tampered inter-agent messages
    # - Missing signing, replay protection, or mutual authentication
    (
        [
            "SECURITY_INSECURE_INTER_AGENT_COMMUNICATION_",
        ],
        "ASI07", "ASI07", "ASI07 - Insecure Inter-Agent Communication",
    ),

    # ASI08 - Cascading Failures
    # Covers faults in one agent propagating and compounding through the system:
    # - Hallucination propagation across multi-agent chains / RAG pipelines
    # - Overreliance: automated systems blindly executing unverified agent outputs,
    #   causing unsafe cascading actions across downstream components
    # - Model DoS: resource exhaustion (recursive queries, token floods) causing
    #   system-wide latency spikes or cascading availability failures
    # - Q&A hallucinations: factual errors propagating through automated pipelines
    (
        [
            "HALLUCINATION_AND_TRUSTWORTHINESS_HALLUCINATION_PROPAGATION_",
            "SECURITY_OVERRELIANCE_",              # blind trust in outputs → cascading actions
            "SECURITY_MODEL_DENIAL_OF_SERVICE_",   # resource exhaustion → system-wide cascade
            "HALLUCINATION_AND_TRUSTWORTHINESS_Q_A_",  # factual errors propagating downstream
        ],
        "ASI08", "ASI08", "ASI08 - Cascading Failures",
    ),

    # ASI09 - Human-Agent Trust Exploitation
    # Covers attacks that exploit or overwhelm human oversight of agents:
    # - Social-engineering and fatigue attacks tricking humans into approving
    #   unsafe agent actions or bypassing safeguards
    # - Flooding human reviewers with noisy alerts to trigger approval mistakes
    (
        [
            "BUSINESS_ALIGNMENT_HUMAN_AGENT_TRUST_EXPLOITATION_",
            "BUSINESS_ALIGNMENT_OVERWHELMING_HUMAN_IN_THE_LOOP_",
        ],
        "ASI09", "ASI09", "ASI09 - Human-Agent Trust Exploitation",
    ),

    # ASI10 - Rogue Agents
    # Covers agents exhibiting autonomous misalignment or deceptive behavior:
    # - Compromised/malicious agents exfiltrating, persisting, or moving laterally
    # - Agents intentionally misleading, evading constraints, or showing alignment drift
    #   (deceptive reasoning, misaligned incentives — NOT triggered by external injection)
    # - Bias tests: inherent agent bias producing outputs misaligned with societal norms
    #   (no explicit trick required — tests the agent's baseline misalignment)
    (
        [
            "BUSINESS_ALIGNMENT_ROGUE_AGENTS_",
            "BUSINESS_ALIGNMENT_MISALIGNED_AND_DECEPTIVE_BEHAVIORS_",
            "SAFETY_BIAS_",                        # inherent agent misalignment / bias
        ],
        "ASI10", "ASI10", "ASI10 - Rogue Agents",
    ),
]

# Regex to match and replace the category block (3 lines)
CATEGORY_BLOCK_RE = re.compile(
    r'(  category:\n)'
    r'(    name: )([^\n]+)(\n)'
    r'(    shortName: )([^\n]+)(\n)'
    r'(    displayName: )([^\n]+)(\n)'
)


def get_category_for_file(filename):
    for patterns, name, short_name, display_name in CATEGORY_MAP:
        for prefix in patterns:
            if filename.startswith(prefix):
                return name, short_name, display_name
    return None


def update_file(filepath, name, short_name, display_name):
    with open(filepath, "r") as f:
        content = f.read()

    def replacer(m):
        return (
            m.group(1)
            + m.group(2) + name + m.group(4)
            + m.group(5) + short_name + m.group(7)
            + m.group(8) + display_name + m.group(10)
        )

    new_content, count = CATEGORY_BLOCK_RE.subn(replacer, content)
    if count > 0 and new_content != content:
        with open(filepath, "w") as f:
            f.write(new_content)
        return True
    return False


def main():
    files = [f for f in os.listdir(GENERATED_DIR) if f.endswith(".yml")]
    updated = 0
    skipped = 0
    unmatched = []

    for filename in sorted(files):
        result = get_category_for_file(filename)
        if result is None:
            unmatched.append(filename)
            skipped += 1
            continue
        name, short_name, display_name = result
        filepath = os.path.join(GENERATED_DIR, filename)
        if update_file(filepath, name, short_name, display_name):
            updated += 1

    print(f"Updated: {updated}")
    print(f"Skipped (no match): {skipped}")
    if unmatched:
        print("Unmatched files:")
        for f in unmatched:
            print(f"  {f}")


if __name__ == "__main__":
    main()
