# Remediation for NODEJS_DIRECTORY_TRAVERSAL

## Remediation Steps for Node.js Local File Inclusion

Local File Inclusion (LFI) is a serious security issue in Node.js applications. By exploiting LFI vulnerabilities, an attacker may gain unauthorized access to sensitive data stored on the server.
Below are the steps to remediate this issue.

### Step 1: Validate User Inputs

Untrusted inputs can lead to LFI vulnerabilities. Therefore, user inputs should be validated before processing. Here's an example using express-validator in a Node.js/Express application:

```javascript
const { check, validationResult } = require('express-validator');

app.post('/user', [
  // username must be an email
  check('username').isEmail(),
  // password must be at least 5 chars long
  check('password').isLength({ min: 5 })
], (req, res) => {
  // Finds the validation errors in this request and wraps them in an object with handy functions
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }
  
  // ...proceed with processing if no errors.
});
```
### Step 2: Limit File Access

Make sure your application only has access to the files it needs in order to perform its function. Use access control lists (ACLs) to limit the files that can be accessed in the file system.

```bash
sudo setfacl -m u:<user>:r <filename>
```

### Step 3: Use Safe File Path Methods

Avoid using file paths provided by users. Instead use safe methods to resolve file paths and ensure users can not access files outside the designated directories.

```javascript
var express = require('express');
var path = require('path');
var app = express();

app.get('/:user', function(req, res) {
  res.sendFile(path.resolve(__dirname + '/../users/' + req.params.user + '/data.txt'));
});
```