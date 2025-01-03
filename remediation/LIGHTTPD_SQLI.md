# Remediation for LIGHTTPD_SQLI

## Remediation Steps for Lighttpd SQL Injection
Lighttpd SQL Injection is a critical security flaw that could allow a potential attacker to inject malicious SQL code into your application, and possibly manipulate and extract data from your database. Protecting your application against SQL injection involves both secure coding practices and properly configured SQL database.

### Step 1: Use Prepared Statements
The best way to prevent SQL injection is to use prepared statements. In PHP, prepared statements look like `bindParam()`.

```php
<?php
$stmt = $db->prepare('SELECT * FROM users WHERE email = :email AND status=:status');
$stmt->bindParam(':email', $userInputEmail);
$stmt->bindParam(':status', $userInputStatus);
$stmt->execute();
?>
```

### Step 2: Limit Database Permissions
Your web application's database user should have the minimal permissions necessary to run the application. They should generally not have permissions to modify schema or drop databases.

```sql
GRANT SELECT, INSERT, UPDATE ON myDatabase.* TO 'myUser'@'localhost';
```

### Step 3: Enable Lighttpd's `mod_sql_vhost` 
Use `mod_sql_vhost` module of Lighttpd which provides automatic SQL Injection protection.

```txt
server.modules += ( "mod_sql_vhost" )
```

### Step 4: Regularly Update Lighttpd and Its Components
Always keep Lighttpd and its components updated to the latest stable version, which could include patches for known vulnerabilities.

```bash
sudo apt-get update
sudo apt-get upgrade lighttpd
```

### Step 5: Audit Your System
Regularly audit your system for potential vulnerabilities. Consider using tools specifically designed for SQL Injection detection such as SQLMap.

Remember, these steps alone will not guarantee a completely secure system. Follow good security practices for Lighttpd configuration and other server-side security standards.