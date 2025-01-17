

## Remediation Steps for Basic Union Based SQL Injection On POST Method APIs

Basic Union-based SQL Injection is a critical vulnerability that could allow attackers to manipulate the structure of your application's SQL queries using user input. By properly sanitizing your input data and avoiding raw SQL queries, you can protect your application from this type of attack.

### Step 1: Parameterized Queries
Use parameterized queries or prepared statements. This guarantees that the data passed into your queries will be always treated as literal string input and never part of the SQL command itself.

This practice can be implemented in many modern programming languages. Below, we demonstrate this using Python's psycopg2 library:

```python
import psycopg2

# Establish a connection to db
conn = psycopg2.connect(database="dbname", user="dbuser", password="dbpass", host="localhost", port="5432")

# Create a cursor object
cur = conn.cursor()

# BAD PRACTICE: SQL query using python f-string
# cur.execute(f"SELECT * FROM users WHERE username = {user_input}")

# GOOD PRACTICE: Parameterized query
cur.execute("SELECT * FROM users WHERE username = %s", (user_input,))

# Close communication with db
cur.close()
conn.close()
```

### Step 2: Use an ORM

Using an Object-Relational Mapping library (ORM) can also prevent SQL Injection as they often use parameterized queries by default.

For example, with Django's ORM:

```python
from django.contrib.auth.models import User

# Bad practice: Raw SQL query
# User.objects.raw('SELECT * FROM auth_user WHERE username = %s' % user_input)

# Good practice: Django ORM
users = User.objects.filter(username=user_input)
```

### Step 3: Input Validation

As an extra layer of defense, validate and sanitize user input. By enforcing the rules on input fields, you can prevent malicious data from being entered into your system.

```python
import re
from django.core.exceptions import ValidationError

def validate_username(username):
    if not re.match(r'^[\w.@+-]+$', username):
        raise ValidationError('Invalid username')
    return username
```

These steps, if implemented, would allow your database to remain secure from Basic Union based SQL Injection in POST method APIs.