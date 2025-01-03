# Remediation for UNION_SUBQUERY_EXTRACT_USERNAME_MYSQLI

## Remediation Steps for Union Based SQL Injection in MySQL on Login Endpoint

Union based SQL Injection is a dangerous security issue that can allow an attacker to manipulate queries to the database. A malicious payload can be embedded in the input fields that are passed into SQL queries, potentially revealing sensitive information from the database like usernames. To stop this type of attack, we can use parameterized queries, also known as prepared statements.

### Step 1: Use Prepared Statements
SQL queries usually contain string concatenation to include inputs from the user. This can lead to SQL injection attacks if not properly sanitized. To mitigate this, we can use prepared statements. 

If you're using PHP, you can utilize the built-in `PDO` library.

Here's an example in PHP:

```php
<?php
$servername = "localhost";
$dbname = "testdb";
$username = "user";
$password = "password";

try {
    $pdo = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // prepare sql and bind parameters
    $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
    // bind parameters to statement variables
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':password', $password);

    // set parameters and execute
    $username = "John";
    $password = "Doe";
    $stmt->execute();
    
} catch(PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}
?>
```

### Step 2: Input validation
It's also important to validate or sanitize user input before passing it to SQL statements.

```php
// sanitize user input
$username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_STRING);
$password = filter_input(INPUT_POST, 'password', FILTER_SANITIZE_STRING);
```

### Step 3: Limit Database Privileges
Limit access rights of the application or the user that's used in the connection to the database to only what they need, further reducing the potential impact of a SQL injection.

### Step 4: Regularly Update and Patch
Ensure your SQL server and your coding language libraries are regularly updated and patched, as vulnerabilities are often found and fixed in these updates. 

By following these best practices, the impact of Union based SQL Injection can be minimized.