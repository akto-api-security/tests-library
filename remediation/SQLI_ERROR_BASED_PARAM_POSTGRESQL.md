

## Remediation Steps for Error Based SQL Injection Test for Parameters for PostgreSQL
SQL injection is a code injection technique that attackers exploit to gain unauthorized access to a database or to retrieve/sabotage sensitive information. Attackers use malicious SQL codes to bypass the application security measures, thereby accessing, modifying, and deleting the content of a database.

### Step 1: Parameterized Queries
Use parameterized queries or prepared statements to prevent SQL injection. Here is a Python example with `psycopg2` for PostgreSQL.
```python
import psycopg2
try:
    connection = psycopg2.connect(user="sysadmin",password="password",host="localhost",port="5432",database="database")
    cursor = connection.cursor()
    postgres_insert_query = """ INSERT INTO student (id, name) VALUES (%s,%s)"""
    record_to_insert = (5, 'arslan')
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
```
### Step 2: Use Store Procedures
Stored procedures can provide a powerful way to code application logic that can be stored on the server. This can also help to prevent SQL Injection. Here is a SQL example.
```sql
CREATE OR REPLACE FUNCTION get_employees (p_name varchar)
RETURNS SETOF employees AS
$$
BEGIN
RETURN QUERY 
SELECT * FROM employees WHERE name = p_name;
END;
$$ LANGUAGE plpgsql;
```
### Step 3: Regular Expression Checks
Using regular expressions to validate input data and restrict to alphanumeric characters only or as per the requirement can prevent SQL injection in most cases.

### Step 4: Least Privilege Principle
Implementing the principle of least privilege for database accounts can protect the database even if a SQL injection attack occurs. Never connect to your database using an account with admin-level privileges, unless this is absolutely necessary.