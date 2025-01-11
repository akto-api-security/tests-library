# Remediation for SSRF_SCRIPT_TAG_BASIC

## Remediation Steps for SSRF Test via Replacing Parameters
Server-Side Request Forgery (SSRF) attacks occur when an attacker is able to make a request to a server from the victim's system. One form of SSRF attack vectors involves substituting legitimate parameters in a request with script tags containing harmful URLs.
### Step 1: Validate Input 
Ensure that all input from the user is checked for malicious code. This can be achieved by making use of secure coding practices and libraries to sanitize and encode user input.
```python
from django.core.exceptions import ValidationError

def validate_script(value):
    if "<script" in value:
        raise ValidationError("Invalid input: script tags are not allowed.")
```
### Step 2: Make Use of Safe Libraries or APIs
In many programming languages, there are built-in libraries or APIs that can prevent SSRF attacks. 
For example, in PHP, you can use the `parse_url()` function to validate if the URL schema is http(s) before making the request.
```php
$url_parts = parse_url($url);
if($url_parts['scheme'] == 'http' || $url_parts['scheme'] == 'https'){
    // If it is, proceed with the request.
}
```
### Step 3: Limit and Monitor Server Permissions and Requests 
Limit and monitor the server's permissions to interact with internal and external resources. Use custom firewall rules to block unwanted or suspicious outgoing requests.
```bash
sudo iptables -A OUTPUT -p tcp --dport 80 -j DROP
sudo iptables -A OUTPUT -p tcp --dport 443 -j DROP
```
