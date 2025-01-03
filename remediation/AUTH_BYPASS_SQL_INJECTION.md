# Remediation for AUTH_BYPASS_SQL_INJECTION

## Remediation Steps for Authentication Bypass using SQL Injection

Authentication Bypass using SQL Injection is a critical security issue that allows malicious users to potentially gain unauthorised access to sensitive information in your database. SQL Injection typically occurs when the application uses raw SQL in the code, which could be manipulated to perform unintended actions. 

### Step 1: Use Prepared Statements 
Prepared statements ensure that an attacker is not able to change the intent of a query, even if SQL commands are inserted into the query. 

Here is an example using PHP with MySQLi:

```php
$stmt = $conn->prepare("INSERT INTO Users (firstname, lastname, email) VALUES (?, ?, ?)");
$stmt->bind_param("sss", $firstname, $lastname, $email);

$firstname = "John";
$lastname = "Doe";
$email = "john@example.com";
$stmt->execute();
```

### Step 2: Use Stored Procedures
A stored procedure is a prepared SQL code that you can save so that the code can be reused over and over again. Here is an example using MySQL:

```sql
CREATE PROCEDURE InsertUser(IN p_firstname varchar(255), IN p_lastname varchar(255), IN p_email varchar(255))
BEGIN
    INSERT INTO Users(firstname, lastname, email) VALUES (p_firstname, p_lastname, p_email);
END//
```

### Step 3: Escape User Supplied Input
Another, less effective, means of preventing SQL Injection is to escape user input. PHP has the built-in `mysql_real_escape_string()` function to escape user-provided data:

```php
$username = mysql_real_escape_string($username);
$password = mysql_real_escape_string($password);
```

### Step 4: Least Privilege Principle
Ensure that the database account your app uses to perform routine tasks has the fewest privileges necessary, to minimize potential damage.

```sql
GRANT SELECT, INSERT, UPDATE ON database.table TO 'user'@'localhost';
```

### Step 5: Regular Auditing and Update
Keep track of and regularly update the dependencies and libraries that your application is using, as they may also harbor vulnerabilities that may lead to SQl Injection attacks. 

```bash
npm audit
npm update
```
Be sure to incorporate these remediation steps in your application to prevent Authentication Bypass using SQL Injection attacks.