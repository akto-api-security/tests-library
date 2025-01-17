

## Remediation Steps for Swagger API Documentation Exposure
Swagger API documentation exposure can become a severe security issue. Unauthorized individuals might gain detailed knowledge about the structure of your API, which might be exploited for malicious activities.

### Step 1: Protect the API Documentation
In most cases, the API Documentation should not be publicly accessible. You can protect it by adding an authentication layer.
Here is an example using Node.js and Express:

```javascript
var express = require('express');
var swaggerUi = require('swagger-ui-express');
var swaggerDocument = require('./swagger.json');

var app = express();
 
app.use('/api-docs', 
  function (req, res, next) {
    // Add your authentication here
    // Example: 
    // if(token == "YourTokenValidation") next(); else res.status(403).send('Forbidden');
    next();
  },
  swaggerUi.serve, 
  swaggerUi.setup(swaggerDocument)
);
```

### Step 2: Limit the amount of detail exposed in error messages
Ensure that your Swagger API does not return too much information in error messages. This can be achieved by creating a custom error class in your application, and limiting the information returned in its 'toString()' method.

### Step 3: Regularly Monitor and Update
Ensure that your Swagger API is continuously maintained and updated with the latest patches. Additionally, perform periodic audits to verify the security of your documentation.

Always check that the information exposed through the API is designed to be public, and never unintentionally expose private details (API keys, passwords, etc.).

### Step 4: Consider using API Gateways

API Gateways provide several security layers such as API keys, rate limiting, and others. Example: Using AWS API Gateway.

```javascript
// In AWS Lambda function handler
exports.handler = async function(event, context) {
  // Add your API logic here
  return {"statusCode": 200, "body": JSON.stringify({"message": "Hello World"})};
}
```
Then in AWS API Gateway, you can set up your API to trigger this Lambda function and add API keys and rate limiting.

These steps should point you in the right direction to secure your Swagger API Documentation from exposure.