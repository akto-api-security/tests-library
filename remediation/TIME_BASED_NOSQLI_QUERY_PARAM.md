

## Remediation Steps for Time-Based NoSQL Injection Test for Query Parameters with Javascript

NoSQL Injection is a critical security issue in a NoSQL Database environment. If not properly mitigated, attackers can use this vulnerability to retrieve, manipulate or delete data from your database.

Here are the steps to fix a Time-Based NoSQL Injection in Query Parameters.

### Step 1: Use Parameterized Queries 

Parameterized queries make sure the data is sent in a separate path than the actual SQL command in your application code logic. Here is a code snippet that demonstrates creating a safer query in Node.js with MongoDB.

```javascript
function getUser(username, callback) {
   var collection = db.collection('users');
   collection.findOne({ username: username }, function(err, user) {
      callback(err, user);
   });
}
```

### Step 2: Input Validation

Input validation is necessary to ensure that application behaves as expected with certain input. This can be done using express-validator middleware in Express.js as follows:

```javascript
const { body } = require('express-validator');
app.post('/user', [
  body('username').isLength({ min: 5 })
], (req, res) => {
  // ...
});
```

### Step 3: Limiting Database Permissions

Make sure the application account has only the least necessary database permissions to prevent malicious activities even if an attacker successfully exploits a vulnerability.

Sharing an example of creating a database user with read and write access to the data in a `test` database only:

```bash
db.createUser(
  {
    user: "myTester",
    pwd: "xyz123",
    roles: [ { role: "readWrite", db: "test" } ]
  }
);
```