# Remediation for ID_WRAP_ARRAY_JSON_BODY_INTEGER_ID_DELETE

## Remediation Steps for BOLA: Turning JSON Param into Integer Array 

Broken Object Level Authorization (BOLA) is a critical API vulnerability where the attacker can manipulate object identifiers to gain unauthorized access to data. A common manifestation of BOLA can occur when a JSON parameter is turned into an Integer array leading to unauthorized DELETE method APIs. Here's how we can prevent that:

### Step 1: Validate User Input
It’s important to validate any user provided input in your code. Avoid assuming the client will send correctly formatted JSON parameters, check everything.

For example, in Python, use the `isinstance()` function:
```python
def validate_input(input):
    if isinstance(input, int):
        return True
    else:
        return False
```

### Step 2: Use Proper Authentication & Authorization Checks
Implement strict access controls and ensure only authorized users can access specific API end points.

In Node.js with Express.js, using middleware like passport.js could look like this:

```javascript
var express = require('express');
var passport = require('passport');
var router = express.Router();

router.delete('/api/delete', passport.authenticate('jwt', { session: false }), function(req, res){
    // Perform deletion
});
```

### Step 3: Limit API Response Data
Limit the amount of data returned by the API to only what is necessary, thus reducing the chance of exposing sensitive information.

### Step 4: Regular Audit and Update
Your dev team should regularly audit their code for security vulnerabilities, make updates as needed and stay aware of the latest security standards and best practices.

```bash
# Update your package dependencies
npm update
``` 
Remember, static code analysis tools and security audits are an essential part of the development cycle. Regular updates and patches help to keep your application secure.