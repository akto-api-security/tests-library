import os
import re

# ─── OWASP MCP Top 10 (2025) ───────────────────────────────────────────────
MCP_CATEGORIES = {
    "MCP01": "Token Mismanagement & Secret Exposure",
    "MCP02": "Privilege Escalation via Scope Creep",
    "MCP03": "Tool Poisoning",
    "MCP04": "Software Supply Chain Attacks & Dependency Tampering",
    "MCP05": "Command Injection & Execution",
    "MCP06": "Intent Flow Subversion",
    "MCP07": "Insufficient Authentication & Authorization",
    "MCP08": "Lack of Audit and Telemetry",
    "MCP09": "Shadow MCP Servers",
    "MCP10": "Context Injection & Over-Sharing",
}

# ─── OWASP LLM Top 10 (2025) ───────────────────────────────────────────────
LLM_CATEGORIES = {
    "LLM01": "Prompt Injection",
    "LLM02": "Sensitive Information Disclosure",
    "LLM03": "Supply Chain",
    "LLM04": "Data and Model Poisoning",
    "LLM05": "Improper Output Handling",
    "LLM06": "Excessive Agency",
    "LLM07": "System Prompt Leakage",
    "LLM08": "Vector and Embedding Weaknesses",
    "LLM09": "Misinformation",
    "LLM10": "Unbounded Consumption",
}

# ─── MCP file → category code ──────────────────────────────────────────────
# MCP01 – Token Mismanagement & Secret Exposure
# Covers: tokens reflected in responses/headers, API key passthrough,
#         env var extraction (secrets in env), config extraction (creds in config),
#         response data leak
MCP_FILE_MAPPING = {
    "MCPAuthenticationTokenReflectionInResponse":       "MCP01",
    "MCPAuthenticationTokenReflectionInResponseHeaders":"MCP01",
    "MCPTokenPassthroughAPIKey":                        "MCP01",
    "MCPTokenPassthroughDownstreamToken":               "MCP01",
    "MCPTokenPassthroughOpaqueToken":                   "MCP01",
    "MCPEnvironmentVariablesExtraction":                "MCP01",
    "MCPConfigurationInformationExtraction":            "MCP01",
    "MCPResponseDataLeakCheck":                         "MCP01",

    # MCP02 – Privilege Escalation via Scope Creep
    # Covers: function calls escalating privilege, consent fatigue, unauthorized tool access
    "MCPFunctionCallPrivilegeEscalation":               "MCP02",
    "MCPConsentFatigueExploitation":                    "MCP02",
    "MCPUnauthorizedToolAccess":                        "MCP02",

    # MCP03 – Tool Poisoning
    # Covers: poisoning tool outputs, manipulating function call metadata/responses
    "MCPToolPoisoningViaOutputInjection":               "MCP03",
    "MCPFunctionCallDirectMethodManipulation":          "MCP03",
    "MCPFunctionCallMetadataInjection":                 "MCP03",
    "MCPFunctionCallOutputManipulation":                "MCP03",
    "MCPFunctionCallParamsNameManipulation":            "MCP03",
    "MCPFunctionCallResponseManipulation":              "MCP03",

    # MCP04 – Software Supply Chain Attacks & Dependency Tampering
    # Covers: deserialization via binary URIs (tampered dependencies)
    "MCPResourceBinaryUriDeserializationAttack":        "MCP04",

    # MCP05 – Command Injection & Execution
    # Covers: OS command injection, SQL injection, LDAP injection, path traversal,
    #         XSS injection, code injection in tools/resources, input validation bypasses,
    #         header injection, MIME type injection, parameter overloading
    "MCPCommandInjectionByPassingExtraValues":          "MCP05",
    "MCPCommandInjectionParameterInjection":            "MCP05",
    "MCPRemoteCommandInjectionRCE":                     "MCP05",
    "MCPSQLInjectionParameterInjection":                "MCP05",
    "MCPLDAPInjectionParameterInjection":               "MCP05",
    "MCPPathTraversalParameterInjection":               "MCP05",
    "MCPPathTraversalResourceUri":                      "MCP05",
    "MCPXSSInjectionParameterInjection":                "MCP05",
    "MCPResourcesReadCodeInjection":                    "MCP05",
    "MCPToolsCallCodeInjection":                        "MCP05",
    "MCPToolsCallCodeInjectionSandboxEscape":           "MCP05",
    "MCPToolsCallShellLikeCommand":                     "MCP05",
    "MCPFunctionCallParameterInjection":                "MCP05",
    "MCPFunctionCallNestedParameterInjection":          "MCP05",
    "MCPPingParameterInjection":                        "MCP05",
    "MCPByPassInputLengthValidation":                   "MCP05",
    "MCPByPassInputValidationWithNullValues":           "MCP05",
    "MCPBreakingJsonParsing":                           "MCP05",
    "MCPHeaderAllKeysInvalidValues":                    "MCP05",
    "MCPHeaderInvalidValues":                           "MCP05",
    "MCPInputValidationByReplacingParamWithArray":      "MCP05",
    "MCPInputValidationForBoolean":                     "MCP05",
    "MCPInvalidMIMETypeInjection":                      "MCP05",
    "MCPParamOverload":                                 "MCP05",
    "MCPDummyAcceptHeader":                             "MCP05",
    "MCPDummyContentLengthHeader":                      "MCP05",
    "MCPDummyContentTypeHeader":                        "MCP05",
    "MCPHTTPHeaderInjectionDoS":                        "MCP05",

    # MCP06 – Intent Flow Subversion
    # Covers: direct/indirect prompt injection, ANSI escape deception,
    #         session hijacking via prompt injection, resource prompt injection
    "MCPDirectPromptInjection":                                 "MCP06",
    "MCPIndirectPromptInjection":                               "MCP06",
    "MCPIndirectPromptInjectionCommandInjectionAgentTest":      "MCP06",
    "MCPIndirectPromptInjectionToolBypass":                     "MCP06",
    "MCPIndirectPromptInjectionToolBypassAgentTest":            "MCP06",
    "MCPResourcePromptInjection":                               "MCP06",
    "MCPSessionHijackingPromptInjection":                       "MCP06",
    "MCPANSICursorManipulationDeception":                       "MCP06",
    "MCPANSIHyperlinkManipulationDeception":                    "MCP06",
    "MCPANSIInvisibleTextDeception":                            "MCP06",
    "MCPANSIScreenClearingDeception":                           "MCP06",

    # MCP07 – Insufficient Authentication & Authorization
    # Covers: broken auth (wrong scheme, removed/replaced tokens, DNS rebinding),
    #         session issues, and DoS (lack of rate limiting = access control gap)
    "MCPAuthenticationByChangingAuthScheme":                    "MCP07",
    "MCPBrokenAuthenticationByRemovingToken":                   "MCP07",
    "MCPReplacingAuthToken":                                    "MCP07",
    "MCPDNSRebindingByExploitingOriginHeader":                  "MCP07",
    "MCPSessionHijackingFilteredAttack":                        "MCP07",
    "MCPSessionNotBoundToUser":                                 "MCP07",
    "MCPPredictableSessionIDs":                                 "MCP07",
    "MCPSessionMustUsePerRequestAuth":                          "MCP07",
    "MCPDenialOfServiceByEnteringLongStringsInUrl":             "MCP07",
    "MCPDenialOfServiceOnDateFields":                           "MCP07",
    "MCPDoSAttachFileInBody":                                   "MCP07",
    "MCPDoSAttachLargeFile":                                    "MCP07",
    "MCPDoSDeeplyNestedJSONBody":                               "MCP07",
    "MCPDoSTestCSVFileURL":                                     "MCP07",
    "MCPDoSTestHeaderKey":                                      "MCP07",
    "MCPDoSTestHeaderValue":                                    "MCP07",
    "MCPDoSTestJPGFileURL":                                     "MCP07",
    "MCPDoSTestJSONBodyKey":                                    "MCP07",
    "MCPDoSTestLongStringQueryParamJSONBodyValues":             "MCP07",
    "MCPDoSTestMP4FileURL":                                     "MCP07",
    "MCPDoSTestPDFFileURL":                                     "MCP07",
    "MCPDoSTestPNGFileURL":                                     "MCP07",
    "MCPDoSTestQueryParamKey":                                  "MCP07",
    "MCPDosTestLargeNumbers":                                   "MCP07",
    "MCPEmailRegexDOSSmallInput":                               "MCP07",
    "MCPExcessiveResourceReadsRateLimit":                       "MCP07",
    "MCPExpensiveSearch":                                       "MCP07",
    "MCPFunctionCallExcessiveInvocation":                       "MCP07",
    "MCPJSONBodyParameterBombingDoS":                           "MCP07",
    "MCPPingAmplificationAttack":                               "MCP07",
    "MCPPingFloodingDoS":                                       "MCP07",
    "MCPPingNoRateLimiting":                                    "MCP07",
    "MCPPingSlowResponse":                                      "MCP07",
    "MCPImproperPageSizeHandling":                              "MCP07",

    # MCP08 – Lack of Audit and Telemetry
    # Covers: extracting debug/internal details, exposing error internals,
    #         timing information leakage via ping, reflection of invalid arguments
    "MCPDebugInformationExtraction":                            "MCP08",
    "MCPInternalErrorExposure":                                 "MCP08",
    "MCPInternalSystemDetailsExtraction":                       "MCP08",
    "MCPInvalidArgumentsReflection":                            "MCP08",
    "MCPPingTimingInformationLeak":                             "MCP08",

    # MCP09 – Shadow MCP Servers
    # Covers: accessing unsupported protocol versions/methods, undefined tools,
    #         invalid protocol messages — probing for rogue/shadow endpoints
    "MCPInputValidationByPassingUnsupportedVersion":            "MCP09",
    "MCPInputValidationBypassingUnsupportedMcpMethod":          "MCP09",
    "MCPMethodNotFound":                                        "MCP09",
    "MCPInvalidToolCall":                                       "MCP09",
    "MCPPingInvalidJSONRPC":                                    "MCP09",
    "MCPPingMissingResponse":                                   "MCP09",
    "MCPInvalidRequestRemovedParam":                            "MCP09",
    "McpInvalidParams":                                         "MCP09",

    # MCP10 – Context Injection & Over-Sharing
    # Covers: cross-session context bleed, shared memory leakage, vector store bleed,
    #         conversation/tool/system prompt extraction, chain-of-thought extraction,
    #         session state persistence, model name leakage via parameters
    "MCPContextBleed":                                          "MCP10",
    "MCPCrossSessionContextBleeding":                           "MCP10",
    "MCPSharedMemoryContextLeakage":                            "MCP10",
    "MCPVectorStoreContextBleeding":                            "MCP10",
    "MCPConversationHistoryTheft":                              "MCP10",
    "MCPConversationHistoryExtractionViaParameters":            "MCP10",
    "MCPChainOfThoughtExtractionViaParameters":                 "MCP10",
    "MCPGlobalMemoryBufferLeakage":                             "MCP10",
    "MCPSessionStatePersistence":                               "MCP10",
    "MCPSystemPromptExtraction":                                "MCP10",
    "MCPSystemPromptExtractionViaParameters":                   "MCP10",
    "MCPToolCallHistoryExtractionViaParameters":                "MCP10",
    "MCPToolsListExtractionViaParameters":                      "MCP10",
    "MCPModelNameExtractionViaParameters":                      "MCP10",
}

# ─── LLM file → category code ──────────────────────────────────────────────
LLM_FILE_MAPPING = {
    # LLM01 – Prompt Injection
    # Covers: encoding/obfuscation-based prompt injection, STAN jailbreak,
    #         basic direct prompt injection, XSS via prompt injection
    "LLMEncoding#1":                                "LLM01",
    "LLMEncoding#2":                                "LLM01",
    "LLMEncoding#4":                                "LLM01",
    "LLMEncoding#5":                                "LLM01",
    "LLMObfuscation":                               "LLM01",
    "PromptInjectionBasic":                         "LLM01",
    "PromptInjectionBasicHello":                    "LLM01",
    "PromptInjectionBasicV2":                       "LLM01",
    "PromptInjectionSTANTest":                      "LLM01",
    "PromptInjectionXSSTest":                       "LLM01",

    # LLM05 – Improper Output Handling
    # Covers: insecure output handling tests and LLM generating complete malware,
    #         malware evasion, malware payloads, and malware subfunctions
    "InsecureOutputHandling#1":                     "LLM05",
    "InsecureOutputHandling#2":                     "LLM05",
    "LLMInsecureOutput#1":                          "LLM05",
    "LLMInsecureOutput#2":                          "LLM05",
    "LLMInsecureOutput#3":                          "LLM05",
    "LLMOverrelianceCompleteMalwareARM64":          "LLM05",
    "LLMOverrelianceCompleteMalwareC":              "LLM05",
    "LLMOverrelianceCompleteMalwareCPP":            "LLM05",
    "LLMOverrelianceCompleteMalwareCSharp":         "LLM05",
    "LLMOverrelianceCompleteMalwareRust":           "LLM05",
    "LLMOverrelianceCompleteMalwareSwift":          "LLM05",
    "LLMOverrelianceCompleteMalwarex86-64":         "LLM05",
    "LLMOverrelianceEvadeMalwareARM64":             "LLM05",
    "LLMOverrelianceEvadeMalwareC":                 "LLM05",
    "LLMOverrelianceEvadeMalwareCPP":               "LLM05",
    "LLMOverrelianceEvadeMalwareCSharp":            "LLM05",
    "LLMOverrelianceEvadeMalwareRust":              "LLM05",
    "LLMOverrelianceEvadeMalwareSwift":             "LLM05",
    "LLMOverrelianceEvadeMalwarex86-64":            "LLM05",
    "LLMOverrelianceEvadeMalwarex86":               "LLM05",
    "LLMOverrelianceMalwarePayloadsARM64":          "LLM05",
    "LLMOverrelianceMalwarePayloadsCPP":            "LLM05",
    "LLMOverrelianceMalwarePayloadsCSharp":         "LLM05",
    "LLMOverrelianceMalwarePayloadsSwift":          "LLM05",
    "LLMOverrelianceMalwarePayloadsx86-64":         "LLM05",
    "LLMOverrelianceMalwarePayloadsx86":            "LLM05",
    "LLMOverrelianceMalwareSubfunctionARM64":       "LLM05",
    "LLMOverrelianceMalwareSubfunctionC":           "LLM05",
    "LLMOverrelianceMalwareSubfunctionCPP":         "LLM05",
    "LLMOverrelianceMalwareSubfunctionCSharp":      "LLM05",
    "LLMOverrelianceMalwareSubfunctionRust":        "LLM05",
    "LLMOverrelianceMalwareSubfunctionSwift":       "LLM05",
    "LLMOverrelianceMalwareSubfunctionx86-64":      "LLM05",
    "LLMOverrelianceMalwareSubfunctionx86":         "LLM05",

    # LLM07 – System Prompt Leakage
    # Covers: injection used to extract/leak the system prompt
    "PromptLeakInjection":                          "LLM07",

    # LLM09 – Misinformation
    # Covers: overreliance on incorrect/hallucinated LLM outputs, package hallucination,
    #         misleading answers, emotional/psychological manipulation (sycophancy),
    #         social scoring manipulation (biased/harmful compliance)
    "LLMOverreliance#1":                                        "LLM09",
    "LLMOverreliance#2":                                        "LLM09",
    "LLMOverreliance#4":                                        "LLM09",
    "LLMOverreliance#5":                                        "LLM09",
    "LLMOverreliance#6":                                        "LLM09",
    "LLMOverrelianceMisleading":                                "LLM09",
    "LLMOverreliancePackageHallucination":                      "LLM09",
    "LLMOverrelianceWrongAnswer#2":                             "LLM09",
    "LLMComplianceEmotionManipulationPunishment":               "LLM09",
    "LLMComplianceEmotionManipulationUserVulnerability":        "LLM09",
    "LLMComplianceSocialScoreCommStyle":                        "LLM09",
    "LLMComplianceSocialScoring":                               "LLM09",
    "LLMComplianceSocialScoringProfileAttribututes":            "LLM09",
    "LLMComplinaceEmotionDependencyCultivation":                "LLM09",
    "LLMComplinaceEmotionManipulationEmpathy":                  "LLM09",
    "LLMComplinaceEmotionManipulationPhsychologicalSteering":   "LLM09",
    "LLMComplinaceEmotionManipulationShame":                    "LLM09",
    "LLMSocialScoringLanguageComplexity":                       "LLM09",
}


def update_file(filepath, cat_code, cat_name):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    display_name = f"{cat_code} - {cat_name}"

    # Match the category block (2-space indented) and replace name/shortName/displayName
    pattern = (
        r'(  category:\n    name: )([^\n]+)'
        r'(\n    shortName: )([^\n]+)'
        r'(\n    displayName: )([^\n]+)'
    )
    replacement = (
        f'\\g<1>{cat_code}'
        f'\\g<3>{cat_code}'
        f'\\g<5>{display_name}'
    )

    new_content, count = re.subn(pattern, replacement, content)

    if count > 0 and new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False


def process_directory(dir_path, file_mapping, category_dict, label):
    updated = 0
    skipped = 0
    no_match = []

    for fname in os.listdir(dir_path):
        if not (fname.endswith('.yml') or fname.endswith('.yaml')):
            continue

        # Strip extension to get the base name for lookup
        base = fname.rsplit('.', 1)[0]
        cat_code = file_mapping.get(base)

        if cat_code is None:
            no_match.append(fname)
            skipped += 1
            continue

        cat_name = category_dict[cat_code]
        fpath = os.path.join(dir_path, fname)
        if update_file(fpath, cat_code, cat_name):
            updated += 1
        else:
            skipped += 1

    print(f"\n{'─'*50}")
    print(f"  {label}")
    print(f"{'─'*50}")
    print(f"  Updated : {updated}")
    print(f"  Skipped : {skipped}")
    if no_match:
        print(f"  No mapping found for {len(no_match)} file(s):")
        for f in sorted(no_match):
            print(f"    - {f}")


BASE = os.path.dirname(os.path.abspath(__file__))

process_directory(
    os.path.join(BASE, "MCP-Security"),
    MCP_FILE_MAPPING,
    MCP_CATEGORIES,
    "MCP-Security  →  OWASP MCP Top 10 (2025)"
)

process_directory(
    os.path.join(BASE, "LLM-Security"),
    LLM_FILE_MAPPING,
    LLM_CATEGORIES,
    "LLM-Security  →  OWASP LLM Top 10 (2025)"
)
