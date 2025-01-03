# Remediation for SSL_ENABLE_CHECK

## Remediation Steps for Bypass Authentication by Modifying URL to HTTP
Bypassing Authentication by modifying a URL from HTTPS to HTTP is a potential security vulnerability that may give a malicious user unauthorized access to sensitive pages or resources. The security of the site can be compromised if proper safety measures aren't implemented.

### Step 1: Force HTTPS
Implement HTTP Strict Transport Security (HSTS) on your server. This ensures that the browser will always use a secure HTTPS connection, even if an insecure HTTP link is requested.

In Node.js using express, it can be done as follows:

```javascript
const express = require('express');
const app = express();
const helmet = require('helmet');

app.use(helmet.hsts({
    maxAge: 60 * 60 * 24 * 365,  // One year in seconds
    includeSubDomains: true,  // Must be enabled to be approved on some browsers
    preload: true,
}));

app.listen(3000);
```

### Step 2: Implement Strict URL Validation
Check the URL on the server side before the user is redirected. This validation should return an error when HTTP is detected and redirect to HTTPS.

Here is a simple middleware in Node.js using Express that can be used to enforce HTTPS:

```javascript
app.use(function(req, res, next) {
  if (req.headers['x-forwarded-proto'] !== 'https') {
    return res.redirect(['https://', req.get('Host'), req.url].join(''));
  }
  return next();
});
```

### Step 3: Implement Input Sanitization
With strict input validation and sanitization measures in place, harmful data can be prevented from entering the system.

```javascript
const sanitizeString = (string) => {
    const sanitized = string.replace(/[^0-9a-z]/gi, '')
    return sanitized;
}

app.post('/user', function (req, res) {
    let { username } = req.body 
    username = sanitizeString(username)
    // rest of the logic
})
```

### Step 4: Regular Audit and Update
Regular software audits and updates help to ensure that all the latest security patches and updates have been applied to the software stack.

```bash
sudo apt-get update
sudo apt-get upgrade
```

Keep in mind that prevention is better than cure. It's proactive measures you set in place that keep your system safe from such vulnerabilities.