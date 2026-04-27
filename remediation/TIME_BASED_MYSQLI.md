

## Remediation Steps for Time-Based SQL Injection in MySQL DB

Time-Based SQL Injection is an exploitable vulnerability that allows an attacker to gain unauthorized access or retrieve information from your database. To protect your MySQL database from such attacks, follow these steps:

### Step 1: Use Prepared Statements

The most effective way to avoid SQL injection attacks is to use Prepared Statements instead of dynamically concatenating queries.

In the Python language, this can be achieved using the *execute* method from the *cursor* object. Here's an example:

```py
import mysql.connector

cnx = mysql.connector.connect(user='USERNAME', password='PASSWORD', host='127.0.0.1', database='YOURDB')
cursor = cnx.cursor()

query = ("SELECT * FROM users WHERE username = %s AND password = %s")
values = ('username_value', 'password_value')

cursor.execute(query, values)

for (username, password) in cursor:
  print("{} and {}".format(username, password))
```

### Step 2: Limit Database Privileges

Ensure that the database user used by your application possesses only the bare minimum privileges it needs to function.  

```sql
GRANT SELECT, INSERT, UPDATE ON mydb.mytbl TO 'someuser'@'somehost';
```


### Step 3: Implementing a Firewall

Restrict incoming and outgoing traffic to your database server. Only allow trusted IPs to access your server. You could do this via the `iptables` firewall for Linux like so:

```bash
iptables -A INPUT -p tcp -s YOUR.TRUSTED.IP.ADDRESS --dport 3306 -j ACCEPT
iptables -A INPUT -p tcp --dport 3306 -j DROP
```

Replace "YOUR.TRUSTED.IP.ADDRESS" with the actual IP address.

### Step 5: Regular Monitoring and Logging

Monitor your systems for any unusual activity and log any suspected attacks to allow for thorough investigation later on. You can use open-source tools like `ossec` for log management.

```bash
sudo service ossec start
```