

## Remediation Steps for Command Injection via Curl
Command injection via Curl is a serious security flaw. Taking right precautions during the development of the application should minimize the risks of such vulnerability. 

Here are some remediation steps:
### Step 1: Validate and Sanitize Input
An initial step in preventing command injection attacks is proper input validation. This generally involves eliminating or escaping characters that can allow for command execution. It can be implemented using regular expressions for instance.

Here is an example in Python:

```python
import re
user_input = re.sub(r'[^a-zA-Z0-9]', '', user_input)
```

### Step 2: Use Safe APIs

Using safe API that avoid the use of the shell to execute commands can prevent the arbitrary command execution. If possible, avoid APIs like `system()`, which could be manipulated for command injection.

For example, instead of using curl via `os.system` in Python:

```python
import os
os.system('curl {}'.format(url))
```

You should use the `requests` library like so:
```python
import requests
response = requests.get(url)
```

This way, command injection is impossible because there's no shell that interprets the input.

### Step 3: Implement Least Privilege Principle
The principle of least privilege is a important principle to adhere to in system security. Under this principle, a user is given the minimum levels of access necessary to perform his/her job functions. In the case of a web service or application, this can involve implementing thorough access controls to ensure that only the necessary parts of a system are available to a user.

In addition, it may be prudent to use a low-privileged user to run your web server or app, to limit what a command injection attack can do.