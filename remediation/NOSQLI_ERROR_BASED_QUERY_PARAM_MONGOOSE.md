# Remediation for NOSQLI_ERROR_BASED_QUERY_PARAM_MONGOOSE

## Remediation Steps for Error Based NoSQL Injection in Mongoose Query Parameters

NoSQL Injection errors occur when untrusted user-input affects database query logic. In Mongoose, a popular ODM library for MongoDB, there is a risk that a malicious actor could inject unwanted commands or data into the NoSQL database. Here are the steps to fix this issue:

### Step 1: Data Validation and Input Sanitization
Ensure that you correctly validate and sanitize incoming requests. One way of doing this is by using libraries such as `express-validator` or `joi`. Below is an example of data validation using `express-validator`

```javascript
const { body, validationResult } = require('express-validator');

router.post('/user',
  // Use array of validation middlewares
  [
    body('username').isLength({ min: 5 }),
    body('password').isLength({ min: 5 })
  ], 
  (req, res) => {
    // Check for validation errors
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }
    
    // Now proceed with creating user
    //...
  });
```

### Step 2: Mongoose Schema Validation
Use mongoose schemas to ensure that input data fits into the expected format. Mongoose schema uses built-in validators to verify the data before saving it to the database

```javascript
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const userSchema = new Schema({
  username: {
    type: String,
    required: true,
    minlength: 5
  },
  password: {
    type: String,
    required: true,
    minlength: 5
  }
});

module.exports = mongoose.model('User', userSchema);
```

### Step 3: Parameterized Queries 
Use Parameterized queries. This essentially allows the database to differentiate between code and data regardless of what user input is supplied.

In Mongoose, you can setup query parameters like so:

```javascript
const username = req.body.username; // assuming `username` is coming from client
const query = { username: new RegExp('^' + username + '$', "i") };

User.find(query, function(error, users) { /* Your callback function here */ });
```