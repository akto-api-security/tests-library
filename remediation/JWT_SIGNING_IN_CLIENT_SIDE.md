

## Remediation Steps for JWT Signing in Client Side

JWT (JSON Web Token) signing in the client side is a severe security issue. It can expose the app to numerous types of attacks, including the interception of unencrypted tokens. The client-side JWT signing should not be allowed for security reasons.

### Step 1: Move JWT Signing to the Server Side

In order to fix this vulnerability, JWT signing should be done on the server side, not on the client side. Here's a simple example:

```javascript
const express = require("express");
const jwt = require("jsonwebtoken");
const app = express();
app.post("/authenticate", (req, res) => {
    const user = req.body; // assuming you are using body-parser JSON
    const token = jwt.sign(user, 'your-secret-key', { expiresIn: '1h' });
    res.json({ token: token });
});
app.listen(3000);
```
In the example above, `/authenticate` endpoint is used to generate a new token for each user.

### Step 2: Use HTTPS for Safe Transfer

Even after moving JWT signing to the server side, token can still be intercepted during the transfer between the client and the server. To prevent this, HTTPS should be used:

```javascript
const https = require('https');
const fs = require('fs');

const options = {
  key: fs.readFileSync('test/fixtures/keys/agent2-key.pem'),
  cert: fs.readFileSync('test/fixtures/keys/agent2-cert.pem')
};

app.createServer(options, (req, res) => {
  res.writeHead(200);
  res.end("hello world\n");
}).listen(8000);
```
In the above example with NodeJS, HTTPS server is created to ensure that JWT is securely sent to the client.

### Step 3: Include JWT in HTTP Authorization Header

To secure the JWT token in each request after login, attach it in the HTTP Authorization header. 

```javascript
fetch('/api/protected', {
  method: 'GET',
  headers: {
    'Authorization': 'Bearer ' + token
  }
});
```
In the example above, the token is attached to the 'Authorization' header in every request.