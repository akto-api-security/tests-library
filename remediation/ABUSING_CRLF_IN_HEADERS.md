

## Remediation Steps for HTTP Header Abuse using CRLF Injection

HTTP Header Abuse using CRLF (Carriage Return Line Feed) Injection is a security threat that manipulates the HTTP headers which breach the communication protocol leading to potential security implications such as HTTP response splitting and other forms of web applications attack.

### Step 1: Validate and sanitize user inputs

The first remediation step is to validate and sanitize all the user inputs and data received from third parties. Below is an example using Python.

```python
import re

def sanitize(input):
    return re.sub('\r|\n', '', input)
```

### Step 2: Use libraries that automatically prevent CRLF injection

Various libraries are available that automatically prevent CRLF injection, such as OWASP Encoder for Java.

```java
String safe = ESAPI.encoder().encodeForHTTP( userInput );
```

### Step 3: Turn off HTTP Header splitting 

If your web server allows, turn off HTTP Header splitting. Below is an example of how to do this in Nginx by using ignore_invalid_headers directive.

```nginx
server  {
   ...
   ignore_invalid_headers on;
   ...
}
```