# Remediation steps: Command Injection for MCP Write Agent

## 1. Secure Execution Layer (Eliminate the Shell)

The most common root cause is using a shell interpreter (like `/bin/sh` or `cmd.exe`) to run tools.

### Avoid Shell Execution
Never use functions like `os.system()` or `subprocess.run(..., shell=True)`. These interpret characters like `;`, `&`, and `$` as commands.

### Use Parameterized APIs
Pass arguments as an array/list. This ensures the operating system treats the input as a literal string argument for the program, not as a command to be parsed.

**Secure (Python):**
```python
subprocess.run(["/usr/bin/tool", user_input])
```

**Secure (Node.js):**
```javascript
child_process.spawn('/usr/bin/tool', [user_input])
```

## 2. Input Validation and MCP Schema Hardening

Since MCP tools are triggered by LLMs, the "User Input" is often the LLM's generated JSON.

### JSON Schema Enforcement
Use the MCP tool definition to strictly type all inputs. Use the `pattern` field to enforce regex that forbids shell metacharacters.

**Example Regex:** `^[a-zA-Z0-9_\-\.]+$` (Only allows alphanumeric, underscores, hyphens, and dots).

### Allowlist Tools
Create a hard allowlist of binaries that the MCP agent is permitted to call. Block access to dangerous system binaries like `grep`, `find`, `env`, `cat`, or `base64`.

## 3. Environment Variable & Secret Isolation

The attack specifically targets environment variables (searching for `ey`—the prefix for JWTs).

### Environment Scrubbing
When spawning a tool, do not inherit the MCP server's environment. Create a "Clean Room" environment containing only the 2-3 variables the tool actually needs.

### Secret Management
Move secrets out of environment variables. Use a vault (AWS Secrets Manager, Hashicorp Vault) where tools must authenticate to retrieve a secret, rather than finding it globally available in the shell.

### Redaction Layer
Implement an output filter for the MCP server. If the tool output contains patterns resembling secrets (e.g., `eyJ...`), the server should redact them before sending the data back to the LLM.

## 4. Least Privilege & Sandboxing

Assume the LLM will eventually find a way to inject a command; ensure that command has no power.

### Non-Root Execution
The MCP server must run as a dedicated, low-privilege user (e.g., `mcp_user`) with no sudo access.

### Containerization
Run each tool execution in an ephemeral Docker container or a sandbox like gVisor or NSJail.

### Read-Only Filesystem
Mount the tool's working directory as read-only, except for specific, temporary scratch spaces.

## 5. Monitoring and Auditing

### Audit Logging
Log the full command string and the environment variables passed to every tool execution.

### Behavioral Alarms
Trigger alerts if an MCP tool attempts to access `/etc/`, `.ssh/`, or execution of commands that pipe (`|`) data to external network addresses (e.g., `curl` or `nc`).
