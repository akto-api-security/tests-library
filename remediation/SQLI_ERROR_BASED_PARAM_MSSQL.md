

## Remediation Steps for Error Based SQL Injection for Parameters in MS SQL Server

Error Based SQL Injection is a serious security issue. Without appropriate input validation and parameterized queries, attackers can manipulate SQL queries to expose sensitive information or even perform destructive operations.

### Step 1: Input Validation
Validate user's inputs before processing them to make sure they are as expected. In C#, you can use `Regex` to validate the inputs.

```csharp
bool IsValidInput(string input) 
{
    return Regex.IsMatch(input, @"^[\w\s]+$");
}
```

### Step 2: Replace In-line SQL with Parameterized Queries or Stored Procedures

Avoid constructing SQL queries with string concatenation. Instead, use parameterized queries or stored procedures. 

In C#, you can use `SqlCommand` to execute parameterized queries.

```csharp
using (var connection = new SqlConnection(connectionString))
{
    connection.Open();
    using (var command = new SqlCommand("SELECT * FROM Users WHERE Name = @Name", connection))
    {
        command.Parameters.AddWithValue("@Name", userName); // userName is user's input

        using(var reader = command.ExecuteReader())
        {
            while(reader.Read())
            {
                // Process the result
            }
        }
    }
}
```

### Step 3: Least Privilege Principle

Ensure that the database account used by your application to connect to the database has only those privileges which it absolutely needs. Don't grant it admin rights unless it's necessary.