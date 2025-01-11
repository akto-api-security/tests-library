# Remediation for NOSQLI_ERROR_BASED_PARAM_MONGO_SPECIAL_CHARACTERS

## Remediation Steps for NoSQL Injection Error in JSON Body Parameters for Mongo

NoSQL injection is a security issue where an attacker is able to inject code into the NoSQL query by manipulating the application's input data. The attacker can potentially read, update and delete all the data in the database or execute arbitrary code on the server. 

### Step 1: Sanitize user input
Always sanitize user inputs to ensure that malicious code isn't pushed into the database. This can be done using a function that filters out characters or strings that are commonly used in NoSQL injection attacks. Here is an example in JavaScript:

```javascript
function sanitize(input) {
    return input.replace(/[^\w\s]/gi, '');
}
```

### Step 2: Use parameterized queries
Parameterized queries can be used to prevent NoSQL injection. With parameterized queries, the query pattern is defined and then the parameters are passed separately. Here is an example in JavaScript:

```javascript
var userid = sanitize(req.body.userid);  
collection.find({"userid" : userid});
```

### Step 3: Use a mature ORM/ODM or a database library
Using a mature library or ORM/ODM can provide another layer of security against NoSQL injection. These tools often come with built-in support for parameterized queries and data sanitization.

For example, in JavaScript, you can use mongoose which is a MongoDB object modeling tool.

```javascript
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/test');

var userSchema = mongoose.Schema({
    userid: String
});
var User = mongoose.model('User', userSchema);

User.find({userid: sanitize(req.body.userid)}, function(err, user) {
  if (err) throw err;
  console.log(user);
});
```


### Step 4: Enable authentication in your MongoDB Database
Authentication controls who can access the MongoDB database.

Edit your `mongodb-conf` file usually located at /etc/mongod.conf

Include or uncomment this portion

```bash
security:
  authorization: "enabled"
```

Then, restart your mongodb service.

```bash
service mongod restart
```