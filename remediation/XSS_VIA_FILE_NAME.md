# Remediation for XSS_VIA_FILE_NAME

## Remediation Steps for XSS by Changing File Names

Cross-Site Scripting (XSS) attacks via file names can pose serious risks. These attacks can occur when an attacker can manipulate a file name that is eventually rendered in HTML pages without being properly escaped or sanitized. 

### Step 1: Encode/Escape User Inputs
Ensure at the point of rendering, all user inputs are properly escaped to prevent execution of any malicious scripts.

You should apply HTMLEncode to the filename before displaying it in the web page.

Here is an example in Java:
```java
import org.apache.commons.text.StringEscapeUtils;

String unsafeFileName = "unsafe_file_name";
String safeFileName = StringEscapeUtils.escapeHtml4(unsafeFileName);
```
In the above case, `escapeHtml4` method will ensure that any HTML control characters present in the filename are escaped properly, rendering them harmless.

This is an equivalent for C#:
```csharp
string unsafeFileName = "unsafe_file_name";
string safeFileName = System.Net.WebUtility.HtmlEncode(unsafeFileName);
```

### Step 2: Validating File Names
Always validate the file names before accepting them into your system. This can include checks for length, type, and checks against a whitelist of allowed characters/patterns.

Here is an example in Python:
```python
import re

def is_filename_safe(filename):
    return re.match(r'^[\w\-. ]+$', filename) is not None
```
In the above Python sample, a regular expression is used to ensure that the filename only contains word characters, "-" or ".", and spaces. If the filename contains any other characters, it will be deemed as unsafe.

### Step 3: Use Content Security Policy
Implementing Content Security Policy (CSP) can help to mitigate a large portion of XSS attacks including this one. CSP allows you to specify the domains that the browser should consider as valid sources of executable scripts.

```python
response["Content-Security-Policy"] = "default-src 'self'"
```
By setting the CSP header in the response object, we are instructing the browser that it should only execute scripts from the same domain as the domain for the website.

### Step 4: Regular Audits and Updates
Regularly audit your codebase for potential XSS vulnerabilities and keep your libraries, dependencies and frameworks updated. Use static code analyzers which can help you identify potential security flaws.