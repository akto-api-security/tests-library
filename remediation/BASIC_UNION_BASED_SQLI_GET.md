# Remediation for BASIC_UNION_BASED_SQLI_GET

## Remediation Steps for Basic Union based SQL Injection on GET method APIs

Standard SQL injection is a web security vulnerability that allows an attacker to intervene with the queries an application makes to its database. Using a Basic Union based SQL Injection on GET method APIs can allow unauthorized users to read data that they are not permitted to access. 

### Step 1: Parameterized Queries or Prepared Statements
The most effective way to prevent SQL Injection attacks is to use parameterized queries also known as prepared statements. This process assures that the parameters (inputs from user) passed into SQL queries are treated safely by the database and can’t manipulate the structure of the query.

#### Python example:

```python
from flask_sqlalchemy import SQLAlchemy

## assuming 'app' is your Flask app
db = SQLAlchemy(app)

## assuming 'User' is the table you want to query from
query = db.session.query(User).filter(User.name == :name)
result = query.params(name = user_input).all()
```

### Step 2: Applying Least Privilege Principle
Limit database permissions by applying the least privilege principle. Don’t use the `sa` or `root` database users in your application.

#### MySQL example:

```mysql
GRANT SELECT, INSERT, UPDATE ON mydb.mytbl TO 'someuser'@'somehost';
```

### Step 3: Regular Audit and Update
Keep your database and development frameworks up-to-date.

```bash
sudo apt-get update
sudo apt-get upgrade
```

### Step 4: Input validation
Use a web application firewall (WAF) to detect and block SQL Injections.

```bash
sudo apt-get install libapache2-mod-security2
sudo service apache2 restart
```