

## Remediation Steps for Stored SQL Injection Test with XSS and GET method APIs

Stored SQL Injection combined with Cross-Site Scripting (XSS) is a serious security issue. An attacker can manipulate SQL queries via APIs to interact with the database, and conduct XSS attacks. This can lead to data theft, data manipulation, and even remote code execution.

### Step 1: Parameterize SQL Queries

Instead of building SQL queries with string concatenation, use parameterized queries. This helps to prevent an attacker from injecting malicious SQL code. 

Example in Python using `psycopg2` library:

```python
import psycopg2

# connect to the database
conn = psycopg2.connect(database="testdb", user = "postgres", password = "pass123")

# create a cursor
cur = conn.cursor()

# create a parameterized query
cur.execute("SELECT * FROM employees WHERE last_name = %s", (lname,))

rows = cur.fetchall()
```
### Step 2: Use a WAF (Web Application Firewall)

WAFs can identify and block common penetration testing techniques such as SQL injection XSS attack vectors.

```bash
sudo apt-get install mod-security
sudo a2enmod security2
sudo service apache2 restart
```

### Step 3: Validate input on GET Method APIs

Use strict input validation to filter out any rogue or malformed data in GET requests.

```python
from django.core.exceptions import ValidationError

def validate_username(username):
    if not username.isalnum():
        raise ValidationError("Username should be alphanumeric")

```

### Step 4: Sanitize User Inputs

Ensure that all user inputs are sanitized before they are used in SQL queries or displayed back to the user. This could prevent attackers from introducing harmful SQL or HTML/JavaScript code.

```python
from django.utils.html import escape

def sanitize_input(input_data):
    return escape(input_data)
```

### Step 5: Use Content Security Policy (CSP)

CSP adds an additional layer of security, helping to detect and mitigate XSS and other data injection attacks.

```html
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src https://*; child-src 'none';">
```