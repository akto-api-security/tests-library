

## Remediation Steps for Union Based SQL Injection Test with Subquery to Extract Passwords Payload for MySQL on GET method APIs

Union Based SQL Injection is a major security threat that can leak sensitive information such as passwords. Here are the remediation steps:

### Step 1: Use Prepared Statements or Parameterized Queries

The use of Prepared Statements or Parameterized Queries is one of the most efficient ways to prevent SQL Injections. This makes the data sent by the user to be received as a string, not as part of SQL command.

Here's an example using PHP's Prepared Statements:

```php
$stmt = $pdo -> prepare('SELECT * FROM table WHERE id = ?');
$stmt -> execute([$_GET['id']]);
```

### Step 2: Use Web Application Firewall (WAF)

A WAF can provide an external security layer that can detect and filter out potential SQL Injection attempts.

### Step 3: Regularly Update and Patch your Systems

Ensure your systems and SQL servers are up to date with the latest software versions and security patches.

### Step 4: Least Privilege Principle

Implement the principle of least privilege across your database server. Ensure that a database account has the minimal necessary privileges for performing its intended function.

### Step 5: Input Validation

Use input validation to check user input against a set of rules. It helps prevent malicious or unintended data from being processed by your application.


### Step 6: Escaping All User-Supplied Input

This method is simplest and can be easily used in small projects. Here's an example:

```php
$id = mysqli_real_escape_string($connection, $_GET['id']);
```