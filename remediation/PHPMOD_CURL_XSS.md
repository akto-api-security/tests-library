# Remediation for PHPMOD_CURL_XSS

## Remediation Steps for Php-mod/curl Library Cross-Site Scripting
Cross-Site Scripting (XSS) vulnerabilities occur when data entered by a user is interpreted as code by the browser. This can allow attackers to execute malicious scripts.

To tackle XSS vulnerabilities in php-mod/curl library, sanitize all user inputs and implement proper output encoding. Below are the remediation steps:

### Step 1: Sanitize User Input
Ensure all user input is sanitized. This should be done for all data that comes from an untrusted source, such as form submissions.

```php
$input = $_POST['user_input']; // unsanitized user input

$sanitized_input = filter_var($input, FILTER_SANITIZE_STRING); // sanitizing user input
```

### Step 2: Encoding Output
Ensure all outputs are properly encoded, meaning characters that have a special meaning in HTML are translated to their corresponding HTML Entities.

```php
echo htmlentities($sanitized_input, ENT_QUOTES, 'UTF-8');
```

### Step 3: Use Prepared Statements for SQL Queries
With prepared statements, the SQL code is defined and placeholders are used for the direct input. That way, an attacker is unable to change the intent of a query, even if SQL commands are inserted into it.

```php
$stmt = $dbConnection->prepare('SELECT * FROM users WHERE email = ?');
$stmt->bind_param('s', $sanitized_input);

$stmt->execute();
```