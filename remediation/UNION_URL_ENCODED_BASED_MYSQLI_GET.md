

## Remediation Steps for Union based SQL Injection with URL Encoded Payloads

Union-based SQL Injection is a serious security vulnerability affecting web applications that do not properly sanitize user input for SQL special characters. This allows attackers to modify SQL queries and access data they are not supposed to.

### Step 1: Parameterized Queries

The first step in countering SQL injection attacks is by using parameterized queries instead of string concatenation to build SQL queries. This ensures data is treated strictly as user input and not part of SQL command.

```python
# Example in Python using pymysql library
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
```

### Step 2: URL Encoding Validation

You need to ensure your application correctly decodes URL encoded payloads and does not interpret special characters or SQL commands from these payloads

```python
import urllib.parse

def safe_decode(url):
    return urllib.parse.unquote(url)
```

### Step 3: Implement Web Application Firewall

Consider a web application firewall (WAF) that may detect and block SQLi attacks. Many WAFs have built-in rulesets for preventing SQLi.

### Step 4: Least Privilege Principle

Ensure your database user has minimal privileges necessary to function. This can limit the potential damage caused by a SQLi attack. Do not grant admin or db owner access unless it's absolutely necessary. 

```bash
GRANT SELECT, INSERT, UPDATE ON database_name.* TO 'user'@'localhost';
```