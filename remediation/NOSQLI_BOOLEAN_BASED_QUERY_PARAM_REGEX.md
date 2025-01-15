# Remediation for NOSQLI_BOOLEAN_BASED_QUERY_PARAM_REGEX

## Remediation Steps for Boolean Based NoSQL Injection
NoSQL injection refers to manipulation of query parameters that exploits an improperly secured NoSQL database. This can allow unauthorized access to sensitive information. Here we give the necessary steps to prevent such NoSQL injections when working with regular expressions (Regex).

### Python Flask sample application remediation steps from MongoDB NoSQL Injection:

### Step 1: Validate and sanitize user input

Do not trust user input, especially when it's used to create a database query. Sanitize and validate all user inputs. Utilize built-in functions to escape special characters:

```python
from werkzeug.security import safe_str_cmp

def sanitize(input):
    return safe_str_cmp(input, input)
```

### Step 2: Use parameterized queries or prepared statements

Instead of creating dynamic queries, use parameterized queries or prepared statements:

```python
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

@app.route("/user/<user_id>")
def user_profile(user_id):
    user = mongo.db.users.find_one_or_404({"_id": ObjectId(user_id)})
    return render_template("user.html", user=user)
```

### Step 3: Implement appropriate permissions

Use the principle of least privilege to restrict access rights for users to the bare minimum permissions they need to perform their work:

```python
db.createUser(
  {
    user: "safeUser",
    pwd: "password",
    roles: [ { role: "read", db: "database" } ]
  }
)
```