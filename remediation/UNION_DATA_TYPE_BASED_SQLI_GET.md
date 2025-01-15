# Remediation for UNION_DATA_TYPE_BASED_SQLI_GET

## Remediation Steps for Union Based SQL Injection Test with Data Type Variations on GET method APIs

Union based SQL Injection is a form of SQL Injection attack that uses the UNION SQL operator to combine the result of the original query with results from injected malicious SQL queries. It's a serious security risk as it could allow an attacker to extract sensitive data from a database. This becomes even more dangerous when dealing with data type variations and unsecured GET method APIs where the attacker can manipulate URL-encoded parameters to induce the SQL injection.

### Step 1: Use Prepared Statements (Parameterized Queries)

The most effective way to prevent SQL injection is to use prepared statements. They work by allowing you to define all the SQL code in advance, then you just pass in parameters to the statement. SQL will ensure that these parameters are safe and can't be used for SQL injection.

Here is an example with PHP using PDO:
```php
$stmt = $pdo->prepare('SELECT * FROM employees WHERE name = :name');

$stmt->execute(['name' => $name]);

foreach ($stmt as $row) {
    // do something with $row
}
```

### Step 2: Use Stored Procedures

Stored procedures are SQL code saved on the server that can be reused over and over again. This might add some complexity to the code but it is more secure because it allows you to encapsulate the SQL code functionality, and restrict access to underlying tables.

An example in MySQL could be:
```sql
DELIMITER $$
CREATE PROCEDURE `sp_getEmployee`(IN name varchar(255))
BEGIN
    SELECT * FROM employees WHERE name = name;
END$$
DELIMITER ;
```

### Step 3: Whitelist Input Validation

Input validation is useful for common fields like email, which have a well-defined structure. Remember to always filter and sanitize user inputs to make sure any suspicious-looking input is rejected or transformed into safe values.

### Step 4: Update and Escape Database Queries
   
It's also a good practice to escape strings in SQL queries to ensure that they're safe. Many modern web languages have functions for this. In PHP, we could use:
```php
$name = mysql_real_escape_string($name);
$query = sprintf("SELECT * FROM employees WHERE name='%s'", $name);
```

### Step 5: Limit Database Permissions

Whenever possible, limit the permissions of the database login used by your web application. Ideally, this account should only be able to perform select, insert, update and delete operations.

Please remember that the best protection is a combination of these techniques, not just relying on a single solution.