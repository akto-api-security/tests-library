

## Remediation Steps for Union based SQL Injection Test with XSS for GET method APIs

SQL injection is a common web-based exploit where an attacker can submit SQL commands from a web form to affect database operations. Cross-site scripting (XSS) is a type of computer security vulnerability that allows malicious scripts to be included in web pages viewed by other users.

### Step 1: Use Parameterized Queries

By using parameterized queries (also called prepared statements), you prevent the SQL injection vulnerability since it will not execute a mix of commands and data.

For instance, in Java, you can remediate the vulnerability as follows:

```java
String selectSQL = "SELECT user FROM users WHERE id = ? ";
PreparedStatement preparedStatement = dbConnection.prepareStatement(selectSQL);
preparedStatement.setInt(1, 1001);
ResultSet rs = preparedStatement.executeQuery(selectSQL);
```

### Step 2: Use ORM Frameworks

ORM (Object Relational Mapping) frameworks create a virtual object database that you can use from within your programming language. 

```python
# Using SQLAlchemy ORM in Python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
conn = engine.connect()
conn.execute("select user from users where id=?", (1001,))
```

### Step 3: Employ Proper Error Handling

Avoid leaking server-side details to the end-user, which might help an attacker.

```java
try {
  // some code
} catch (SQLException ex) {
  logger.log(Level.SEVERE, "an SQL exception was thrown", ex);
  return "error";
}
```

### Step 4: Implement Output Encoding/escaping When Using Untrusted Data

To prevent XSS attacks, you need to encode/escape the output.

For instance, in PHP you can remediate the vulnerability as follows:

```php
echo htmlspecialchars($untrustedData, ENT_QUOTES, 'UTF-8');
```

### Step 5: Use Security Headers

By setting HTTP security headers like Content-Security-Policy (CSP), you can prevent a broad set of XSS attacks.

```python
# Python-Flask example
@app.after_request
def apply_csp(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response
```