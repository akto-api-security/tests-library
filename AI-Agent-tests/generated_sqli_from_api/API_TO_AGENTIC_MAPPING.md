# API SQL/NoSQL template → generated agentic test mapping

Auto-generated — do not edit by hand.

Regenerate:

```bash
python3 AI-Agent-tests/generate_agentic_sqli_from_api.py --write-mapping
```

Generator: `AI-Agent-tests/generate_agentic_sqli_from_api.py`.
Output directory: `AI-Agent-tests/generated_sqli_from_api/`.

## Hand-maintained (not from `generate_agentic_sqli_from_api.py`)

| API template (old) | Agentic template (new) |
|--------------------|--------------------------|
| `Broken-User-Authentication/SQLiErrorBasedParamMySQL.yml` | `Broken-User-Authentication/SQLiErrorBasedParamMySQL_AGENTIC.yml` (id `SQLI_ERROR_BASED_PARAM_MYSQL_AGENTIC`) |

## Summary (one API template → base agentic id)

| API template (old) | `variant_key` | Base agentic test id | Base filename |
|--------------------|---------------|----------------------|---------------|
| `Broken-User-Authentication/AuthBypassSQLInjection.yml` | `auth_bypass_login_body` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY.yml` |
| `Broken-User-Authentication/NoSQLiErrorBasedReplaceBodyMongo.yml` | `replace_body_mongo` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO.yml` |
| `Broken-User-Authentication/SQLInjectionRefererHeader.yml` | `referer_header` | `SECURITY_SQL_AGENTIC_REFERER_HEADER` | `SECURITY_SQL_AGENTIC_REFERER_HEADER.yml` |
| `Broken-User-Authentication/SQLInjectionUserAgentHeader.yml` | `user_agent_header` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadMySQL.yml` | `append_payload_mysql` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadPostgreSQL.yml` | `append_payload_postgresql` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadSQLite.yml` | `append_payload_sqlite` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamMySQL.yml` | `error_based_param_mysql` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamPostgreSQL.yml` | `error_based_param_postgresql` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL.yml` |
| `Verbose-Error-Messages/SQLInjectionURLPath.yml` | `url_path_verbose_error` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR.yml` |

## Expanded profile outputs (`--expand-profiles`)

- **SQL** sources: `SECURITY_SQL_AGENTIC_<VARIANT>_<PROFILE>.yml` — 13 profiles per source (see `SQL_PROBE_PROFILES` in the generator).
- **NoSQL** sources: `SECURITY_NOSQL_AGENTIC_<VARIANT>_<PROFILE>.yml` — 12 profiles per source (see `NOSQL_PROBE_PROFILES`).
- With **`--expand-profiles --emit-base`**, each source also gets the base file above (same id as summary).

## Full mapping (every generated file id)

| API template (old) | `variant_key` | Profile | Agentic test id | Filename |
|--------------------|---------------|---------|-----------------|----------|
| `Broken-User-Authentication/AuthBypassSQLInjection.yml` | `auth_bypass_login_body` | `boolean_tautology` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_BOOLEAN_TAUTOLOGY` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_BOOLEAN_TAUTOLOGY.yml` |
| `Broken-User-Authentication/AuthBypassSQLInjection.yml` | `auth_bypass_login_body` | `quote_breaking` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_QUOTE_BREAKING` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_QUOTE_BREAKING.yml` |
| `Broken-User-Authentication/AuthBypassSQLInjection.yml` | `auth_bypass_login_body` | `comment_termination` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_COMMENT_TERMINATION` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_COMMENT_TERMINATION.yml` |
| `Broken-User-Authentication/AuthBypassSQLInjection.yml` | `auth_bypass_login_body` | `union_select` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_UNION_SELECT` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_UNION_SELECT.yml` |
| `Broken-User-Authentication/AuthBypassSQLInjection.yml` | `auth_bypass_login_body` | `stacked_queries` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_STACKED_QUERIES` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_STACKED_QUERIES.yml` |
| `Broken-User-Authentication/AuthBypassSQLInjection.yml` | `auth_bypass_login_body` | `time_blind` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_TIME_BLIND` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_TIME_BLIND.yml` |
| `Broken-User-Authentication/AuthBypassSQLInjection.yml` | `auth_bypass_login_body` | `error_based` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_ERROR_BASED` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_ERROR_BASED.yml` |
| `Broken-User-Authentication/AuthBypassSQLInjection.yml` | `auth_bypass_login_body` | `second_order` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_SECOND_ORDER` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_SECOND_ORDER.yml` |
| `Broken-User-Authentication/AuthBypassSQLInjection.yml` | `auth_bypass_login_body` | `encoding_obfuscation` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_ENCODING_OBFUSCATION` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_ENCODING_OBFUSCATION.yml` |
| `Broken-User-Authentication/AuthBypassSQLInjection.yml` | `auth_bypass_login_body` | `multiturn_escalation` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_MULTITURN_ESCALATION` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_MULTITURN_ESCALATION.yml` |
| `Broken-User-Authentication/AuthBypassSQLInjection.yml` | `auth_bypass_login_body` | `function_boundary` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_FUNCTION_BOUNDARY` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_FUNCTION_BOUNDARY.yml` |
| `Broken-User-Authentication/AuthBypassSQLInjection.yml` | `auth_bypass_login_body` | `like_wildcards` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_LIKE_WILDCARDS` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_LIKE_WILDCARDS.yml` |
| `Broken-User-Authentication/AuthBypassSQLInjection.yml` | `auth_bypass_login_body` | `mixed_families` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_MIXED_FAMILIES` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY_MIXED_FAMILIES.yml` |
| `Broken-User-Authentication/AuthBypassSQLInjection.yml` | `auth_bypass_login_body` | *(base, no profile)* | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY` | `SECURITY_SQL_AGENTIC_AUTH_BYPASS_LOGIN_BODY.yml` |
| `Broken-User-Authentication/NoSQLiErrorBasedReplaceBodyMongo.yml` | `replace_body_mongo` | `operator_eq_ne` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_OPERATOR_EQ_NE` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_OPERATOR_EQ_NE.yml` |
| `Broken-User-Authentication/NoSQLiErrorBasedReplaceBodyMongo.yml` | `replace_body_mongo` | `boolean_logic` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_BOOLEAN_LOGIC` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_BOOLEAN_LOGIC.yml` |
| `Broken-User-Authentication/NoSQLiErrorBasedReplaceBodyMongo.yml` | `replace_body_mongo` | `regex_operator` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_REGEX_OPERATOR` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_REGEX_OPERATOR.yml` |
| `Broken-User-Authentication/NoSQLiErrorBasedReplaceBodyMongo.yml` | `replace_body_mongo` | `where_function` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_WHERE_FUNCTION` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_WHERE_FUNCTION.yml` |
| `Broken-User-Authentication/NoSQLiErrorBasedReplaceBodyMongo.yml` | `replace_body_mongo` | `type_confusion` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_TYPE_CONFUSION` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_TYPE_CONFUSION.yml` |
| `Broken-User-Authentication/NoSQLiErrorBasedReplaceBodyMongo.yml` | `replace_body_mongo` | `update_operators` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_UPDATE_OPERATORS` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_UPDATE_OPERATORS.yml` |
| `Broken-User-Authentication/NoSQLiErrorBasedReplaceBodyMongo.yml` | `replace_body_mongo` | `injection_nesting` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_INJECTION_NESTING` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_INJECTION_NESTING.yml` |
| `Broken-User-Authentication/NoSQLiErrorBasedReplaceBodyMongo.yml` | `replace_body_mongo` | `encoding_obfuscation` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_ENCODING_OBFUSCATION` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_ENCODING_OBFUSCATION.yml` |
| `Broken-User-Authentication/NoSQLiErrorBasedReplaceBodyMongo.yml` | `replace_body_mongo` | `multiturn_escalation` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_MULTITURN_ESCALATION` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_MULTITURN_ESCALATION.yml` |
| `Broken-User-Authentication/NoSQLiErrorBasedReplaceBodyMongo.yml` | `replace_body_mongo` | `mixed_operators` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_MIXED_OPERATORS` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_MIXED_OPERATORS.yml` |
| `Broken-User-Authentication/NoSQLiErrorBasedReplaceBodyMongo.yml` | `replace_body_mongo` | `error_leakage` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_ERROR_LEAKAGE` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_ERROR_LEAKAGE.yml` |
| `Broken-User-Authentication/NoSQLiErrorBasedReplaceBodyMongo.yml` | `replace_body_mongo` | `auth_bypass_shape` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_AUTH_BYPASS_SHAPE` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO_AUTH_BYPASS_SHAPE.yml` |
| `Broken-User-Authentication/NoSQLiErrorBasedReplaceBodyMongo.yml` | `replace_body_mongo` | *(base, no profile)* | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO` | `SECURITY_NOSQL_AGENTIC_REPLACE_BODY_MONGO.yml` |
| `Broken-User-Authentication/SQLInjectionRefererHeader.yml` | `referer_header` | `boolean_tautology` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_BOOLEAN_TAUTOLOGY` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_BOOLEAN_TAUTOLOGY.yml` |
| `Broken-User-Authentication/SQLInjectionRefererHeader.yml` | `referer_header` | `quote_breaking` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_QUOTE_BREAKING` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_QUOTE_BREAKING.yml` |
| `Broken-User-Authentication/SQLInjectionRefererHeader.yml` | `referer_header` | `comment_termination` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_COMMENT_TERMINATION` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_COMMENT_TERMINATION.yml` |
| `Broken-User-Authentication/SQLInjectionRefererHeader.yml` | `referer_header` | `union_select` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_UNION_SELECT` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_UNION_SELECT.yml` |
| `Broken-User-Authentication/SQLInjectionRefererHeader.yml` | `referer_header` | `stacked_queries` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_STACKED_QUERIES` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_STACKED_QUERIES.yml` |
| `Broken-User-Authentication/SQLInjectionRefererHeader.yml` | `referer_header` | `time_blind` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_TIME_BLIND` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_TIME_BLIND.yml` |
| `Broken-User-Authentication/SQLInjectionRefererHeader.yml` | `referer_header` | `error_based` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_ERROR_BASED` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_ERROR_BASED.yml` |
| `Broken-User-Authentication/SQLInjectionRefererHeader.yml` | `referer_header` | `second_order` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_SECOND_ORDER` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_SECOND_ORDER.yml` |
| `Broken-User-Authentication/SQLInjectionRefererHeader.yml` | `referer_header` | `encoding_obfuscation` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_ENCODING_OBFUSCATION` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_ENCODING_OBFUSCATION.yml` |
| `Broken-User-Authentication/SQLInjectionRefererHeader.yml` | `referer_header` | `multiturn_escalation` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_MULTITURN_ESCALATION` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_MULTITURN_ESCALATION.yml` |
| `Broken-User-Authentication/SQLInjectionRefererHeader.yml` | `referer_header` | `function_boundary` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_FUNCTION_BOUNDARY` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_FUNCTION_BOUNDARY.yml` |
| `Broken-User-Authentication/SQLInjectionRefererHeader.yml` | `referer_header` | `like_wildcards` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_LIKE_WILDCARDS` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_LIKE_WILDCARDS.yml` |
| `Broken-User-Authentication/SQLInjectionRefererHeader.yml` | `referer_header` | `mixed_families` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_MIXED_FAMILIES` | `SECURITY_SQL_AGENTIC_REFERER_HEADER_MIXED_FAMILIES.yml` |
| `Broken-User-Authentication/SQLInjectionRefererHeader.yml` | `referer_header` | *(base, no profile)* | `SECURITY_SQL_AGENTIC_REFERER_HEADER` | `SECURITY_SQL_AGENTIC_REFERER_HEADER.yml` |
| `Broken-User-Authentication/SQLInjectionUserAgentHeader.yml` | `user_agent_header` | `boolean_tautology` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_BOOLEAN_TAUTOLOGY` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_BOOLEAN_TAUTOLOGY.yml` |
| `Broken-User-Authentication/SQLInjectionUserAgentHeader.yml` | `user_agent_header` | `quote_breaking` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_QUOTE_BREAKING` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_QUOTE_BREAKING.yml` |
| `Broken-User-Authentication/SQLInjectionUserAgentHeader.yml` | `user_agent_header` | `comment_termination` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_COMMENT_TERMINATION` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_COMMENT_TERMINATION.yml` |
| `Broken-User-Authentication/SQLInjectionUserAgentHeader.yml` | `user_agent_header` | `union_select` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_UNION_SELECT` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_UNION_SELECT.yml` |
| `Broken-User-Authentication/SQLInjectionUserAgentHeader.yml` | `user_agent_header` | `stacked_queries` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_STACKED_QUERIES` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_STACKED_QUERIES.yml` |
| `Broken-User-Authentication/SQLInjectionUserAgentHeader.yml` | `user_agent_header` | `time_blind` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_TIME_BLIND` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_TIME_BLIND.yml` |
| `Broken-User-Authentication/SQLInjectionUserAgentHeader.yml` | `user_agent_header` | `error_based` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_ERROR_BASED` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_ERROR_BASED.yml` |
| `Broken-User-Authentication/SQLInjectionUserAgentHeader.yml` | `user_agent_header` | `second_order` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_SECOND_ORDER` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_SECOND_ORDER.yml` |
| `Broken-User-Authentication/SQLInjectionUserAgentHeader.yml` | `user_agent_header` | `encoding_obfuscation` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_ENCODING_OBFUSCATION` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_ENCODING_OBFUSCATION.yml` |
| `Broken-User-Authentication/SQLInjectionUserAgentHeader.yml` | `user_agent_header` | `multiturn_escalation` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_MULTITURN_ESCALATION` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_MULTITURN_ESCALATION.yml` |
| `Broken-User-Authentication/SQLInjectionUserAgentHeader.yml` | `user_agent_header` | `function_boundary` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_FUNCTION_BOUNDARY` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_FUNCTION_BOUNDARY.yml` |
| `Broken-User-Authentication/SQLInjectionUserAgentHeader.yml` | `user_agent_header` | `like_wildcards` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_LIKE_WILDCARDS` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_LIKE_WILDCARDS.yml` |
| `Broken-User-Authentication/SQLInjectionUserAgentHeader.yml` | `user_agent_header` | `mixed_families` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_MIXED_FAMILIES` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER_MIXED_FAMILIES.yml` |
| `Broken-User-Authentication/SQLInjectionUserAgentHeader.yml` | `user_agent_header` | *(base, no profile)* | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER` | `SECURITY_SQL_AGENTIC_USER_AGENT_HEADER.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadMySQL.yml` | `append_payload_mysql` | `boolean_tautology` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_BOOLEAN_TAUTOLOGY` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_BOOLEAN_TAUTOLOGY.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadMySQL.yml` | `append_payload_mysql` | `quote_breaking` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_QUOTE_BREAKING` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_QUOTE_BREAKING.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadMySQL.yml` | `append_payload_mysql` | `comment_termination` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_COMMENT_TERMINATION` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_COMMENT_TERMINATION.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadMySQL.yml` | `append_payload_mysql` | `union_select` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_UNION_SELECT` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_UNION_SELECT.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadMySQL.yml` | `append_payload_mysql` | `stacked_queries` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_STACKED_QUERIES` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_STACKED_QUERIES.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadMySQL.yml` | `append_payload_mysql` | `time_blind` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_TIME_BLIND` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_TIME_BLIND.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadMySQL.yml` | `append_payload_mysql` | `error_based` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_ERROR_BASED` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_ERROR_BASED.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadMySQL.yml` | `append_payload_mysql` | `second_order` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_SECOND_ORDER` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_SECOND_ORDER.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadMySQL.yml` | `append_payload_mysql` | `encoding_obfuscation` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_ENCODING_OBFUSCATION` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_ENCODING_OBFUSCATION.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadMySQL.yml` | `append_payload_mysql` | `multiturn_escalation` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_MULTITURN_ESCALATION` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_MULTITURN_ESCALATION.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadMySQL.yml` | `append_payload_mysql` | `function_boundary` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_FUNCTION_BOUNDARY` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_FUNCTION_BOUNDARY.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadMySQL.yml` | `append_payload_mysql` | `like_wildcards` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_LIKE_WILDCARDS` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_LIKE_WILDCARDS.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadMySQL.yml` | `append_payload_mysql` | `mixed_families` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_MIXED_FAMILIES` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL_MIXED_FAMILIES.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadMySQL.yml` | `append_payload_mysql` | *(base, no profile)* | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_MYSQL.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadPostgreSQL.yml` | `append_payload_postgresql` | `boolean_tautology` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_BOOLEAN_TAUTOLOGY` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_BOOLEAN_TAUTOLOGY.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadPostgreSQL.yml` | `append_payload_postgresql` | `quote_breaking` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_QUOTE_BREAKING` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_QUOTE_BREAKING.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadPostgreSQL.yml` | `append_payload_postgresql` | `comment_termination` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_COMMENT_TERMINATION` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_COMMENT_TERMINATION.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadPostgreSQL.yml` | `append_payload_postgresql` | `union_select` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_UNION_SELECT` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_UNION_SELECT.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadPostgreSQL.yml` | `append_payload_postgresql` | `stacked_queries` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_STACKED_QUERIES` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_STACKED_QUERIES.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadPostgreSQL.yml` | `append_payload_postgresql` | `time_blind` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_TIME_BLIND` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_TIME_BLIND.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadPostgreSQL.yml` | `append_payload_postgresql` | `error_based` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_ERROR_BASED` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_ERROR_BASED.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadPostgreSQL.yml` | `append_payload_postgresql` | `second_order` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_SECOND_ORDER` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_SECOND_ORDER.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadPostgreSQL.yml` | `append_payload_postgresql` | `encoding_obfuscation` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_ENCODING_OBFUSCATION` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_ENCODING_OBFUSCATION.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadPostgreSQL.yml` | `append_payload_postgresql` | `multiturn_escalation` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_MULTITURN_ESCALATION` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_MULTITURN_ESCALATION.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadPostgreSQL.yml` | `append_payload_postgresql` | `function_boundary` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_FUNCTION_BOUNDARY` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_FUNCTION_BOUNDARY.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadPostgreSQL.yml` | `append_payload_postgresql` | `like_wildcards` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_LIKE_WILDCARDS` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_LIKE_WILDCARDS.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadPostgreSQL.yml` | `append_payload_postgresql` | `mixed_families` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_MIXED_FAMILIES` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL_MIXED_FAMILIES.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadPostgreSQL.yml` | `append_payload_postgresql` | *(base, no profile)* | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_POSTGRESQL.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadSQLite.yml` | `append_payload_sqlite` | `boolean_tautology` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_BOOLEAN_TAUTOLOGY` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_BOOLEAN_TAUTOLOGY.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadSQLite.yml` | `append_payload_sqlite` | `quote_breaking` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_QUOTE_BREAKING` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_QUOTE_BREAKING.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadSQLite.yml` | `append_payload_sqlite` | `comment_termination` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_COMMENT_TERMINATION` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_COMMENT_TERMINATION.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadSQLite.yml` | `append_payload_sqlite` | `union_select` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_UNION_SELECT` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_UNION_SELECT.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadSQLite.yml` | `append_payload_sqlite` | `stacked_queries` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_STACKED_QUERIES` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_STACKED_QUERIES.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadSQLite.yml` | `append_payload_sqlite` | `time_blind` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_TIME_BLIND` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_TIME_BLIND.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadSQLite.yml` | `append_payload_sqlite` | `error_based` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_ERROR_BASED` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_ERROR_BASED.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadSQLite.yml` | `append_payload_sqlite` | `second_order` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_SECOND_ORDER` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_SECOND_ORDER.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadSQLite.yml` | `append_payload_sqlite` | `encoding_obfuscation` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_ENCODING_OBFUSCATION` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_ENCODING_OBFUSCATION.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadSQLite.yml` | `append_payload_sqlite` | `multiturn_escalation` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_MULTITURN_ESCALATION` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_MULTITURN_ESCALATION.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadSQLite.yml` | `append_payload_sqlite` | `function_boundary` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_FUNCTION_BOUNDARY` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_FUNCTION_BOUNDARY.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadSQLite.yml` | `append_payload_sqlite` | `like_wildcards` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_LIKE_WILDCARDS` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_LIKE_WILDCARDS.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadSQLite.yml` | `append_payload_sqlite` | `mixed_families` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_MIXED_FAMILIES` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE_MIXED_FAMILIES.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamAppendPayloadSQLite.yml` | `append_payload_sqlite` | *(base, no profile)* | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE` | `SECURITY_SQL_AGENTIC_APPEND_PAYLOAD_SQLITE.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamMySQL.yml` | `error_based_param_mysql` | `boolean_tautology` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_BOOLEAN_TAUTOLOGY` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_BOOLEAN_TAUTOLOGY.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamMySQL.yml` | `error_based_param_mysql` | `quote_breaking` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_QUOTE_BREAKING` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_QUOTE_BREAKING.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamMySQL.yml` | `error_based_param_mysql` | `comment_termination` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_COMMENT_TERMINATION` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_COMMENT_TERMINATION.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamMySQL.yml` | `error_based_param_mysql` | `union_select` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_UNION_SELECT` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_UNION_SELECT.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamMySQL.yml` | `error_based_param_mysql` | `stacked_queries` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_STACKED_QUERIES` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_STACKED_QUERIES.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamMySQL.yml` | `error_based_param_mysql` | `time_blind` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_TIME_BLIND` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_TIME_BLIND.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamMySQL.yml` | `error_based_param_mysql` | `error_based` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_ERROR_BASED` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_ERROR_BASED.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamMySQL.yml` | `error_based_param_mysql` | `second_order` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_SECOND_ORDER` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_SECOND_ORDER.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamMySQL.yml` | `error_based_param_mysql` | `encoding_obfuscation` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_ENCODING_OBFUSCATION` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_ENCODING_OBFUSCATION.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamMySQL.yml` | `error_based_param_mysql` | `multiturn_escalation` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_MULTITURN_ESCALATION` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_MULTITURN_ESCALATION.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamMySQL.yml` | `error_based_param_mysql` | `function_boundary` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_FUNCTION_BOUNDARY` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_FUNCTION_BOUNDARY.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamMySQL.yml` | `error_based_param_mysql` | `like_wildcards` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_LIKE_WILDCARDS` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_LIKE_WILDCARDS.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamMySQL.yml` | `error_based_param_mysql` | `mixed_families` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_MIXED_FAMILIES` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL_MIXED_FAMILIES.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamMySQL.yml` | `error_based_param_mysql` | *(base, no profile)* | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_MYSQL.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamPostgreSQL.yml` | `error_based_param_postgresql` | `boolean_tautology` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_BOOLEAN_TAUTOLOGY` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_BOOLEAN_TAUTOLOGY.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamPostgreSQL.yml` | `error_based_param_postgresql` | `quote_breaking` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_QUOTE_BREAKING` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_QUOTE_BREAKING.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamPostgreSQL.yml` | `error_based_param_postgresql` | `comment_termination` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_COMMENT_TERMINATION` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_COMMENT_TERMINATION.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamPostgreSQL.yml` | `error_based_param_postgresql` | `union_select` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_UNION_SELECT` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_UNION_SELECT.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamPostgreSQL.yml` | `error_based_param_postgresql` | `stacked_queries` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_STACKED_QUERIES` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_STACKED_QUERIES.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamPostgreSQL.yml` | `error_based_param_postgresql` | `time_blind` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_TIME_BLIND` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_TIME_BLIND.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamPostgreSQL.yml` | `error_based_param_postgresql` | `error_based` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_ERROR_BASED` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_ERROR_BASED.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamPostgreSQL.yml` | `error_based_param_postgresql` | `second_order` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_SECOND_ORDER` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_SECOND_ORDER.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamPostgreSQL.yml` | `error_based_param_postgresql` | `encoding_obfuscation` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_ENCODING_OBFUSCATION` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_ENCODING_OBFUSCATION.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamPostgreSQL.yml` | `error_based_param_postgresql` | `multiturn_escalation` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_MULTITURN_ESCALATION` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_MULTITURN_ESCALATION.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamPostgreSQL.yml` | `error_based_param_postgresql` | `function_boundary` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_FUNCTION_BOUNDARY` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_FUNCTION_BOUNDARY.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamPostgreSQL.yml` | `error_based_param_postgresql` | `like_wildcards` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_LIKE_WILDCARDS` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_LIKE_WILDCARDS.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamPostgreSQL.yml` | `error_based_param_postgresql` | `mixed_families` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_MIXED_FAMILIES` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL_MIXED_FAMILIES.yml` |
| `Broken-User-Authentication/SQLiErrorBasedParamPostgreSQL.yml` | `error_based_param_postgresql` | *(base, no profile)* | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL` | `SECURITY_SQL_AGENTIC_ERROR_BASED_PARAM_POSTGRESQL.yml` |
| `Verbose-Error-Messages/SQLInjectionURLPath.yml` | `url_path_verbose_error` | `boolean_tautology` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_BOOLEAN_TAUTOLOGY` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_BOOLEAN_TAUTOLOGY.yml` |
| `Verbose-Error-Messages/SQLInjectionURLPath.yml` | `url_path_verbose_error` | `quote_breaking` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_QUOTE_BREAKING` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_QUOTE_BREAKING.yml` |
| `Verbose-Error-Messages/SQLInjectionURLPath.yml` | `url_path_verbose_error` | `comment_termination` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_COMMENT_TERMINATION` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_COMMENT_TERMINATION.yml` |
| `Verbose-Error-Messages/SQLInjectionURLPath.yml` | `url_path_verbose_error` | `union_select` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_UNION_SELECT` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_UNION_SELECT.yml` |
| `Verbose-Error-Messages/SQLInjectionURLPath.yml` | `url_path_verbose_error` | `stacked_queries` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_STACKED_QUERIES` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_STACKED_QUERIES.yml` |
| `Verbose-Error-Messages/SQLInjectionURLPath.yml` | `url_path_verbose_error` | `time_blind` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_TIME_BLIND` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_TIME_BLIND.yml` |
| `Verbose-Error-Messages/SQLInjectionURLPath.yml` | `url_path_verbose_error` | `error_based` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_ERROR_BASED` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_ERROR_BASED.yml` |
| `Verbose-Error-Messages/SQLInjectionURLPath.yml` | `url_path_verbose_error` | `second_order` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_SECOND_ORDER` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_SECOND_ORDER.yml` |
| `Verbose-Error-Messages/SQLInjectionURLPath.yml` | `url_path_verbose_error` | `encoding_obfuscation` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_ENCODING_OBFUSCATION` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_ENCODING_OBFUSCATION.yml` |
| `Verbose-Error-Messages/SQLInjectionURLPath.yml` | `url_path_verbose_error` | `multiturn_escalation` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_MULTITURN_ESCALATION` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_MULTITURN_ESCALATION.yml` |
| `Verbose-Error-Messages/SQLInjectionURLPath.yml` | `url_path_verbose_error` | `function_boundary` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_FUNCTION_BOUNDARY` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_FUNCTION_BOUNDARY.yml` |
| `Verbose-Error-Messages/SQLInjectionURLPath.yml` | `url_path_verbose_error` | `like_wildcards` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_LIKE_WILDCARDS` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_LIKE_WILDCARDS.yml` |
| `Verbose-Error-Messages/SQLInjectionURLPath.yml` | `url_path_verbose_error` | `mixed_families` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_MIXED_FAMILIES` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR_MIXED_FAMILIES.yml` |
| `Verbose-Error-Messages/SQLInjectionURLPath.yml` | `url_path_verbose_error` | *(base, no profile)* | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR` | `SECURITY_SQL_AGENTIC_URL_PATH_VERBOSE_ERROR.yml` |

## Profile slugs (SQL)

| `profile` slug |
|----------------|
| `boolean_tautology` |
| `quote_breaking` |
| `comment_termination` |
| `union_select` |
| `stacked_queries` |
| `time_blind` |
| `error_based` |
| `second_order` |
| `encoding_obfuscation` |
| `multiturn_escalation` |
| `function_boundary` |
| `like_wildcards` |
| `mixed_families` |

## Profile slugs (NoSQL)

| `profile` slug |
|----------------|
| `operator_eq_ne` |
| `boolean_logic` |
| `regex_operator` |
| `where_function` |
| `type_confusion` |
| `update_operators` |
| `injection_nesting` |
| `encoding_obfuscation` |
| `multiturn_escalation` |
| `mixed_operators` |
| `error_leakage` |
| `auth_bypass_shape` |
