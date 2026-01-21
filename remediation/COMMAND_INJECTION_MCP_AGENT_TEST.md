# Command Injection Remediation for MCP Agents

## 1. Architectural Remediation (The "Gold Standard")

The most effective fix is to remove the shell interpreter from the execution chain entirely.

### Avoid Shell Wrappers
Instead of executing commands via `sh -c` or `cmd.exe`, use language-native system calls. This ensures that arguments are treated as literal strings rather than executable logic.

### Direct Execution
Use the "exec" family of functions:
- `execve` in C
- `subprocess.run(shell=False)` in Python
- `child_process.spawn()` in Node.js

### Process Isolation
Execute all MCP tools inside an unprivileged container (Docker/Podman) or a specialized sandbox (gVisor/Firecracker). If an injection occurs, the attacker is trapped in a "throwaway" environment.

## 2. Input Validation & Tool Schema Enforcement

MCP tools rely on structured schemas. You must treat the LLM as an untrusted user and validate its "intent."

### Strict Regex Constraints
In your tool definitions, use JSON Schema pattern properties to restrict input.

**Example:** If a tool takes a filename, use `^[a-zA-Z0-9._-]+$`. This automatically blocks characters like `;`, `$`, and `|`.

### Allowlisting Arguments
If a tool has a fixed set of operations, use an enum in the tool definition. Never allow the LLM to pass raw strings that are concatenated into a command.

### Input Sanitization
If you must use a shell, use a library specifically designed for escaping shell arguments, such as `shlex.quote()` in Python.

## 3. Environment Variable Security

Since the vulnerability specifically targets variable assignment, you must harden how your agent handles its environment.

### Variable Scoping
Do not pass the parent process's environment variables to the child tool process. Instead, provide a "Clean Room" environment containing only the specific variables required for that tool.

### Secret Masking
Ensure that sensitive variables (API keys, DB credentials) are not accessible to the `env` or `printenv` commands.

### External Secret Managers
Move away from OS environment variables. Use a Secret Manager (HashiCorp Vault, AWS Secrets Manager) where the tool fetches a secret via an API call using a temporary token, rather than reading it from a persistent variable.

## 4. System-Level Hardening (Least Privilege)

Restrict what the process is physically allowed to do on the host machine.

| Method | Description |
|--------|-------------|
| **RBASH** | Use a Restricted Shell to prevent the user from changing directories or setting environment variables. |
| **AppArmor / SELinux** | Create a profile for your MCP server that explicitly denies access to sensitive files (e.g., `/etc/passwd`) and high-risk binaries (e.g., `curl`, `netcat`). |
| **Non-Root User** | Never run an MCP server as root. Use a dedicated service account with no sudoers privileges. |

## 5. Monitoring and "Agentic" Guardrails

Since LLMs can be creative in their bypasses, implement runtime monitoring.

### Command Logging
Log every command executed by the MCP agent, including the raw arguments and the resulting environment state.

### Heuristic Analysis
Monitor for "high-entropy" strings in tool arguments or common injection patterns like `$(...)` or `` `...` ``.

### Output Filtering
Implement a filter that scans tool outputs for sensitive patterns (like the `ey...` prefix mentioned in your test case, which often indicates a JWT) and redacts them before the LLM sees the result.
