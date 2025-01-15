# Remediation for UNION_INLINE_COMMENT_BASED_MYSQLI

## Remediation Steps for Union based SQL Injection with Inline Comments for MySQL on Login Endpoints

Union based SQL injection is a dangerous security issue. Such attacks allow malicious parties to manipulate an application's database queries. This can compromise sensitive data, corrupt the data, or even give full control of the server to an attacker.

### Step 1: Use Prepared Statements (Parameterized Queries)

Most programming languages offer a way to use prepared statements or parameterized queries to protect from SQL Injection. Here's an example in Python using MySQL Connector.

```python
import mysql.connector

cnx = mysql.connector.connect(user='username', password='password',
                              host='127.0.0.1',
                              database='database_name')

cursor = cnx.cursor(prepared=True)

query = "SELECT username, password FROM users WHERE username=%s AND password=%s"
values = ('user1', 'password1')

cursor.execute(query, values)

data = cursor.fetchall()
```

### Step 2: Use Stored Procedures 

Stored procedures also offer similar protection. Here's an example in PHP:

```php
$mysqli = new mysqli("localhost", "user", "password", "database");
$stmt = $mysqli->prepare("CALL sp_login(?,?)");
$stmt->bind_param('ss', $username, $password);
$stmt->execute();
$result_set = $stmt->get_result();
```

### Step 3: Input Validation

Always validate inputs that are being passed into SQL queries. Check for data type, length, format, and range. 

Here's an example of input validation using Python:

```python
def is_valid_username(username):
    return username.isalnum()

def is_valid_password(password):
    return len(password) >= 8
```

### Step 4: Least Privilege Principle 

Ensure that the database user used by the application has the least amount of privilege necessary. The user should only be able to execute the necessary commands and access the necessary tables.