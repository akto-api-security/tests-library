# Remediation for SQLI_ERROR_BASED_PARAM_APPEND_PAYLOAD_MYSQL

## Remediation Steps for Error Based SQL Injection 

Error-based SQL injection is a technique where an attacker induces errors in SQL queries to gather useful information. It is common in environments using MySQL databases. 

### Step 1: Use Prepared Statements 

The first step to prevent SQL Injection is using prepared statements. 

```java
String query = "SELECT * FROM orders WHERE id = ?";
PreparedStatement stmt = connection.prepareStatement(query);
stmt.setInt(1, id); 
ResultSet rs = stmt.executeQuery();
```

### Step 2: Use Stored Procedures

Stored procedures can also be used as they define the SQL code to be executed and allow the application to provide parameter values, reducing the risk of an SQL Injection.

```sql
CREATE PROCEDURE getUserById(IN id INT)
BEGIN
  SELECT * FROM users WHERE id = id;
END;
```

```java
CallableStatement cstmt = connection.prepareCall("{call getUserById(?)}");
cstmt.setInt(1, id);
cstmt.execute();
``` 

### Step 3: Data validation

Validating input data can serve as a secondary defense against SQL Injections. 

```java
if(userId.matches("[0-9]+")){
  // Execute the query if user Id is numeric
}
else{
  // Do not execute the query if user Id is non-numeric
}
```

### Step 4: Least Privilege Principle

Implement the principle of least privilege. Each user should be granted the minimum rights they require to complete their job function. This will minimize potential damages in case of SQL injection attack.

```bash
GRANT SELECT, UPDATE ON orders TO 'web_user'@'localhost';
```