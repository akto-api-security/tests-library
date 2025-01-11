# Remediation for UNION_SUBQUERY_EXTRACT_USERNAME_MYSQLI_POST

## Remediation Steps for Union based SQL Injection with Subquery for MySQL

Union based SQL Injection can lead to serious security vulnerabilities, possibly allowing malicious users to view, modify, and delete data in your database. Here is the best way to counter this threat:

### Step 1: Use Prepared Statements
Use Prepared Statements with Parameterized Queries. These are SQL statements that are sent to and parsed by the database server separately from any parameters. This way, it is impossible for an attacker to inject malicious SQL.

For example, in Python with MySQL Connector you could use:

```python
import mysql.connector

cnx = mysql.connector.connect(user='username', database='database')
cursor = cnx.cursor(prepared=True)

query = ("SELECT * FROM users WHERE username = %s AND password = %s")
cursor.execute(query, (username, password))
```

### Step 2: Use Object Relational Mapping Tools (ORMs)
ORMs like Hibernate in Java or SQLAlchemy in Python can protect your application by default from SQL Injection by using parameterized queries.

Example in SQLAlchemy:

```python
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine('postgresql://username:password@localhost/dbname')
session = Session(bind=engine)

res = session.query(User).filter(User.name == username).filter(User.passw == password)
```

### Step 3: Employ a Web Application Firewall (WAF)
A good WAF can help filter out SQL Injection attempts. While this shouldn't be your only line of defense, it can be a useful tool in your security arsenal.