

## Remediation Steps for Basic Prompt Injection in LLMs

Basic Prompt Injection in Language Learning Machines (LLMs) is a high risk security issue. If LLMs that use user input in executed commands are not properly sanitized, attackers may gain unauthorized access and execute dangerous scripts.

### Step 1: Sanitize All User Inputs

No matter the programming language in use, it is imperative to sanitize all user inputs to prevent unwanted scripts from being executed. Here's how to sanitize user inputs in Python:

```python
import html

# Sanitize user input by escaping HTML special characters
def sanitize_input(user_input):
    return html.escape(user_input)
```

### Step 2: Use Parameterized Queries or Prepared Statements

Parameterized queries or prepared statements allow the database to differentiate between code and data, no matter what user input is supplied. This avoids the risk of code injection.

For example, in Java:

```java
String userInput = "example";
String sql = "INSERT INTO Students (NAME) VALUES (?)";
PreparedStatement preparedStatement = connection.prepareStatement(sql);
preparedStatement.setString(1, userInput);
preparedStatement.executeUpdate();
```

### Step 3: Regularly Audit Your Code

It is important to regularly audit your code for potential vulnerabilities. This includes looking for instances where untrusted user input is used in a function that executes a command.

```bash
# Use grep to check for risky functions
grep -rE "(system|exec|popen|proc_open|shell_exec|eval|passthru|`|create_function)" .
```