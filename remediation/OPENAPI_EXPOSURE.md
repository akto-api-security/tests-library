# Remediation for OPENAPI_EXPOSURE

## Remediation Steps for OpenAPI Documentation Exposure
OpenAPI Documentation Exposure can expose details about the underlying software architecture of an application. An attacker may use this information to identify potential vulnerabilities and craft specialized attacks.

### Step 1: Restrict Access to OpenAPI Documentation

The first step is to limit the access of your OpenAPI documentation to only the trusted users. This prevents unauthorized users from gaining information about your API's structure.

```javascript
const express = require('express');
const swaggerUi = require('swagger-ui-express');
const swaggerDocument = require('./swagger.json');

const app = express();

app.use('/api-docs', function (req, res, next) {
  // perform authentication
  // if authenticated call next()
  // else res.status(403).send('Forbidden');
}, swaggerUi.serve, swaggerUi.setup(swaggerDocument));

app.listen(3000);
```

### Step 2: Remove sensitive data from the API spec

Review your OpenAPI spec (Swagger doc) and remove any information that can be considered sensitive or would not be beneficial for an end user.

```yaml
# Example of avoiding sensitive data
swagger: '2.0'
info:
  title: Sample API
  description: API description in markdown.
```
### Step 3: Implement Rate Limiting 

By limiting the frequency of calls to your documentation end point, you can protect against iteratively exploring your API's structure and overwhelming your server with requests. The following example uses Express Rate Limit to limit documentation endpoints to 100 requests per hour.

```javascript
const swaggerUi = require('swagger-ui-express');
const swaggerDocument = require('./swagger.json');
const express = require('express');
const rateLimit = require("express-rate-limit");

const limiter = rateLimit({
  windowMs: 60 * 60 * 1000, // 1 hour
  max: 100 // limit number of requests per windowMs
});

const app = express();
app.use('/api-docs', limiter, swaggerUi.serve, swaggerUi.setup(swaggerDocument));
app.listen(3000);
```
### Step 4: Regular Review of OpenAPI Documentation
Constantly review your OpenAPI documentation. Be sure to remove old and unused APIs which can become potential security loopholes.