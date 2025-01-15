# Remediation for TIME_BASED_SQLI_SQLITE_GET

## Remediation Steps for Time Based SQL Injection in SQLite DB for GET Method APIs

SQL injection can lead to unauthorized access to your application's database. Here are the steps to mitigate the risk of time-based SQL injection for SQLite DB for GET method APIs.

### Step 1: Parameterization of Database Queries

Parameterization ensures SQL queries are structured in a way that the database can differentiate the code from the data irrespective of what user input is supplied.

Here is a python example using SQLite.

```python
import sqlite3

def get_user(user_id):
    db = sqlite3.connect("my_sqlite_db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))  
    # ? will be replaced by the value of user_id
    user = cursor.fetchone()  
    return user

user_id = input("Enter user id:")  
# if an attacker tries to send id as 1 OR 1=1 -- , it will not work
print(get_user(user_id))
```

### Step 2: Use of Prepared Statements

Using prepared statements ensure that the actual SQL command and the data are sent separately which can completely prevent SQL injection attacks. 

Here is a python example using SQLite.

```python
import sqlite3

def get_user(user_id):
    db = sqlite3.connect('my_sqlite_db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users WHERE id=?', (user_id,))  
    # The execute function automatically escapes the parameters, 
    # rendering the application safe from sql injection
    user = cursor.fetchone()
    return user

user_id = input("Enter user id:")
print(get_user(user_id))
```

### Step 3: Regularly Update and Patch Your Systems

Make sure SQLite is regularly updated and patched with the latest security patches. This can be done by checking the SQLite website for the latest version and applying patches as needed. If you are making use of a hosted platform, ensure that they apply patches on a regular basis.

### Step 4: Validation & Sanitization 

Ensure you have validation rules in place to validate user input. An encoder library can also be used to sanitize user inputs to make sure that the input does not contain SQL meta-characters which can be utilized in an injection attack.

```python
import sqlite3
from html import escape

def get_user(user_id):
    # make sure user_id is safe to use in an SQL query
    user_id = escape(user_id)  
    db = sqlite3.connect('my_sqlite_db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users WHERE id=?', (user_id,))
    user = cursor.fetchone()
    return user

user_id = input("Enter user id:")
print(get_user(user_id))
```