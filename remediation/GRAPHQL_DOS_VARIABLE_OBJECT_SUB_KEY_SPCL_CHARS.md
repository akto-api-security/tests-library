# Remediation for GRAPHQL_DOS_VARIABLE_OBJECT_SUB_KEY_SPCL_CHARS

## Remediation Steps for Denial of Service Tests on GraphQL API with Special Characters in Variable's Object Key Field
Highlighted below are proposed steps to prevent the vulnerability of Denial of Service (DoS) attacks on a GraphQL API by introducing special characters in a variable's key field. A malformed key field can cause the API server to crash, creating a Denial of Service.
### Step 1: Implement Input Validation
Always validate user inputs before processing it. Reject any inputs that contain special characters and don't meet your field requirements. This can be done by using an input validator library or with a custom validator method. 

Here's an example in JavaScript using Express.js framework and the express-validator library:
```JavaScript
const {body, validationResult} = require('express-validator');

app.post('/graphqlRoute', [
    body('variableKey').isString().isLength({min:1}),
    (req, res, next) => {
        const errors = validationResult(req);
        if (!errors.isEmpty()) {
            return res.status(400).json({errors: errors.array()});
        }
        next();
    }
], (req, res) => {
    // Process request
})
```
### Step 2: Normalize or Sanitize Your Input
Sanitizing or normalizing your input means to make it conform to some rules or standards that you set. This will protect your API from accepting malicious data. 

```javascript
const sanitize = require('sanitize')();

app.post('/graphqlRoute', (req, res) => {
   const sanitizedKey = sanitize(req.body.variableKey);
   // Continue processing with sanitized data
})
```
### Step 3: Implement Rate Limiting
Rate limiting restricts the number of requests a client can make in a specified amount of time. It is an effective way to prevent DoS attacks.

Here's an example using the express-rate-limit library in an Express.js application:
```JavaScript
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100 // limit each IP to 100 requests per windowMs
});

// apply to all requests
app.use(limiter);
```