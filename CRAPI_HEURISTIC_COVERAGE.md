# crAPI × Akto — heuristic coverage (no smart testing)

## Verdict

**Almost.** Existing active heuristic templates cover most OWASP-style crAPI challenges. A few need **new generic PRO templates** (this branch). Two JWT edge cases need **platform JWT modifiers**, not YAML alone.

## Covered by existing heuristics

| Ch | Vuln | Active template(s) | Branch |
|---|---|---|---|
| 1–2 | BOLA | `REPLACE_AUTH_TOKEN`, `FUZZ_USER_ID` | master |
| 3 | Weak OTP / version downgrade | `BYPASS_OTP_RATE_LIMIT` (already rewrites `v3+` → `v2`) | standard |
| 4 | BFLA user listing | `BFLA_WITH_GET_METHOD`, `BFLA_INSERT_ADMIN_IN_URL_PATHS` | master |
| 7 | BFLA admin delete | `BFLA_INSERT_ADMIN_IN_URL_PATHS` | master |
| 11 | SSRF | `SSRF_ON_LOCALHOST(_ENCODED)`, `FETCH_SENSITIVE_FILES`, `STANDARD_SSRF` | master / standard / pro |
| 12 | NoSQLi | `NOSQLI_ERROR_BASED_REPLACE_BODY_MONGO` | master |
| 13 | SQLi | `SQLI_ERROR_BASED_PARAM_POSTGRESQL` | master |
| 14 | Missing auth | `REMOVE_TOKENS` | master |
| 15 | JWT none / bad sig / jku / jwk / kid | `JWT_NONE_ALGO`, `JWT_INVALID_SIGNATURE`, `ADD_JKU_TO_JWT`, `JWT_HEADER_PARAM_INJECTION_JWK`, `JWT_HEADER_PARAM_INJECTION_KID` | standard / master |

Note: integer mass-assignment templates on master (`INTEGER_MASS_ASSIGN_*`) are **`inactive: true`** — do not rely on them.

## New templates on this branch (`feature/crapi-heuristic-gaps-pro`)

| ID | File | Closes |
|---|---|---|
| `MASS_ASSIGNMENT_FULFILLMENT_STATUS` | `Mass-Assignment/MassAssignmentFulfillmentStatus.yml` | Ch 8–9 status=`returned` |
| `MASS_ASSIGNMENT_NEGATIVE_QUANTITY` | `Mass-Assignment/MassAssignmentNegativeQuantity.yml` | Ch 8–9 negative qty (active replacement for inactive number MA) |
| `EXCESSIVE_DATA_EXPOSURE_PROCESSING_PARAMS` | `Security-Misconfiguration/ExcessiveDataExposureProcessingParams.yml` | Ch 5 internal processing field leak |
| `MASS_ASSIGNMENT_PROCESSING_PARAMS` | `Mass-Assignment/MassAssignmentProcessingParams.yml` | Ch 10 writable processing params |
| `RESOURCE_CONSUMPTION_REPEAT_PARAM` | `Lack-of-Resources-and-Rate-Limiting/ResourceConsumptionRepeatParam.yml` | Ch 6 repeat/iteration amplification |
| `PROMPT_INJECTION_INSTRUCTION_OVERRIDE` | `LLM-Security/PromptInjectionInstructionOverride.yml` | Ch 16–18 (active; existing LLM prompt tests stay inactive) |
| `COMMAND_INJECTION_PROCESSING_PARAM` | `Command-Injection/CommandInjectionProcessingParam.yml` | Secret challenge / processing-param RCE path |

All are **generic** (key/url patterns, no product names).

## Residual gaps (YAML cannot forge these alone)

| Gap | Why |
|---|---|
| JWT alg confusion RS256→HS256 using JWKS | No `auth_context.*` modifier for JWKS-as-HMAC |
| Exact `kid=/dev/null` + empty HMAC | Built-in kid modifier uses `/proc/1/comm` + secret `systemd` |

`JWT_NONE_ALGO` / `JWT_INVALID_SIGNATURE` still exercise related broken JWT verification on many builds.

## Heuristic run list (subCategory IDs)

```
REPLACE_AUTH_TOKEN
FUZZ_USER_ID
BFLA_INSERT_ADMIN_IN_URL_PATHS
BFLA_WITH_GET_METHOD
REMOVE_TOKENS
BYPASS_OTP_RATE_LIMIT
JWT_NONE_ALGO
JWT_INVALID_SIGNATURE
ADD_JKU_TO_JWT
JWT_HEADER_PARAM_INJECTION_KID
JWT_HEADER_PARAM_INJECTION_JWK
NOSQLI_ERROR_BASED_REPLACE_BODY_MONGO
SQLI_ERROR_BASED_PARAM_POSTGRESQL
SSRF_ON_LOCALHOST
SSRF_ON_LOCALHOST_ENCODED
FETCH_SENSITIVE_FILES
STANDARD_SSRF
MASS_ASSIGNMENT_CHANGE_ACCOUNT
MASS_ASSIGNMENT_CHANGE_ROLE
COMMAND_INJECTION_BY_ADDING_QUERY_PARAM
MASS_ASSIGNMENT_FULFILLMENT_STATUS
MASS_ASSIGNMENT_NEGATIVE_QUANTITY
EXCESSIVE_DATA_EXPOSURE_PROCESSING_PARAMS
MASS_ASSIGNMENT_PROCESSING_PARAMS
RESOURCE_CONSUMPTION_REPEAT_PARAM
PROMPT_INJECTION_INSTRUCTION_OVERRIDE
COMMAND_INJECTION_PROCESSING_PARAM
```
