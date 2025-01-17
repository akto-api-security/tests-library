

## Remediation Steps for Error Based SQL Injection in MySQL Parameters

Error-based SQL injection is a common security vulnerability where an attacker can inject malicious SQL code through user input fields, which can result in unauthorized data access or even data manipulation. Below are the steps to remediate this issue. 

### Step 1: Use Prepared Statements

You should always use prepared statements or parameterized queries. They allow you to define all the SQL code, and then pass in each parameter to the query later. This helps MySQL distinguish the difference between code and data, regardless of what user input is supplied.

In PHP, you could use the `mysqli` extension to prepare statements.

```php
$stmt = $mysqli->prepare("INSERT INTO MyTable (Column) VALUES (?)");
$stmt->bind_param('s', $user_input);
$stmt->execute();
$stmt->close();
```

Here, `s` denotes the datatype of the input parameter (`s` string, `i` integer, etc.).

### Step 2: Use a Web Application Firewall (WAF)

A WAF can help filter out SQL Injection attempts and can be an effective measure in conjunction with implementing secure code practices.

### Step 3: Regular Code Reviews

Regular code reviews can help identify SQL injection vulnerabilities, especially in older code. Automated tools can also be used to aid in the process, but manual reviews are highly recommended as well.

### Step 4: Least Privilege Principle

Always ensure that database accounts used by your web applications only have the necessary permissions and no more. This limits the potential damage of a successful SQL injection attack. For example, if an application only needs to retrieve data, the account it uses should only have SELECT permissions and nothing else.

### Step 5: Input Validation

Check if the input provided is of expected data type like integers, strings, etc. If the application expects an integer, ensure that the input is an integer before passing it to the SQL query.

Please remember that input validation alone is not enough to prevent SQL injections. It should be used in combination with the other steps mentioned above.