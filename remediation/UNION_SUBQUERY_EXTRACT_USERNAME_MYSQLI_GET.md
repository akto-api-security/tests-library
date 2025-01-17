

## Remediation Steps for Union based SQL Injection

SQL Injection is a serious security vulnerability that can allow an attacker to view, modify, and delete data in your database. When using Subquery to extract Usernames Payload for MySQL on GET method APIs, it's important to ensure that your application is properly validating and sanitizing all user inputs to prevent this vulnerability.

### Step 1: Use Prepared Statements

The most effective method to prevent SQL injection is to use prepared statements. Prepared statements essentially work by defining all the SQL code first and then passing in the parameters afterwards.

Below is an example of how to use a prepared statement in PHP:

```php
$stmt = $db->prepare('SELECT * FROM users WHERE username = ?');
$stmt->bind_param('s', $username);
$stmt->execute();
$result = $stmt->get_result();
while ($row = $result->fetch_assoc()) {
    // do something with $row
}
```

### Step 2: Use Stored Procedures

Another way to avoid SQL injection is by using stored procedures. Just like prepared statements, stored procedures separate the SQL logic from the data being passed in.

```sql
CREATE PROCEDURE getUserByUsername(IN username CHAR(20))
BEGIN
   SELECT * FROM users WHERE username = username;
END
```

You can then call this stored procedure from your application code:

```php
$stmt = $db->prepare('CALL getUserByUsername(?)');
$stmt->bind_param('s', $username);
$stmt->execute();
```

### Step 3: Input Validation

Validate user inputs to ensure they are as expected. Regular expression can be helpful in accomplishing this:

```php
$username = $_GET['username'];
if (!preg_match("/^[a-zA-Z0-9]*$/", $username)) {
   // Not a valid username
   exit;
}
```