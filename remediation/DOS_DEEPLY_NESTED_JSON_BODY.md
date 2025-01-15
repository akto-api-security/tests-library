# Remediation for DOS_DEEPLY_NESTED_JSON_BODY

## Remediation Steps for Denial of Service through Deeply Nested JSON Body

A Denial of Service (DoS) attack through a deeply nested JSON body is a significant security issue. An attacker can send a very deeply nested JSON body to cause the server to consume all the resources while trying to parse it, resulting in other legit requests being dropped and causing a denial of service. This guide will provide steps to prevent such DoS attacks in a Node.js application.

### Step 1: Limit Body Parser Size
```javascript
    var express = require('express');
    var bodyParser = require('body-parser');

    var app = express();
    // Limit request to 1mb
    app.use(bodyParser.json({ limit: '1mb' })); 
    app.use(bodyParser.urlencoded({ limit: '1mb', extended: true }));
```
In this step, we restrict the size of JSON request body using body parser's limit option. This will prevent large JSON payloads from being accepted by the server.

### Step 2 : Limit Depth of Nested Objects
```javascript
    app.use(bodyParser.json({ 
        limit: '1mb',
        depth: 5  // Limit depth of nested objects
    })); 
    app.use(bodyParser.urlencoded({ 
        limit: '1mb',
        extended: true, 
        parameterLimit: 5000 // Limit number of parameter fields
    }));
```
Most of the JSON parsing libraries, including body-parser for express.js provide the option to limit the depth of nested objects. We limit the depth to 5 which should be more than enough for common APIs.

### Step 3 : Implement Rate Limiting
```javascript
    var rateLimit = require("express-rate-limit");
    var limiter = rateLimit({
        windowMs: 15 * 60 * 1000, // 15 minutes
        max: 100 // limit each IP to 100 requests per windowMs
    });

    //  apply limiter to all requests
    app.use(limiter);
```
Rate limiting restricts the number of requests a client can make to the API within a certain period. Here we limit the number of requests to 100 every 15 minutes.