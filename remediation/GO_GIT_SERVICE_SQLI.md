# Remediation for GO_GIT_SERVICE_SQLI

## Remediation Steps for Go Git Service SQL Injection Test

Go Git Service (GGS) SQL injection occurs when an attacker is able to insert malicious SQL code into a query. This may allow the attacker to view, edit, or delete data in the affected SQL database. Here are the steps to remediate the SQL injection vulnerability in Go Git Service:

### Step 1: Use Parameterized Statements
Parameterized statements ensure that the parameters (user supplied input) are separated from the SQL command. This makes SQL injections less likely.

In Go, we use the `database/sql` package for this:

```go
stmt, err := db.Prepare("SELECT * FROM users WHERE username=?")
if err != nil {
    log.Fatal(err)
}
rows, err := stmt.Query("GogsUser")
if err != nil {
    log.Fatal(err)
}
```

### Step 2: Validate User Input
Ensure that all user-supplied data is validated before executing a SQL query:

```go
func validInput(input string) bool {
    if strings.ContainsAny(input, ";-'") {
        return false
    }
    return true
}
```

### Step 3: Limit Database Permissions
Only required permissions should be given to the application database user. Don't use a 'root' or 'admin' database user.

Typically, a user `gogsdbuser` is created and granted permissions only on the `gogs` database:

```sql
CREATE USER 'gogsdbuser'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP ON gogs.* TO 'gogsdbuser'@'localhost';
FLUSH PRIVILEGES;
```

### Step 4: Regular Patching and Security Audits
Make sure to apply patches to the Go Git Service and underlying database system. Also, regularly perform security audits on your application and database.

```bash
sudo apt update
sudo apt upgrade
```