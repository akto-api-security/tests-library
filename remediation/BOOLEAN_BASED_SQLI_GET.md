# Remediation for BOOLEAN_BASED_SQLI_GET

## Remediation Steps for Boolean Based SQL Injection
Boolean based SQL injection on GET method APIs allows an attacker to manipulate queries. Without proper input validation, an attacker can potentially view, modify and delete data.

### Step 1: Always Escape Input
The first and foremost step is to validate all input data. Any data from an untrusted source should be considered a potential security risk. Always filter input data, accept only what is required and expected.
```java
String user_input = request.getParameter( "input" );
user_input = ESAPI.encoder().encodeForSQL( new OracleCodec(), user_input );
```

### Step 2: Use Parameterized Queries or Prepared Statements
Parameterized queries ensure that parameters (user supplied input) are separate from the query code, thus making it impossible for an attacker to manipulate the query structure.  

```java
String selectSQL = "SELECT user_id FROM users WHERE username = ? AND password = ?";
PreparedStatement preparedStatement = dbConnection.prepareStatement(selectSQL);
preparedStatement.setString(1, input_uname);
preparedStatement.setString(2, input_password);
ResultSet rs = preparedStatement.executeQuery(selectSQL );
```

### Step 3: Limit Privileges
Use the principle of least privilege. Each interaction with a database must be done with the minimum required privileges. Do not connect to a database using an "admin" or "sa" level account.

```bash
CREATE USER 'limitedUser'@'localhost' IDENTIFIED BY 'your-password';
GRANT SELECT, INSERT, UPDATE ON your_database.* TO 'limitedUser'@'localhost';
FLUSH PRIVILEGES;
```