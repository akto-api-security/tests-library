# Remediation for ADV_UNION_BASED_SQLI_XSS_GET

## Remediation Steps for Advanced Union based SQL Injection Test with XSS for GET method APIs

The combination of SQL Injection and XSS in GET method APIs can expose systems to malicious data manipulation and exfiltration. The following remediation steps are recommended in order to safeguard against these threats:

### Step 1: Prepared Statements

Parameterized queries should be used to prevent SQL Injection attacks. In this approach, all SQL statements are sent to and parsed by the database server separately from any parameters.

Here's an example in Python using the `psycopg2` library for PostgreSQL:

```python
import psycopg2
conn = psycopg2.connect("dbname=test user=postgres password=secret")
cur = conn.cursor()

# Unsafe method:
# cur.execute("INSERT INTO test (num, data) VALUES (%i, %s)" % (100, "abc'def"))

# Safe method:
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
```

### Step 2: Use an ORM

Object-Relational Mapping (ORM) is a programming technique for converting data between incompatible type systems using OOP languages. Most of them prevent SQL Injection by default.

```python
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name
```

### Step 3: Input validation and escaping

Input validation should be a cornerstone of your defense against XSS. Inputs should be checked against patterns of harmless data (such as email addresses) and rejected if they fail to conform. Special characters in HTML should also be escaped.

This can be done using language built-in functions or libraries like `html.escape()` in Python:

```python
import html
safe_html = html.escape("<script>unsafe_html</script>")
```
### Step 4: Use Content Security Policy (CSP)

CSP provides a standard method for website operators to declare which dynamic resources are allowed to load. Here's a simple example on how to use CSP:

```python
def application(environ, start_response):
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Security-Policy', "default-src 'self'")]
    start_response('200 OK', response_headers)
    return [b'Hello, World!']
```
