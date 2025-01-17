

## Remediation Steps for Command Injection using Here String and Chained System Commands

Command injection is a critical vulnerability that is exploited when unsanitized user inputs are passed into a system shell. Here String and chained system commands can amplify this security issue. To remediate this issue, you can adopt the following steps.

### Step 1: Avoid Using System Commands Directly
Try to rewrite your code by using native language functions and libraries that don't involve system shell interaction.

```python
# BAD CODE
import os
userInput = input("Enter your name: ")
os.system("echo Hello " + userInput)

# GOOD CODE
userInput = input("Enter your name: ")
print("Hello " + userInput)
```

### Step 2: Sanitize User Input
If you absolutely need to use system commands, always sanitize the user input. Use an allowlist-based approach to check the input against a set of pre-approved inputs.

```python
# Python Code
userInput = input("Enter your name: ")

# Allowlist of characters
allowlist = set("abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ ")
if set(userInput).issubset(allowlist):
    print('Hello ' + userInput)
else:
    print("Invalid characters in your input!")
```

### Step 3: Limit Privileges of Your Application
Run your application with the least necessary privileges. That way, even if a command injection occurs, the potential damage is limited.

```bash
# Run as a non-privileged user
sudo -u nobody python3 your_script.py
```

### Step 4: Use Prepared Statements
When interacting with databases, use prepared statements or parameterized queries. They ensure that the inputs passed are always treated as literals, not executable code.

```python
# Python Code with sqlite3
import sqlite3

userInput = input("Enter your name: ")
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("SELECT * FROM Users WHERE Name=?", (userInput,))
```