

## Remediation Steps for Time based SQL Injection Test for MySQL DB for GET method APIs

Time based SQL injection is a serious security issue. Without properly securing your GET method APIs against SQL injections, attackers may leak sensitive data from your MySQL database. 

### Step 1: Do Not Trust User Input
Firstly, do not trust user input, treat all input as untrusted. Always sanitize your inputs.

```python
import cgi

def sanitize(user_input):
    return cgi.escape(user_input)
```

### Step 2: Use Parameterized Queries/PREPARE Statements
SQL injections are possible when you concatenate strings to create SQL queries. To avoid this, use parameterized queries/PREPARE statements.

```python
import mysql.connector

def fetch_data(param):
    mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="password",
         database="mydatabase"
    )
    cursor = mydb.cursor(prepared=True)
    sql_query = "SELECT * from users WHERE name = %s"
    cursor.execute(sql_query, (param, ))
```

### Step 3: Use a Web Application Firewall (WAF)
A good WAF helps protect your application by inspecting HTTP traffic before it reaches your app. It can help to mitigate SQL injection attacks.

Check your service provider's documentation for how to enable and configure the WAF.



### Step 4: Normalize Inputs
Use whitelist input validation, utilize built-in functions like `ctype_digit()` to ensure data is of the right type, length and format.

```php
if(!ctype_digit($input)){
    throw new Exception("Invalid input format.");
}
```

Following these steps should help you to mitigate threats from a Time based SQL Injection Test for MySQL DB for GET method APIs.