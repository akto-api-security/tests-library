

## Remediation Steps for Union based SQL Injection Test with XSS

Union based SQL Injection and Cross-site Scripting (XSS) are serious security issues that can compromise the integrity and confidentiality of the data within a system. Prevention involves implementing secure coding practices, setting up robust input validation and sanitization, and using prepared statements in database queries.

### Step 1: Parameterize Queries/ Use Prepared Statements

Prepared statements ensure that the data passed into your SQL queries is treated as literal input, not part of the SQL query. This prevents an attacker from changing the structure of your SQL queries. Below is an example using PHP.

```php
$stmt = $pdo->prepare('SELECT * FROM employees WHERE name = :name');

$stmt->execute(['name' => $name]);

foreach ($stmt as $row) {
    // do something with $row
}
```

### Step 2: Implement Input Validation and Sanitizing

Ensure that all input from users is validated and sanitized before use. Users should only be able to input data that is valid for that particular context. Below is an example using PHP.

```php
$name = $_POST["name"];
$name = filter_var($name, FILTER_SANITIZE_STRING);
```
### Step 3: Implement Content Security Policy (CSP)

CSP is a computer security standard that provides an added layer of protection against XSS attacks. It can be implemented via HTTP headers from the server side.

```bash
Header set Content-Security-Policy "default-src 'self';"
```


### Step 4: Use an ORM (Object-Relational Mapping) 

An ORM is a technique that lets you interact with your database, like SQL, as though it were an object. It can protect against SQLi attacks as they utilize parameterized queries and sometimes build upon native parameterization features present in languages such as C# and java.

```python
from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///sample.db')

with engine.connect() as con:

    data = ( { "name" : "Anna" },)

    statement = text("SELECT * FROM users WHERE name = :name")

    for line in con.execute(statement, **data):
        print line
```

### Step 5: Use XSS protection libraries and functions

This will help to further sanitize input and ensure that malicious scripts can’t be executed in the victim’s browser.

```python
from django.utils.html import escape

def some_view(request):
    # Assuming request.POST['username'] contains '<script>alert("XSS")</script>'
    escaped_username = escape(request.POST['username'])

    # escaped_username now contains '&lt;script&gt;alert("XSS")&lt;/script&gt;'
```