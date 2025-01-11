# Remediation for STORED_SQLI_XSS

## Remediation Steps for Stored SQL Injection & XSS
Stored SQL Injection and Cross-Site Scripting (XSS) are serious security issues that can lead to data breaches and unauthorized access to data. Here are remediation steps to protect against these vulnerabilities:

### Step 1: Parameterized Queries
To prevent SQL Injection, use parameterized queries to assure your application treats all data strictly as user input. This can be achieved in several languages, for instance:

```java
PreparedStatement preparedStatement = connection.prepareStatement("SELECT * FROM employees WHERE name = ?");
preparedStatement.setString(1, name);
ResultSet resultSet = preparedStatement.executeQuery();
```

### Step 2: Output Encoding
To prevent XSS, you need to ensure any client-submitted data that is later displayed to users is correctly encoded. Most languages have libraries for this, here's a PHP example:

```php
$secure_output = htmlentities($input, ENT_QUOTES, 'UTF-8');
```

### Step 3: Implement Proper Filtering
Make sure to filter all user-submitted data before it's stored in your database.

```php
$filtered_input = filter_input(INPUT_POST, 'data', FILTER_SANITIZE_STRING);
```