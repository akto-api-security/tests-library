# Remediation for EXPRESSION_LANGUAGE_INJECTION

## Remediation Steps for Expression Language Injection
Expression Language (EL) Injection is a critical security issue where an attacker is able to use expression language to execute arbitrary code within the application. Here are the steps to mitigate this vulnerability:

### Step 1: Disable Expression Language Evaluation
In Java-based applications, you can often disable EL evaluation entirely on parts of the application where it isn't needed. Depending on your application, the code might look something like this:
```java
<context-param>
    <param-name>javax.faces.FACELETS_SKIP_COMMENTS</param-name>
    <param-value>true</param-value>
</context-param>
```
### Step 2: Use A Secure EL Processor
Make sure you're using a secure EL processor that provides an easy way to handle user inputs. Apache Commons Lang for example, provides `StringEscapeUtils.escapeEcmaScript()` method which helps in escaping user inputs:
```java
String userInput = getUserInput();
String escapedUserInput = StringEscapeUtils.escapeEcmaScript(userInput);
```
### Step 3: Input Validation
Attacks can be prevented by validating/sanitizing user input before processing. Always apply strong input validation and reject any inputs that look suspicious.
```java
if (userInput.matches("[A-Za-z]+")) {
    // process input
} else {
    throw new IllegalArgumentException("Invalid input detected");
}
```
### Step 4: Use Prepared Statements
If EL Injection is happening within the database interactions, switch to using prepared statements instead of using String concatenation. 
For example in Java:
```java
PreparedStatement statement = connection.prepareStatement("SELECT * FROM users WHERE id = ?");
statement.setString(1, userId);
ResultSet resultSet = statement.executeQuery();
```