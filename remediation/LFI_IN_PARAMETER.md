# Remediation for LFI_IN_PARAMETER

## Remediation Steps for Local File Inclusion (LFI) in Parameter
Local File Inclusion (LFI) is a common security vulnerability that can occur when user-supplied input is not properly sanitized. This allows an attacker to access sensitive files or even execute arbitrary code.

### Step 1: Validate User Input
Validate user inputs to ensure they meet expected patterns and reject any input that does not match these patterns. Below is an example in Python:

```python
import re

def sanitize_user_input(user_input):
    # only accept alphanumeric characters and dashes
    pattern = re.compile('^[a-zA-Z0-9_-]*$')
    if not pattern.match(user_input):
        raise ValueError("Invalid characters in input")
    return user_input
```

### Step 2: Avoid Using User-Supplied Input to Access Files
Do not use user-supplied input to access file system resources directly. If you can't avoid this, ensure that the input is strictly validated as shown in the previous step.

### Step 3: Limit Access to File System
Limit the application's access to the file system using operating system-level controls. For instance, in Unix-based systems, you may use `chroot`:

```bash
mkdir /var/my_app
chmod 700 /var/my_app
chroot /var/my_app
```