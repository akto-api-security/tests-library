

## Remediation Steps for SSRF Via Scripts Tags With Redirect URLs on Azure

Server Side Request Forgery (SSRF) through script tags is a potential vulnerability chiefly found in web applications. The attacker can gain control of server resources with replaceable parameters in an Azure environment. Below are the remediation steps to mitigate this vulnerability. 

### Step 1: Validate Input
Validate and sanitize input to prevent unwanted tags or scripts from being injected into parameters. Here is an example code to validate input in Python:

```python
import re
def validate_input(input):
    # Removes JavaScript tags
    sanitized_input = re.sub('<.*?>', '', str(input))
    return sanitized_input
```

### Step 2: Use a SafeList For URL Redirection
Ensure that allowed redirects are only to known and explicit URLs in your application. Here is an example in Javascript:

```javascript
var safeUrls = ['https://known.url1.com', 'https://known.url2.com'];
if(safeUrls.indexOf(url) != -1) {
    response.sendRedirect(url);
}
```

### Step 3: Block Access to Azure Metadata Service
Explicitly block SSRF attempts to the Azure Metadata Service URL. Here is an example Python code snippet using a URL extraction library:

```python
import tldextract
def validate_url(url):
    extracted = tldextract.extract(url)
    if 'metadata' in extracted and 'azure' in extracted:
        raise ValueError('Invalid URL: SSRF attempt detected')
    else:
        return url
```

### Step 4: Use Libraries That Mitigate SSRF
Use server-side libraries like Azure Blob storage SDK that helps prevent SSRF issues associated with callbacks or redirects.