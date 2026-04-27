

## Remediation Steps for Bypassing Input Validation with Null Values
When an input validation control has been bypassed with null values, this potentially opens the system to a myriad of vulnerabilities, such as SQL Injection, XSS, and Buffer-Overflow attacks. Therefore, it is vital that you ensure null values aren't used to bypass your validation.

### Step 1: Install a reliable sanitizing library
First, ensure that you have a reliable data sanitizing and validation library in place. For Java, you can use the `org.apache.commons.lang3.StringEscapeUtils` package.

Add the following to your pom.xml file:
```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-lang3</artifactId>
    <version>3.9</version>
</dependency>
```

### Step 2: Sanitize and Validate Input
Next, sanitize the user input received at the server-side by escaping special characters and validating. If the received input is null, do not perform any operations, and return an error message. 

```java
import org.apache.commons.lang3.StringEscapeUtils;

public String sanitize(String input) {
    if(input == null) throw new IllegalArgumentException("Input cannot be null");
    return StringEscapeUtils.escapeHtml4(input);
}
```

### Step 3: Implement Server-Side Data Validation
In addition to sanitizing the data, validate all user-supplied input to ensure that it meets requirements. Using `@NotNull` annotation from `javax.validation.constraints.NotNull` package helps in ensuring that the passed parameter is not null.

```java
import javax.validation.constraints.NotNull;

void processUserInput(@NotNull String input){
  //process input further
}
```