# Remediation for DUMMY_TRANSFER_ENCODING_HEADER

## Remediation Steps for Dummy Transfer-Encoding Header
The dummy Transfer-Encoding header is a well-known security issue. An attacker may manipulate the header of an HTTP request by leveraging the "Transfer-Encoding: chunked" technique to bypass security mechanisms or create potential denial-of-service threats.

### Step 1: Validate Headers
You must ensure that your application validates the headers of every request to ensure that no unauthorized headers, such as a dummy Transfer-Encoding header, are being sent.

If you are using Node.js, use the `http` package's `request` method to validate headers.
```javascript
let http = require('http');

http.createServer((req, res) => {
  if(req.headers['transfer-encoding']){
    res.writeHead(400, {'Content-Type': 'text/plain'});
    res.end('Invalid Header Detected');
  } else {
    //your normal logic.
  }
}).listen(8080);
```
In the code above, if a 'transfer-encoding' header is detected, the server responds with a HTTP 400 status code and ends the connection. 

### Step 2: Implement Firewall Rules
Make sure that your firewall is configured to block HTTP requests containing illegal headers. 

### Step 3: Update Application or Web Server

Make sure to keep your application, web server and all related components up to date with the latest security patches and updates. 

It is worth noting that some web servers have built-in solutions to this problem, which can be utilized by simply updating to the latest version.

## Regular Security Audit
It's very crucial to periodically perform security audits of your application and infrastructure to detect and correct any security weakness promptly. This would help avert potential security threats. Also, subscribing to all related application, web server and OS-level security bulletins or newsletters could help you stay updated with the latest security concerns and patches. 