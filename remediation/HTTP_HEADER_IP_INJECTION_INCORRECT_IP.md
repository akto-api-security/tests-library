# Remediation for HTTP_HEADER_IP_INJECTION_INCORRECT_IP

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

### Step 3: Regular Monitoring and Logging
Monitor logs and perform regular audits to ensure no unauthorized requests are processed. A common way to log requests in Node.js applications is using morgan:

```javascript
const morgan = require('morgan');
app.use(morgan('combined'));
```
This logs requests in Apache combined log output format, which includes the client IP among other information.

Note: Remember to replace `validate_ip()` with the actual method to validate IP addresses in your own application. 

Practice diligently these three steps and be privy to the fact that security is an ongoing process and not a one-time task. Always keep your applications up-to-date with latest security patches.