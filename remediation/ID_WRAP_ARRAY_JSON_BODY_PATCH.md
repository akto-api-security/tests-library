

## Remediation Steps for BOLA via JSON Param Array Manipulation with PATCH/PUT methods
BOLA, or Broken Object Level Authorization, using JSON parameter array manipulation is a critical security issue. If unchecked, attackers can exploit this vulnerability to gain unauthorized access. Here are the steps to safeguard your API from this vulnerability.

### Step 1: Validate and Sanitize Input
Ensure that all inputs are validated, sanitized, and can only be of the expected type. If an incoming request includes an array where it should not, return a '400 Bad Request' response.
```javascript
// Assume 'express' and 'body-parser' are already installed
const express = require('express');
const app = express();
app.use(express.json());

app.put('/api/resource/:id', (req, res) => {
  if (Array.isArray(req.body)){
    res.status(400).json({error: "Bad Request"});
    return;
  }
  // ... your code here ...
});
```
### Step 2: Implement Proper Authorization Checks
Implement proper and strict checks for every request to avoid unauthorised data access. Make sure that users can only access objects that they are authorized to access.
```javascript
app.put('/api/resource/:id', (req, res) => {
  // ... input validation ...

  // You should retrieve user and resource from your authentication middleware/context and your storage
  const user = retrieveUserFromContext();
  const resource = retrieveResourceFromId(req.params.id);
  
  if (user.id !== resource.ownerId){
    res.status(403).json({error: "Forbidden"});
    return;
  }
  // ... your code here ...
});
```
