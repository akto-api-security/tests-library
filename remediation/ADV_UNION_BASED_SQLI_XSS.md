# Remediation for ADV_UNION_BASED_SQLI_XSS

## Remediation Steps for Advanced Union based SQL Injection Test with XSS

SQL Injection is a code injection technique that attackers can use to attack the data-driven applications. This attack can be done by inserting malicious SQL statements into the input field for execution. Cross-Site Scripting (XSS) is another type of security vulnerability typically found in web applications. It enables attackers to inject client-side scripts into webpages viewed by other users.

### Step 1: Use Parameterized Queries
The best way to prevent SQL Injection attacks is to use parameterized queries or prepared statements. 

```java
// Java Example
String query = "SELECT * FROM orders WHERE order_id = ?";
PreparedStatement pstmt = connection.prepareStatement(query);
pstmt.setInt(1, 10);
ResultSet results = pstmt.executeQuery();
```

```python
# Python Example
query = "SELECT * FROM orders WHERE order_id = ?"
cursor.execute(query, (10,))
```

### Step 2: Validate and Sanitize User Input
Ensure that all user-supplied data is validated and sanitized before it is used within your application. This includes not only form submissions, but also URL parameters, cookies, HTTP headers, and any other potential sources of input.

```python
# Python Example
import re
def sanitize(input):
    return re.sub('[^A-Za-z0-9]+', '', input)
```

### Step 3: Encode Data
Encode the output to prevent XSS attacks, any data that originated from user input should be viewed as potentially malicious and handled accordingly.

```java
// Java Example
String user_data = "<b>User Data</b>";
String safe_data = StringEscapeUtils.escapeHtml4(user_data);
```

### Step 4: HTTPOnly and Secure Cookie Flags
This will help to mitigate the most common type of XSS attacks, which is through the theft of session cookies. 

```php
// PHP Example
session_start();
$_SESSION = array("key"=>"value");
$params = session_get_cookie_params();
setcookie(session_name(), '', time() - 42000,
    $params["path"], $params["domain"], 
    $params["secure"], $params["httponly"]
);
```

### Step 5: Content-Security-Policy
To prevent Cross-site Scripting (XSS), use HTTP headers to control the resources which a user-agent is allowed to load for a page.

```bash
# Apache Example
Header set Content-Security-Policy "script-src 'self' example.com"
```

Alternatively, the policy can be defined within a <meta> element inside the <head> tag in your HTML document.

```html
<!-- HTML Example -->
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src https://*; child-src 'none';">
```