

## Remediation Steps for Time Based NoSQL Injection
The Time based NoSQL Injection involves no-standard and tricky approach to perform SQL Injection. Any interaction with the database should be done with validated, escaped, and/or safe parameters to avoid injection.

### Step 1: Validate Input
Input validation can serve as the first line of defense. Only accept expected form of user input.

```python
from werkzeug.datastructures import MultiDict
from wtforms import Form, BooleanField, StringField
from wtforms.validators import DataRequired

class MyForm(Form):
    name = StringField('name', validators=[DataRequired()])

form = MyForm(MultiDict({'name': 'John Doe'}))
```

### Step 2: Use Parameterized Queries / Prepared Statements
Parameterized queries include placeholders that are replaced with user input when the query is run. This helps ensure that user input cannot interfere with the query structure.

```javascript
// Using MongoDB as an example
const MongoClient = require('mongodb').MongoClient;
const uri = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/test?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true });
client.connect(err => {
  const collection = client.db("test").collection("devices");
  collection.findOne({name: userInput}) // Insecure
  collection.findOne({name: {$eq: userInput}}) // Secure
  client.close();
});
```

### Step 3: Use Limit and Whitelisting Characters
By limiting the field inputs and character types, we can further secure our application from NoSQL Injection. This will prevent special characters that are part of the query language.

```python
import re
name = input()
if not re.match("^[A-Za-z]*$", name):
    print("Invalid input!")
```

### Step 4: Use Web Application Firewalls
A web application firewall can help filter out malicious data and can be another effective tool against SQL injection.

Example, ModSecurity is an open source WAF which have rules to mitigate SQL injection.


### Step 5: Appropriate Error Handling
Never display detailed error messages to users, as they can leak important data or database structure which hackers can use for further attacks.

```python
try:
    perform_database_operations()
except Exception as e:
    log_error(e)
    display_generic_error_message()
```