# Remediation for UNION_SUBQUERY_EXTRACT_PASSWORD_MYSQLI_POST

## Remediation Steps for Union Based SQL Injection Test

Union-Based SQL Injection is a serious vulnerability, allowing an attacker to manipulate SQL queries and potentially access sensitive data. Here are steps to remediate the issue:

### Step 1: Parameterize Queries

Parameterized queries ensure that input parameters are treated strictly as data, not part of the SQL command.

For MySQL in PHP:

```php
$stmt = $pdo->prepare('SELECT * FROM users WHERE email = ? AND password = ?');
$stmt->execute([$email, $password]);
```

Python:

```python
cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
```

Java:

```java
PreparedStatement ps = connection.prepareStatement("SELECT * FROM users WHERE email = ? AND password = ?");
ps.setString(1, email);
ps.setString(2, password);
```

Note: It's important that you are not simply using string formatting functions to build your SQL commands, as this leaves you exposed to SQL Injection attacks.

### Step 2: Using An ORM (Object Relational Mapping)

ORMs can be used to mitigate the risk of SQL Injection. 

Example with Python's SQLAlchemy ORM:

```python
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://user:passwd@localhost/db')

# SQLAlchemy ORM Query
result = session.query(User).filter(User.email == email, User.password == password)
```

### Step 3: Input Validation

Using input validation libraries/frameworks to ensure input consistency and security.

For PHP:

```php
$email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
```

For Python:

```python
from django.core.validators import validate_email
validate_email(email)
```