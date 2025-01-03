# Remediation for UNION_URL_ENCODED_BASED_MYSQLI_POST

## Remediation Steps for Union based SQL Injection with URL Encoded Payloads in MySQL on POST method APIs.
SQL injection is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. It happens when a developer accepts input from a user and directly uses it in a SQL Query. 

### Step 1: Use Prepared Statements (with Parameterized Queries)
The use of prepared statements (with Parameterized Queries) will ensure that the SQL injection cannot occur. This is because the input data and the code are sent separately and the data is never treated as code.

Here's how you can implement this in a language like Java with JDBC:

```java
String selectSQL = "SELECT user_id FROM users WHERE username = ? ";
PreparedStatement preparedStatement = dbConnection.prepareStatement(selectSQL);
preparedStatement.setString(1, username);
ResultSet rs = preparedStatement.executeQuery(selectSQL );
```

### Step 2: Apply Proper Error Handling
Never reveal the details of the underlying technology in your error messages.

```java
try {
...//Your Code
} catch (SQLException se) {
  // log the exception
  logger.error("SQL Exception", se);
} catch (Exception e) {
  // log the exception
  logger.error("Exception", e);
}
```

### Step 3: Keep your Database System Version Up-to-Date
Regular updates and patches can fix recognized SQL injection vulnerabilities.

```bash
sudo apt-get update
sudo apt-get upgrade
```
### Step 4: Use a Web Application Firewall (WAF)
A Web Application Firewall (WAF) can help protect your web applications by filtering and monitoring HTTP traffic between a web application and the Internet. You can configure your WAF to block SQL injections. 

Most WAF settings can be tailored to your application's needs while blocking the malicious input patterns associated with SQL injection attacks.

```bash
sudo apt install mod-security-crs
sudo a2enmod security2
sudo systemctl restart apache2
```
In conclusion, an effective approach to protecting against SQL Injection attack involves a combination of these defenses. Keep in mind that it's not enough to just implement one, but a combination of all these measures will ensure your application is safe from SQL Injection attacks.