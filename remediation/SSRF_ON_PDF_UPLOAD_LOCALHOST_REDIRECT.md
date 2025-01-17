

## Remediation Steps for Sensitive Localhost details exposed via SSRF

Server Side Request Forgery (SSRF) is a type of vulnerability class where an attacker is able force a vulnerable server to make arbitrary HTTP/HTTPS requests to an arbitrary domain of the attacker's choosing. An attacker may trick server into making requests to localhost exposing sensitive details.

Here are the remediation steps for SSRF vulnerabilities:

### Step 1: Validate Input

Preventing SSRF attacks is often best achieved by implementing strict validation and filtering on server-side against all user-supplied data.

If possible, server-side code should make HTTP requests to a whitelist of approved IP addresses or domain names.

```python
import socket
from urllib.parse import urlparse


def is_valid_domain(domain):
    valid_domains = ['example.com', 'api.example.com']  # define valid domains
    if domain in valid_domains:
        return True
    return False


def ssrf_prevention(url):
    parsed = urlparse(url)
    domain = parsed.netloc.split(':')[0]
    
    if is_valid_domain(domain):
        pass  # process the request
    else:
        pass  # reject the request
```     

### Step 2: Limit HTTP Methods

Restrict HTTP methods that a server will be allowed to use during a request. Limiting the available HTTP methods can help to mitigate SSRF attacks.

```python
import requests


def safe_request(url, method):
    safe_methods = ['GET', 'POST', 'HEAD']
    if method in safe_methods:
        response = requests.request(method, url)
        return response
    else:
        return None
```

### Step 3: Update Packages

Always make sure all the packages you are using are up-to-date. These packages include libraries, server software like Node.js, Nginx and etc. This can prevent SSRF that may be caused by bugs in those packages. 

```bash
sudo apt update && sudo apt upgrade
```