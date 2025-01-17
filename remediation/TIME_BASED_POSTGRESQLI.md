

## Remediation Steps for Time based SQL Injection in PostgreSQL DB
Time based SQL injection is a serious security issue. Such type of SQL Injection relies on the database's response time to infer information. To protect your PostgreSQL DB from time-based SQLi, consider the following steps: 

### Step 1: Use Parameterized Queries
Parameterized queries ensure that the parameters passed into SQL statements are treated simply as strings and not executable code. This eliminates the possibility of harmful SQL code execution. 

Below is an example in Python.

```python
import psycopg2

# connect to your database
conn = psycopg2.connect(
    dbname="your_db", 
    user="your_username", 
    password="your_password", 
    host="localhost"
)
cur = conn.cursor()

# Never do this -- insecure!
# symbol = 'RHAT'
# cur.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Use this instead
symbol = 'RHAT'
cur.execute("SELECT * FROM stocks WHERE symbol = %s", (symbol,))
```

### Step 2: Limit Database Permissions
Only the necessary permissions should be provided to the roles which are interacting with the database. Avoid using a role with administrative privileges for application roles.

### Step 3: Regularly Update and Patch Your Database Management System
Ensure that the PostgreSQL DB is regularly updated and patched. Newer versions often come with security enhancements that fix known vulnerabilities and add extra layers of security.

### Step 4: Implement a Web Application Firewall (WAF)
A WAF can help to block SQL Injection attacks by inspecting the HTTP traffic and identifying suspicious patterns.
