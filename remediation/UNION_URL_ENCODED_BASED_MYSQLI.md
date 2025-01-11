# Remediation for UNION_URL_ENCODED_BASED_MYSQLI

## Remediation Steps for Union-based SQL Injection Test with URL Encoded Payloads on MySQL Login Endpoints

Union based SQL Injection is a serious security issue. Attackers may inject malicious SQL commands into user input fields, and these commands may successfully pass through authentication processes if your application is vulnerable. These SQL commands can leak, modify or delete sensitive data from your database.

### Step 1: Use Prepared Statements

Use prepared statements with parameterized queries. These features ensure that the parameters (i.e., the inputs from users) passed into SQL statements are treated in a safe manner. 

If you are using Java, for example, you can use `PreparedStatement`.

```java
String name = request.getParameter("username");
String password = request.getParameter("password");
String query = "SELECT * FROM users WHERE username = ? AND password = ?";

PreparedStatement ps = connection.prepareStatement(query);
ps.setString(1, name);
ps.setString(2, password);
ResultSet results = ps.executeQuery();
```

### Step 2: Use an ORM Tool

Object-relational mapping (ORM) tools can be useful as they usually provide SQL-injection safe APIs.

For Python with SQLAlchemy ORM:

```python
from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///your_database.db')

with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM users WHERE username=:username AND password=:password"),
        {"username": user_input_name, "password": user_input_password})
```

### Step 3: Input Validation

Ensure that the user-entered values are validated for their types, lengths, format, and business rules before being used in the SQL query.

```python
# An example in Python
def validate_input(username, password):
    # Add your own validation rules
    if not username.isalnum() or not password.isalnum():
        return False
    if len(username) > 25 or len(password) > 25:
        return False
    return True

# Only proceed when inputs are valid
if validate_input(user_input_name, user_input_password):
    # Proceed with the login process
```

### Step 4: Least Privilege Principle

Ensure your database user has the minimum necessary privileges. 

```bash
mysql> CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';
mysql> GRANT SELECT ON database_name.* TO 'new_user'@'localhost';
```