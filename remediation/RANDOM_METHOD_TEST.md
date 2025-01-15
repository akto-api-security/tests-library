# Remediation for RANDOM_METHOD_TEST

## Remediation Steps for Access Control Bypass

Access Control Bypass by changing the request method to an arbitrary value is a significant security issue. This allows an attacker to access components that should be restricted. The attacker can bypass the intended access control by changing the HTTP request method. 

### Step 1: HTTP Method Restriction in Server Side
The server-side script needs to check the request method before proceeding with the request. This can be in any common backend language. 

Here is an example using Node.js's Express.js:

```javascript
const express = require('express')
const app = express()

app.post('/secured-endpoint', (req, res) => {
  // Only POST method will be able to access this endpoint
  res.send('Secured endpoint accessed.')
})

app.listen(3000, () => {
  console.log('Server is running on port 3000.')
})
```

### Step 2: Include Request Method in Access Control Policies

Ensure your access control policies include the HTTP request method. Any request with an unexpected method should not be allowed to access the resource.

Below is an example configuration for a route in Apache via `.htaccess`:

```bash
<LimitExcept GET POST>
    Deny from all
</LimitExcept>
```

This directive will deny any request methods that are not `GET` or `POST` for the containing location.