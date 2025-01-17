

## Remediation Steps for Union Based SQL Injection on Login Endpoints

Union based SQL injection is a serious security issue which occurs if your application is creating SQL queries by concatenating user inputs without proper sanitization or parameterization. Attackers can exploit this vulnerability to manipulate SQL queries in ways that can lead to unauthorized access or data leakage.

### Step 1: Use Parameterized Queries or Prepared Statements
Using Parameterized Queries or Prepared Statements is one of the most effective ways to prevent SQL injection. It ensures that inputs are treated strictly as values and not part of the SQL command, eliminating the risk of injecion.

For example, in Python using the `psycopg2` library:

```python
import psycopg2

# Connect to your postgres DB
connection = psycopg2.connect(dbname="your_db", user="username", password="password")

# Open a cursor to perform database operations
cur = connection.cursor()

# Here we are using the Parameterized Query, note the placeholders %s
query = "SELECT * FROM users WHERE username = %s AND password = %s"

# Execute the created SQL command
cur.execute(query, ('user_input1', 'user_input2'))

# Display the PostgreSQL database server version
data = cur.fetchone()
print(f"Data: {data}")

# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cur.close()
connection.close()
```

### Step 2: Limit Database Permissions
Only give necessary and adequate database permissions for each user or role. 

### Step 3: Input Validation
Implement stringent input validation routines to ensure only valid inputs are processed. 

```python
def validate_input(user_input):
    # Defining a set of allowed characters
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    
    if set(user_input).issubset(allowed_chars):
        return True
    return False
```
### Step 4: Regularly update and patch your DBMS
SQLi techniques often exploit known issues and bugs in database management systems (DBMS). Ensure your DBMS is regularly updated to the latest patch, so it's not vulnerable to such attacks.

### Step 5: Error handling
Do not reveal SQL errors or stack traces to end-users, which might help an attacker gain useful information about the database structure. Handle errors gracefully and log them for review.
```python
try:
    cur.execute(query, ('user_input1', 'user_input2'))
except Exception as e:
    print("An error occurred, please try again.")
    log_error(e) # Where log_error is a function to log the error details in a secure log file.
```