# Remediation for NOSQLI_BOOLEAN_BASED_JSON_PARAM_JS

## Remediation Steps for Boolean Based NoSQL Injection

A NoSQL Injection attack targets the data integrity in NoSQL-based applications where the malicious code is injected into a query that is then passed to the database. It can be used to execute arbitrary commands on the database.

### Step 1: Use Input Validation

For JavaScript, this means you should be properly validating input on both the client and server-side using packages like [Express Validator](https://www.npmjs.com/package/express-validator) for node.js server or simply with JavaScript built-in function to check if variable is not `undefined` nor `null`.

```javascript
var data = req.body.data;

if (typeof data === "undefined" || data === null){
    throw new Error("Invalid input");
}
```

### Step 2: Always use Parameterized Queries

For Node.js with mongoDB, you can use the mongodb driver's methods to help ensure parameters are properly escaped. Find a simple example below:

```javascript
const MongoClient = require('mongodb').MongoClient;
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

client.connect(err => {
  const collection = client.db("test").collection("devices");
  
  collection.find({ name: req.body.data}).toArray(function(err, result) {
    if (err) throw err;
    console.log(result);
    client.close();
  });
});
```

### Step 3: Limit Database Permissions

For most applications, read, insert, update, and delete permissions are all that are needed. The following command can be used to limit permissions:

```bash
db.grantRolesToUser( "<username>",[{ role: "readWrite", db: "<database>" }] )
```

### Step 4: Regular Update and Monitor

Regularly update your packages and databases to the latest versions, as they may include essential security patches. Regular audits to your code and monitor your applications to ensure no invalid operations.

```bash
npm audit
npm update
```