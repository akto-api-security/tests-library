

## Remediation Steps for SSRF (Server-Side Request Forgery) Test Via Parameter Replacement

SSRF attacks can be a serious security issue. Attackers can trick the server into making calls to internal resources - including potentially private information, gain unauthorized access, and use it as a footstep to launch more serious attacks.

Below are the steps to remediate SSRF with an example of checking and improving parameter handling, validation and encoding in HttpService GET request, shown in Python.

### Step 1: Validating URLs

Url should be validated before they are processed. Reject any suspicious or malformed Urls.

```python
import validators

def validate_url(url):
    if validators.url(url):
        return True
    else: 
        return False
```

### Step 2: Limiting Protocols

Ensure only HTTP/S protocols are used in your application. 

```python
def validate_protocol(url):
    if url.startswith(('http://', 'https://')):
        return True
    else:
        return False
```

### Step 3: Apply Network Segmentation and Firewalls

Imposing network level filters can also protect the internal network and resources from being accessed from SSRF attacks.

Note: It is infrastructure and platform specific. You need to consult your infrastructure manuals for concrete steps.


### Step 4: Denylist Local and Reserved IP Addresses

Block requests going to localhost, 127.0.0.1, or in general any IP address from the private IP ranges:

```python
from ipaddress import ip_address, ip_network

def is_in_network(ip):
    networks = [
        ip_network('127.0.0.0/8'),    # localhost
        ip_network('10.0.0.0/8'),     # Private network
        ip_network('172.16.0.0/12'),  # Private network
        ip_network('192.168.0.0/16'), # Private network
    ]
    ip = ip_address(ip)

    for network in networks:
        if ip in network:
            return True

    return False
```

Don't forget to call these functions before any HTTP request is made.

```python
from urllib.parse import urlparse

url = 'http://example.com'

if validate_url(url) and validate_protocol(url) and not is_in_network(urlparse(url).hostname):
    # Safe to be requested
    pass
```