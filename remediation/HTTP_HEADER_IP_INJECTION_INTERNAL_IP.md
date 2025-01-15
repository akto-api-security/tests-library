# Remediation for HTTP_HEADER_IP_INJECTION_INTERNAL_IP

## Remediation Steps for Internal IP Injection in HTTP Headers
An internal IP injection in HTTP headers can expose internal network details to potential attackers. This vulnerability can be exploited to perform advanced attacks such as Server Side Request Forgery (SSRF). The steps below outline how to remediate this vulnerability.

### Step 1: Use a Middleware to Scrub IP Addresses from Headers
You should use a middleware to prevent the disclosure of internal IP information in HTTP headers. This middleware should check and remove any literal IP addresses from HTTP headers. Below is an example in Node.js using Express middleware. 

```javascript
var app = require('express')();

app.use(function(req, res, next) {
    for (var key in req.headers) {
        if (req.headers[key].match(/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/g)) {
            delete req.headers[key];
        }
    }
    next();
});
```

### Step 2: Always Use a Proxy
The use of a proxy server can prevent revealing internal IP addresses by only forwarding traffic, hiding the details of the private network. The following nginx configuration can be used to setup a reverse proxy. 

```bash
server {
    listen 80;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```