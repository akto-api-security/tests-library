

## Remediation Steps for SSRF Vulnerability

Sensitive Server Side Request Forgery(SSRF) vulnerability is a critical security flaw. An attacker can leverage this vulnerability to bypass access controls, causing requests to be sent for unauthorized access to internal resources.


### Step 1: Safely Parse Redirect URLs

Ensure that you safely parse the incoming redirect URLs. Safely parsing URL parameters as below can prevent the exploit.

```python
from urllib.parse import urlparse

def safe_url(target):
    host = urlparse(target).hostname
    if not host:
        return None
    if host in ["localhost"]:
        return None
    return target
```

### Step 2: Limit Redirection Parameters

Do not trust user input blindly for redirect URL parameters. Make sure that user input is validated against a list of allowed URLs or against a specific URL pattern.

```python
ALLOWED_HOSTS = ['mydomain.com']

def is_valid_url(target):
    host = urlparse(target).hostname
    if host not in ALLOWED_HOSTS:
      return False
    return True
```

### Step 3: Block Localhost Traffic

Add middleware or use networking rules to block traffic to `localhost` and `127.0.0.1`.

```bash
sudo ufw deny from any to 127.0.0.1
sudo ufw deny from any to localhost
```