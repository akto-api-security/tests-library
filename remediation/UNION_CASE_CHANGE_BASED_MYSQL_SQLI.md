# Remediation for UNION_CASE_CHANGE_BASED_MYSQL_SQLI

## Remediation Steps for Union based SQL Injection on Login Endpoints (MySQL)

SQL Injection refers to an attack where an attacker can execute malicious SQL statements that control a web application's database. Specifically, Union Based SQL Injection is a method where an attacker exploits the UNION SQL operator to combine the result set of two or more SELECT statements to retrieve extra information.

### Step 1: Use Prepared Statements (Parameterized Queries)
One of the best ways to prevent SQL injection is to use prepared statements with parameterized queries. Here is an example in PHP using MySQLi:

```php
$stmt = $dbConnection->prepare('SELECT * FROM users WHERE email = ? AND password = ?');
$stmt->bind_param('ss', $user, $password);

$user = $_POST['username'];
$password = $_POST['password'];
$stmt->execute();
```

This code effectively makes sure that the user-provided input is never inserted directly into the query.

### Step 2: Use Stored Procedures
Another effective measure against SQL Injection is the use of stored procedures. It essentially encapsulates the SQL statements in a routine stored on the server, which also prepares the statement.

```SQL
DELIMITER $$
CREATE PROCEDURE `sp_safe_login`(IN `p_username` VARCHAR(50), IN `p_password` VARCHAR(50))
BEGIN
	SELECT * FROM users WHERE username = p_username AND password = p_password;
END$$
DELIMITER ;
```

You can call this Stored Procedure from your code. Note that the above SQL is an example, you should hash and salt passwords instead of storing them as plain texts.

### Step 3: Whitelist Input Validation
Input should always be validated before it is used. A whitelist validation approach (defining exactly what is allowed) is better than a blacklist approach (defining what is disallowed) as it's easier to define what is acceptable and reject everything else. 

```php
if (preg_match('/^[a-z0-9]{5,}$/', $_POST['username'])) { 
    // username is valid
} else {
    // username is not valid
}
```

In this code snippet, we only allow lowercase alphanumeric characters in the username.

### Step 4: Escaping User Input
If you need to use user input in string building SQL queries, make sure the user input is properly escaped.

```php
$username = mysqli_real_escape_string($conn, $username);
```

Note that this is not a best-practice solution and should only be used as a last resort when none of the above methods are viable.

### Step 5: Regular Updates
Install updates, patches, and fixes from your DBMS and application language vendors regularly. They may include security enhancements that prevent SQL Injection.