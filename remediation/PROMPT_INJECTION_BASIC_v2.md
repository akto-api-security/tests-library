# Remediation for PROMPT_INJECTION_BASIC_v2

## Remediation Steps for Basic Prompt Injection Test on LLMs: Print Hello

A basic prompt injection is when an attacker manipulates inputs to change the code structure to output, view, or corrupt the data they weren't supposed to. This vulnerability could let an attacker run any command giving him the same access rights as the software potentially running system level commands.

### Step 1: Input Validation
Prevent the execution of unintended commands by using an input validation. This means don't trust user input without validating it first. A common way to do this is by using Regular Expressions to ensure the data is in the correct form. Here, the user input must only contain alphanumeric characters.
```python
import re
def validate_input(user_input):
    if re.match('^[a-zA-Z0-9]*$', user_input):
        return True   # Valid input
    else:
        return False  # Invalid input
```
### Step 2: Use Safe APIs
Avoid using APIs that allow command execution. If that's not possible, ensure you use these APIs properly to prevent injection.
```python
import subprocess
subprocess.call(['echo', 'Hello'])
```
Instead of:
```python
import os
os.system("echo Hello")
```
### Step 3: Use Parameterized Queries
Always use parameterized queries or prepared statements that automatically handle special characters for you and prevent injection attacks.
```python
import psycopg2
conn = psycopg2.connect("dbname=test user=postgres password=secret")
cur = conn.cursor()
cur.execute('SELECT * FROM table WHERE column=%s', (user_input,))
```
### Step 4: Regular Audit and Update
Regularly audit your codebase for injection vulnerabilities - especially when adding new features. Update your dependencies regularly, many security vulnerabilities come from outdated packages or libraries.