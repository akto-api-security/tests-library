# Remediation for UNION_CASE_CHANGE_BASED_MYSQL_SQLI_GET

## Remediation Steps for Union based SQL Injection test with case change variations for MySQL on GET method APIs

Union based SQL injection is a serious security issue that allows attackers to leverage UNION SQL operator to extract data from the database server. Using different case variations can bypass simple checks or filters put in place. Here are steps to mitigate this issue:

### Step 1: Use Parameterized Queries 

Using parameterized queries will reduce the risk of SQL injection as it separates the SQL logic from the data being passed in.
```python
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="username",
        password="password",
        database="your_database",
    ) as connection:
        insert_query = "INSERT INTO employees (name, address) VALUES (%s, %s)"
        values = ("John", "Highway 21")
        with connection.cursor() as cursor:
            cursor.execute(insert_query, values)
            connection.commit()
except Error as e:
    print(e)
```
### Step 2: Regularly update your SQL database 
Updating your SQL database software ensures that it has the most secure and up-to-date configurations, reducing the potential vulnerabilities that attackers can take advantage of.

```bash
sudo apt-get update
sudo apt-get upgrade mysql-server
```
### Step 3: Input validation
Make sure to validate all the inputs using both PHP’s built-in functions and database specific syntaxes. Ensure that numeric values are numeric and free of special characters that can lead to an SQL command. Do not forget to escape special characters.

### Step 4: Limit User Privileges
Limiting the privileges of database accounts used by the web application can reduce the potential damage of a SQL injection attack. With fewer permissions, the attack can do less harm.

### Step 5: Error Handling
Dangerous information can be revealed through error messages. Make sure not to disclose sensitive information in error messages and handle them properly to prevent information leakage. 

No solution is 100% secure, therefore, regular audits and assessments should be performed to ensure the continuous security of your system.