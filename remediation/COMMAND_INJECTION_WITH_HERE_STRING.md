

## Remediation Steps for Command Injection Using Here String

Command injection is a serious security flaw that allows attackers to run arbitrary commands on your system. To protect against command injection through Here String, one should sanitize and validate all inputs that are being used in system commands.

### Step 1: Avoidance

The best way to avoid injection is to not use system commands at all if possible. Replace them with safer language-specific functions.

### Step 2: Use Prepared Statements or Parameterized Commands

In cases where system commands are unavoidable, use prepared statements or parameterized inputs. Here's an example in Python:

```python
from subprocess import Popen, PIPE 

def safe_command(user_input): 
    command = ['ls', '-l', user_input] 
    process = Popen(command, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
```
In the above code, each argument is treated as a separate entity by the shell and won't be processed for shell expansion.

### Step 3: Input Validation

Always validate the user input to make sure it contains only the types of characters you're expecting. This is an example using a whitelist in Python:

```python
import re
def validate_input(user_input): 
    # Only permit alphanumeric characters
    if not re.match("^[a-zA-Z0-9]*$", user_input):
        raise ValueError("Invalid characters in input!")
    else:
        return True
```

### Step 4: Use of Escaping Mechanisms 

Certain languages provide functions to escape potentially hazardous characters. For instance, PHP provides the `escapeshellarg` and `escapeshellcmd` functions:

```php
<?php
    $user_input = $_POST['user_input'];
    $sanitized_input = escapeshellarg($user_input);
    $command = "ls -l " . $sanitized_input;
    system($command);
?>
```