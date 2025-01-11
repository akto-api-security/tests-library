# Remediation for BASIC_UNION_BASED_SQLI

## Remediation Steps for Basic Union Based SQL Injection Test on Login Endpoints

SQL injection is a significant security vulnerability that can allow an attacker to manipulate the structure of SQL queries, which could potentially access, modify, and delete data.

### Step 1: Parameterized Queries

The most common way to prevent SQL injection is through the use of parameterized queries or prepared statements, which separates SQL data from SQL code.

Here's an example of parametrized query in Python using the MySQL connector:

```python
import mysql.connector

# establish the connection
cnx = mysql.connector.connect(user='username', database='database_name', password='password')

cursor = cnx.cursor(prepared=True)

# query
query = ("SELECT * FROM users WHERE username = ? AND password = ?")

# parameters
username = input("Enter username: ")
password = input("Enter password: ")

# execute the query
cursor.execute(query, (username, password))

cnx.close()
```

### Step 2: Use of ORM Frameworks

Object Relational Mapping (ORM) can abstract database queries, and most ORM frameworks have built-in defense measures against SQL injection.

Here is an example in Ruby on Rails:

```ruby
# Assuming User is a model with :username and :password attributes
username = params[:username]
password = params[:password]

user = User.where("username = ? AND password = ?", username, password).first
```

### Step 3: Database WAF 

Deploy a Database Web Application Firewall (WAF) to add a layer of security and aid in detecting and blocking SQLi attempts. 

No solution is future-proof, but combining these remediation steps will greatly mitigate the risk of SQL injection.