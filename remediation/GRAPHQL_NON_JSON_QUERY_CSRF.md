# Remediation for GRAPHQL_NON_JSON_QUERY_CSRF

## Remediation Steps for CSRF test with Non-JSON Queries in HTTP GET Query Parameters in GraphQL

Cross-site request forgery (CSRF) is a type of malicious exploit of a website where unauthorized commands are transmitted from a user that the web application trusts.

### Step 1: Set CSRF Token

Set a CSRF token in your web application. This can be done in multiple ways but here is one example in Node.js with the csurf module.

```js
var express = require('express')
var cookieParser = require('cookie-parser')
var csrf = require('csurf')

var app = express()
app.use(cookieParser())

// set csrf protection
var csrfProtection = csrf({ cookie: true })
app.get('/form', csrfProtection, function(req, res) {
  // pass the csrfToken to the view
  res.render('send', { csrfToken: req.csrfToken() })
})

```
### Step 2: Validate CSRF Token

Check for the CSRF token in every server mutation. Below is an example on how to validate it within an Express.js server using csurf.

```js
app.post('/process', parseForm, csrfProtection, function(req, res) {
  res.send('CSRF token validated, data processed')
})
```

### Step 3: Use HTTP POST for dangerous actions

Always use HTTP POST for any state-changing operation. GraphQL should not be making state changes with HTTP GET.

```js
fetch('http://example.com/graphql', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
  body: JSON.stringify({query: "{ hello }"})
})
```

### Step 4: Check Origin/Referer headers

If feasible, add an additional layer of security by checking the Origin/Referer headers.

```js
app.use((req, res, next) => {
  const requestOrigin = req.headers.origin;
  const allowedOrigins = ['http://localhost:3000', 'http://example.com'];

  if (allowedOrigins.includes(requestOrigin)) {
    next();
  } else {
    res.sendStatus(403);
  }
});
```