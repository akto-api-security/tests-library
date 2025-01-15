# Remediation for UNION_SUBQUERY_EXTRACT_PASSWORD_MYSQLI

## Remediation Steps for Union based SQL Injection on Login Endpoint

Union based SQL injection is a serious security issue that can lead to unauthorized data access. In this case, the issue involves extracting passwords from a MySQL database via a subquery. 

The main issue here is the fact that untrusted input is being directly embedded in SQL queries. To remediate this issue, the best way would be to use parameterized queries, also known as prepared statements.

### Step 1: Parameterized Queries/Prepared Statements
Parametrizing queries will cause any input to be treated as a string literal rather than as part of the SQL command. This eliminates the risk of SQL injection.

Here is an example in PHP of how to convert a vulnerable SQL query into a parameterized query:

```php
<?php
// Existing vulnerable SQL query
$sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";

// Convert to a parameterized query
$mysqli = new mysqli('localhost', 'my_user', 'my_password', 'my_db');

$stmt = $mysqli->prepare('SELECT * FROM users WHERE username = ? AND password = ?');
$stmt->bind_param('ss', $username, $password); 
$stmt->execute();

// ... rest of the logic
?>
```

In the above example, '?' characters act as placeholders for the username and password in the SQL query, and 'ss' indicates that the parameters are strings.

### Step 2: Use of Stored Procedures 
Using stored procedures can help with this problem, as it includes safety mechanisms if set correctly. It is another way to make sure inputs are treated as literal values and not executable code. 

### Step 3: Input Validation
Though not a full-proof method, input validation can deter a portion of basic SQL injection attacks by restricting allowed inputs.