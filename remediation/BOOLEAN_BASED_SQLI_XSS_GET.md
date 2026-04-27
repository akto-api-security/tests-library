

## Remediation Steps for Boolean based SQL Injection Test with XSS and GET method APIs

Boolean based SQL Injection and Cross-Site Scripting (XSS) are serious security vulnerabilities that can allow an attacker to manipulate or exploit your web application and compromise your database.

### Step 1: Use Prepared Statements (Parameterized Queries)
Prepared statements ensure that an attacker is not able to change the intent of a query, even if SQL commands are inserted into it.

In PHP, you can use PDO to perform this:
```php
$pdo = new PDO('mysql:dbname=db;host=127.0.0.1', 'username', 'password');
$statement = $pdo->prepare('SELECT * FROM employees WHERE name = :name');

$statement->execute(['name' => $name]);
$row = $statement->fetch(PDO::FETCH_ASSOC);
```

### Step 2: Use a Web Application Firewall (WAF)
A WAF can help shield your application from attempts at XXS or SQLi. Some WAFs can automatically sanitize requests which contain malicious data.

### Step 3: Validate, Sanitize and Limit Data
Validate inputs to confirm they adhere to the expected format, sanitize them to ensure they do not contain any harmful data, and limit data to minimize the potential damage of attacks.

In PHP:

```php
$name = trim($_POST['name']);
$name = strip_tags($name);
$name = htmlspecialchars($name);
```

### Step 4: Use HTTPOnly cookies
Use HTTPOnly cookies to mitigate the risk of a client-side script accessing the protected cookie.

### Step 5: Encode Data on Output
At the point where user-controllable data is output in HTTP responses, encode the outputs to prevent XSS attacks.

In PHP, use the `htmlentities()` or `htmlspecialchars()` functions:

```php
$username = $_POST['username'];
echo 'Welcome, '.htmlspecialchars($username, ENT_QUOTES, 'UTF-8');
```

### Step 6: Use Least Privilege Principle
Enforce the principle of least privilege, where a process should accept only the privileges which are essential to its function.

For example, most web applications do not need the permission to DROP tables in the database. By restricting privileges, you can reduce the damage potential of an SQL Injection attack.