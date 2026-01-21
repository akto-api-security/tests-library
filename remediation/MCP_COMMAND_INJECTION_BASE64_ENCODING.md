# Remediation steps for Command Injection via Base64 Encoding with Echo (MCP)

**Vulnerability ID:** MCP_COMMAND_INJECTION_BASE64_ENCODING
**Severity:** CRITICAL
**CWE:** CWE-77 (Command Injection), CWE-78 (OS Command Injection)

---

## 1. Eliminate Shell Execution (Primary Defense)
The most effective remediation is to stop passing user-controlled input (decoded or otherwise) to a shell interpreter like `sh`, `bash`, or `cmd`.

* **Avoid System Calls:** Replace functions like `os.system()`, `subprocess.Popen(shell=True)`, or `eval()` with secure alternatives.
* **Use Parameterized APIs:** Use APIs that take arguments as a list rather than a single string. This prevents the shell from interpreting meta-characters like `;`, `&`, or `|`.

---

## 2. Secure Input Processing & Decoding Logic
Attackers use Base64 to hide payloads from simple regex filters. Your application must validate the content *after* decoding but *before* processing.

* **Post-Decode Validation:** Never trust the output of a Base64 decoding operation. Run a secondary validation check on the resulting string.
* **Strict Character Whitelisting:** If the expected input is alphanumeric, reject any decoded string containing shell characters (e.g., `$`, `(`, `)`, `` ` ``, `;`, `|`).

---

## 3. Implementation Example (Java/Spring Boot)
As a Java developer, ensure you are using `ProcessBuilder` correctly without invoking a shell wrapper.

```java
// VULNERABLE: Invokes shell which interprets the decoded command
// String command = "echo " + decodedInput + " | some_tool";
// Runtime.getRuntime().exec(new String[]{"sh", "-c", command});

// SECURE: Direct execution without shell interpretation
public void processInputSecurely(String base64Input) throws Exception {
    // 1. Decode
    byte[] decodedBytes = Base64.getDecoder().decode(base64Input);
    String decodedString = new String(decodedBytes, StandardCharsets.UTF_8);

    // 2. Validate (Post-Decode)
    if (!decodedString.matches("^[a-zA-Z0-9_ ]*$")) {
        throw new SecurityException("Invalid characters detected in payload");
    }

    // 3. Parameterized Execution
    ProcessBuilder pb = new ProcessBuilder("echo", decodedString);
    pb.start();
}
```

## 4. Architectural Guardrails (MCP Isolation)
The Model Context Protocol environment must be hardened to prevent lateral movement if an injection occurs.

| Layer | Remediation Action | Purpose |
| :--- | :--- | :--- |
| Least Privilege | Non-privileged User | Run the MCP service under a user with no shell access (/usr/sbin/nologin) and no sudo permissions. |
| Sandboxing | Containerization | Run the LLM/MCP logic in a read-only container (Docker/Podman) with a minimal filesystem. |
| AppArmor / Seccomp | Syscall Filtering | Restrict the types of system calls the process can make. Block execve unless strictly necessary. |

## 5. Detection & Monitoring
Since this attack targets the echo and base64 binaries, monitor for unusual process child-parent relationships.

* **SIEM Alerts:** Flag any process where base64 --decode is piped directly into bash, sh, or eval.
* **EDR Monitoring:** Monitor for the execution of high-risk commands like id, whoami, curl, or wget originating from the MCP service account.
* **Regex for Encoded Payloads:** Implement a WAF rule to look for common Base64-encoded signatures of malicious commands (e.g., Y2F0IC9ldGMvcGFzc3dk which is cat /etc/passwd).

## 6. Security Testing Validation
Verify your fixes by attempting to bypass the filters using the payload format from the MCP template.

```bash
# Test for Command Injection vulnerability
# Payload: eval "$(echo "aWQgJiYgaWQ=" | base64 --decode)"
curl -X POST https://api.your-system.com/mcp \
  -d '{
    "jsonrpc": "2.0",
    "method": "process",
    "params": {
      "input": "ZXZhbCAiJChlY2hvICJhV1FnSmlBbmFXUXsiIHwgYmFzZTY0IC0tZGVjb2RlKSI="
    },
    "id": 1
  }'
# EXPECTED: A 400 Bad Request or 403 Forbidden, NOT the output of the 'id' command.
```
