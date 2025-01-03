# Remediation for TIME_BASED_POSTGRESQLI_GET

## Remediation Steps for Time-Based SQL Injection in PostgreSQL DB for GET Method APIs

Time-based SQL injection is a severe security issue that attackers use to delay responses from the database to determine if a potential point of injection exists. They can exploit these points to gain unauthorized access to the database.

### Step 1: Parameterize SQL Queries

Regardless of the language you are using, the most critical step is to parameterize SQL queries.

#### Example in Java JDBC:

```java
String selectSQL = "SELECT USER_ID FROM USERS WHERE USERNAME = ?";
PreparedStatement preparedStatement = dbConnection.prepareStatement(selectSQL);
preparedStatement.setString(1, username);
ResultSet rs = preparedStatement.executeQuery(selectSQL);
```

### Step 2: Use Object Relational Mapping Tools

ORM tools often provide security benefits over raw SQL.

#### Example in Python with SQLAlchemy:

```python
from sqlalchemy.orm import Session
from models import User

session = Session()
user = session.query(User).filter_by(name=user_name).first()
```

### Step 3: Employ a Web Application Firewall (WAF)

A WAF can help filter out malicious data and provide additional protection against injection attacks.

```bash
sudo apt-get install mod-security-crs
```

### Step 4: Regular Audit and Update

Regularly review your code for potential injection points and keep your tools & libraries up to date.

```bash
sudo apt-get update && sudo apt-get upgrade
```

### Step 5: Limit Database Permissions

You should limit your database's permissions and not provide unnecessary access rights to the database account that is used to connect from your web application.

```SQL
REVOKE ALL PRIVILEGES ON schema public FROM username;
GRANT SELECT, INSERT ON schema public TO username;
```

Note: Replace `username` with actual database user name.

Bear in mind that only the application of some or all of these steps can truly lessen the risk of time-based SQL injection. It's also worth noting that using an ORM tool or parameterizing your queries does not guarantee total safety.