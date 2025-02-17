

## Remediation Steps for Incorrect IP Injection in HTTP Headers

Incorrect IP injection in HTTP headers can lead to unauthorized requests, data leaks, and potential Denial-of-service (DoS) attacks. Here's how you can mitigate this security issue.

### Step 1: Validating IP Addresses
Firstly, ensure to validate IP addresses before they are processed. A common way to validate an IPv4 address in python is using the `socket` library:

```python
import socket

def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False
```
For an IPv6 address, use `socket.inet_pton` instead of `socket.inet_aton`.

### Step 2: Sanitize HTTP Headers
Ensure to sanitize HTTP headers to prevent IP spoofing. In JavaScript:

```javascript
function sanitizeHeaders(req, res, next) {
    req.ip = req.headers['x-forwarded-for'] || 
             req.connection.remoteAddress;
    if(validate_ip(req.ip)) {
      next();
    } else {
      res.status(400).send('Invalid IP Address');
    }
}
```
Use this middleware in your application to sanitize incoming requests.