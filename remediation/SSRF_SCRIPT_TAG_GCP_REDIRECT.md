

## Remediation Steps for SSRF Test via Replacing Parameters with Script Tags

Server Side Request Forgery (SSRF) test via replacing parameters with script tags containing redirect URLs for GCP internal URL is a serious security threat. If not handled properly, it can allow attackers to make requests from the server, effectively circumventing access controls and reaching internal systems.

### Step 1: Validate and Sanitize Input

Ensure that all user-provided input is properly validated and sanitized. This can help prevent attackers from injecting malicious payloads.

```python
import re

def sanitize_input(input_str):
    regexp = re.compile(r'<[^\>]*script[^\>]*\>[^\>]*\<\/[^\>]*script[^\>]*\>')
    sanitized_str = regexp.sub('', input_str)
    return sanitized_str
```

### Step 2: Limit Outbound Traffic 

Limit outbound traffic from your application server to mitigate the risk of SSRF attacks. Set up a firewall to restrict outbound network traffic.

```bash
sudo ufw deny out to any
```

### Step 3: Block Default Ports 

Block GCP default internal metadata server ports, this can help to mitigate the server from being exploited via SSRF vulnerabilities.

```bash
sudo ufw deny out 169.254.169.254
```
### Step 4: Use SSRF Mitigating Libraries

There are programming libraries that help in mitigating SSRF attacks, make use of them in your code. 

For example, in Python you can use the `ssrf_protect` library.

```bash
pip install ssrf-protect
```
And then in your code:

```python
from ssrf_protect.ssrf_protect import SSRFProtect

url = "http://some_external_source.com/"  # The URL you need to send a request
try:
    SSRFProtect.validate(url)  # Will throw an exception if the URL is not safe.

    # Your logic for sending the request here
except Exception as e:
    print("Not a valid URL")
```