# Remediation for HEADER_ALL_KEYS_INVALID_VALUES

## Remediation Steps for Header All Keys Invalid Values
This security issue relates to the inability to process requests where all header keys contain invalid values. These requests could potentially lead to erratic system behavior and security vulnerabilities.

### Step 1: Validate Header Inputs
You need to validate that the headers attached with the requests have acceptable keys and values. This can be done at the server entry point or within the middleware of your API. Here's an example in Node.js with the Express.js framework.

```javascript
app.use(function(req, res, next){
    for(let key in req.headers){
        if(!isValid(key, req.headers[key])){
            return res.status(400).json({ message: "Invalid header key/values" });
        }
    }
    next();
});

function isValid(key, value){
    // Add your validation logic here, for example:
    return typeof value === 'string';
}
```

### Step 2: Enable Input Sanitization
Sanitize header key/values to mitigate attacks. Here's an example of how to sanitize your inputs using validator.js library.

```javascript
const validator = require('validator');

app.use(function(req, res, next){
    for(let key in req.headers){
        req.headers[key] = validator.escape(req.headers[key]);
    }
    next();
});
```

### Step 3: Adding Proper Error Handling
Make sure to return proper error message when encountering invalid header key/value element. 

```javascript
app.use(function(req, res, next){
    for(let key in req.headers){
        if(!isValid(key, req.headers[key])){
            return res.status(400).json({ message: "Invalid header key/value detected" });
        }
    }
    next();
});
```