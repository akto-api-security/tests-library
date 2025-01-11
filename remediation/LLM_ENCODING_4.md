# Remediation for LLM_ENCODING_4

## Remediation Steps for Prompt Injection with encoding on LLMs - Base64 Sample Long String

Prompt Injection with encoding on LLMs presents a substantial security risk, allowing attackers to manipulate your system.

For these particular steps, let's use Python as our language example, but these principles can be adapted to other languages. Please check and understand each code snippet before implementing it.

### Step 1: Sanitize User Input
Always sanitize any user input to avert injection attacks. A basic example could be denying special characters for non-admin users.

```python
def sanitize(input_string):
    if input_string:
        sanitized_string = re.sub(r"[^a-zA-Z0-9]+", ' ', input_string)
        return sanitized_string
    return None
```
### Step 2: Avoid Using User Input Directly in Shell Commands

Executing shell commands using user input can lead directly to a shell injection vulnerability. Always validate user inputs before using them in this context.

```python
def safe_subprocess_run(user_input):
    sanitized_input = sanitize(user_input)
    if sanitized_input:
        subprocess.run(['./my_script.sh', sanitized_input])
```
### Step 3: Base64 Encode and Decode Safely

Encode and decode Base64 strings safely to avoid Long String attacks. 

```python
import base64

def safe_base64_encode(input_string):
    sanitized_input = sanitize(input_string)
    encoded_bytes = base64.b64encode(sanitized_input.encode("utf-8"))
    encoded_string = str(encoded_bytes, "utf-8")
    return encoded_string

def safe_base64_decode(input_string):
    decoded_bytes = base64.b64decode(input_string)
    decoded_string = str(decoded_bytes, "utf-8")
    return sanitize(decoded_string)
```