

## Remediation Steps for Missing HTTP Response Headers 
Missing HTTP response headers could potentially expose sensitive client information to cyber attacks. A proper inclusion of HTTP security headers strengthens the overall security of any web application by applying various security policies.

### Step 1: Include Essential HTTP Headers
Here is a neat python application code showing how to include HTTP response headers using the Flask web framework. 

```python
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def set_headers():
    response = make_response("Hello World")
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

if __name__ == '__main__':
    app.run(debug=True)
```    

Here is what each of the 5 headers are doing:

- `Strict-Transport-Security`: This ensures that the browser always uses HTTPS.
- `Content-Security-Policy`: This prevents a wide range of attacks, including Cross-site scripting and other cross-site injections.
- `X-Content-Type-Options`: This prevents attacks based on MIME-type mismatch.
- `X-Frame-Options`: This provides clickjacking protection.
- `X-XSS-Protection`: This is to enable the Cross-site scripting (XSS) filter in your browser.

### Step 2: Test HTTP Headers
Use online tools like [SecurityHeaders](https://securityheaders.com) to analyze the HTTP response headers of your website.