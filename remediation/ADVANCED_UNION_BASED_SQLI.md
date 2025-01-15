# Remediation for ADVANCED_UNION_BASED_SQLI

## Remediation Steps for Advanced Union Based SQL Injection on Login Endpoints

An Advanced Union Based SQL Injection involves exploiting web applications that use user-supplied data in SQL queries without stripping out potentially harmful characters first. This can allow attackers to manipulate SQL queries to view data that they should not be able to access. Here are some ways to prevent it:

### Step 1: Use Prepared Statements

The best way to prevent SQL Injection attacks is to use prepared statements with parameterized queries. Using them ensures that an attacker cannot change the intent of a query, even with SQL commands injected.

Java:
```java
String selectSQL = "SELECT * FROM Users WHERE email = ? AND password = ?";
PreparedStatement preparedStatement = dbConnection.prepareStatement(selectSQL);
preparedStatement.setString(1, userInputEmail);
preparedStatement.setString(2, userInputPassword);
ResultSet rs = preparedStatement.executeQuery();
```

Python using psycopg:
```python
cur = conn.cursor()
cur.execute("SELECT * FROM Users WHERE email = %s AND password = %s", (userInputEmail, userInputPassword))
```

### Step 2: Use Stored Procedures

Stored procedures can also provide a layer of security, functioning similarly to prepared statements. 

SQL:
```sql
CREATE PROCEDURE Login_User
  @userInputEmail varchar(100), 
  @userInputPassword varchar(100)
AS 
  SELECT * FROM Users WHERE email = @userInputEmail AND password = @userInputPassword;
```

### Step 3: Use a Web Application Firewall

A Web Application Firewall (WAF) can help you filter out harmful SQL Injection queries.

```bash
modsecurity_crs_41_sql_injection_attacks.conf
```

### Step 4: Limit Database Permissions

As much as possible, limit the permissions of the database user connected to your web application. Never connect your web application to the database using an account with admin level privileges.

```sql
GRANT SELECT, INSERT, UPDATE ON database.* TO 'user'@'localhost';
```

### Step 6: Input Validation

Validate input by testing type, length, format, and range.

Python:
```python
# Check email format
re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', userInputEmail)
# Check password length
len(userInputPassword) > 8
```

This can help avoid SQL injection vulnerabilities by preventing an attacker from sending malicious inputs.