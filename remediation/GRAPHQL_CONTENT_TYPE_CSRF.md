

## Remediation Steps for CSRF Test with Content-Type Header in GraphQL

Cross-Site Request Forgery, or CSRF, is a serious security issue where an attacker can trick a victim into performing actions they didn't intend to do. GraphQL is not immune to this vulnerability. However, it can be mitigated effectively.

### Step 1: Validate Origin and Referer Headers
We need to validate the Origin and Referer headers for all incoming GraphQL requests. This technique will prevent most CSRF attacks as these headers cannot be changed by scripts.

```javascript
app.use('/graphql', (req, res, next) => {
    const requestOrigin = req.headers.origin;
    const requestReferer = req.headers.referer;
    const allowedOrigin = 'https://example.com'; // Replace with your website domain

    if (requestOrigin !== allowedOrigin || requestReferer !== allowedOrigin) {
        return res.status(403).json({ error: 'Invalid Origin or Referer.' });
    }

    next();
});
```

### Step 2: Implement CSRF Token
Server can provide a CSRF token after successful authentication, and then every subsequent request must include this token. This ensures that every request is made intentionally by a user and is not a CSRF attack.

Node.js express server example including csurf middleware:

```javascript
const express = require('express');
const cookieParser = require('cookie-parser');
const csrf = require('csurf');
const bodyParser = require('body-parser');

const csrfProtection = csrf({ cookie: true });
const app = express();

app.use(bodyParser.json());
app.use(cookieParser());
app.use(csrfProtection);

app.use((req, res, next) => {
  res.cookie('XSRF-TOKEN', req.csrfToken());
  next();
});
```
In this example, `res.cookie('XSRF-TOKEN', req.csrfToken());` line creates a new CSRF token and sets it in a cookie named `XSRF-TOKEN`.

For GraphQL requests from frontend, include the `XSRF-TOKEN` in request headers. 

```javascript
const csrfToken = document.cookie.split('XSRF-TOKEN=')[1];

fetch('/graphql', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'CSRF-TOKEN': csrfToken
  },
  body: JSON.stringify({ query: '' }) // your GraphQL query
});
```