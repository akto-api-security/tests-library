# Remediation for SSRF_ON_PDF_UPLOAD_AZURE_REDIRECT

## Remediation Steps for Azure SSRF Exposure

Sensitive Azure details could be exposed via Server Side Request Forgery (SSRF) attack, leading to the leakage of Azure secrets. Here are the remediation steps to prevent such a scenario.

### Step 1: Disable Redirects in Servers

By disabling all server-side redirects as a HTTP response status, you can prevent an attacker from redirecting users to an undesired location. Most server frameworks provide a setting or configuration options to disable redirects. Here's an example in NodeJS using Express framework:

```javascript
const express = require('express');
const app = express();

app.get('/path', function(req, res, next) {
  var url = req.query.url;
  if(!isSafeUrl(url)) {
    // if the url is not safe, respond with an error
    res.status(400).send('Invalid request');
    return;
  }
  
  // else continue with the request
  next();
});
```
### Step 2: Implement URL validation

By validating the URL before fetching it, you can prevent fetching from undesired locations. The validation should filter out private IP addresses and localhost:

```javascript
function isSafeUrl(url) {
  const ipAddress = urlParser.parse(url).hostname;
  return !ip.isPrivate(ipAddress);
}
```
### Step 3: Limit or restrict outbound requests

By limiting or restricting outbound requests from your server, you can minimize the attack surface for SSRF attacks. This can be done through firewall rules. Here's an example using Linux iptables utility:

```bash
iptables -A OUTPUT -p tcp -d 0.0.0.0/0 -j DROP
iptables -A OUTPUT -p udp -d 0.0.0.0/0 -j DROP
```