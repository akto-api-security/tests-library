

## Remediation Steps for Denial of Service Test with Large MP4 File

Denial of Service (DoS) attacks performed with large files such as MP4 can cause severe issues, depleting resources and affecting your service availability. In response to such events, implement steps to properly validate file uploads and limit their size.

### Step 1: Implement input validation

Before any file is uploaded, make sure it passes through input validation checks. Here is an example using Python:

```python
import os

def validate_file(file):
    if not file:
        raise ValueError("No file provided")
    if file.size > MAX_FILE_SIZE:
        raise ValueError("File size exceeds limit")
    if not file.content_type in ["video/mp4"]:
        raise ValueError("Invalid file type")
    return True
```
Replace `MAX_FILE_SIZE` with the maximum file size you wish to allow (in bytes).

### Step 2: Limit file size

You should also limit the acceptable file size that can be uploaded to the server. 

In NGINX:

```nginx
http {
    ...
    client_max_body_size 10M; #limits the client request body size to 10 megabytes
    ...
}
```

### Step 3: Rate Limiting
Rate limiting restricts the number of requests a client can make to your server within a specified time period.

In Node.js using `express-rate-limit`:

```javascript
const rateLimit = require("express-rate-limit");

app.use(rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
 }));
```
### Step 4: Load Balancing 

Deploy a load balancer to distribute workload across multiple servers, thereby mitigating the risk of a single server being overwhelmed. 

Using HAProxy:

```bash
global
    log /dev/log    local0
    log /dev/log    local1 notice
    daemon

defaults
    log global
    mode    http
    option  httplog
    option  dontlognull
        timeout connect 5000
        timeout client  50000
        timeout server  50000

frontend http_front
   bind *:80
   stats uri /haproxy?stats
   default_backend http_back

backend http_back
   balance roundrobin
   server server1 10.0.0.1:80 check
   server server2 10.0.0.2:80 check
```
This setup will distribute traffic equally to the servers `server1` and `server2`.

These suggestions will defend your server against DoS attacks posed due to large file uploads. Please adapt these methods according to your specific environment and needs.