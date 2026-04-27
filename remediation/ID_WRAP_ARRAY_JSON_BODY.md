

## Remediation Steps for BOLA: Turning JSON Param into Array for Unauthorized Access

BOLA, or Broken Object Level Authorization, exploits occur when an application fails to verify the user's access rights before granting access to data. In the case of turning a JSON parameter into an array for unauthorized access, we can take certain remediation steps.

### Step 1: Implement Proper Access Control
Firstly, make sure that appropriate access control methods are in place. Here's an example in Node.js, using Access Control List (ACL).

```javascript
const AccessControl = require("accesscontrol");
const ac = new AccessControl();

ac.grant('guest')                    
    .readOwn('profile')               
    .updateOwn('profile')              
ac.grant('admin')                     
    .extend('guest')                  
    .readAny('profile')                
    .deleteAny('profile')             
```
In this example, the 'guest' role can only read and update its own profile while the 'admin' role can read and delete any profile.

### Step 2: Validate Input
Never trust user input. Always validate and sanitize user input to make sure it cannot manipulate the behaviour of the system. Here is an example using express-validator middleware in a Node.js express application:

```javascript
const { body } = require('express-validator/check');

app.post('/', [
  body('jsonParam').isArray()
], (req, res, next) => {
  // handle request
});
```
In this example, the JSON parameter 'jsonParam' is checked to ensure it's an array.