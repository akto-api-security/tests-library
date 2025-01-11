# Remediation for BIG_REDIRECTS_SCAN

## Remediation Steps for Big Redirects Scan Issue
A Big Redirect vulnerability involves sending large amounts of data in redirection response effectively affecting application performance or even triggering possible overflow issues.

### Step 1: Review the Redirect Methods in Code
Review all server-side redirect methods in your code. An example of a suspect redirect in Python would look like:

```python
def redirect(request):
    url = request.args.get('url')
    return redirect(url)
```

### Step 2: Avoid Open Redirects
Don't allow anyone to provide the full URL to redirect. Instead, restrict the redirection based on specified paths or endpoints. 

For instance in Python Flask:
  
```python
@app.route('/redirect')
def handle_redirect():
    url = request.args.get('url')
    if url and url.startswith('/'):
        return redirect(url)
    else:
        return 'Invalid URL'
```
In the example above, only redirects to same origin are allowed.

### Step 3: Implement Size Limit for the Redirect
Implement some sort of size check for the redirect response. If the response size exceeds the limit, abort the redirect. This will make sure the system does not become overburdened with large redirect data volume. Here's a Python Flask example:

```python
@app.route('/redirect')
def handle_redirect():
    url = request.args.get('url')
    if url and url.startswith('/') and len(url) < 1024:
        return redirect(url)
    else:
        return 'Invalid URL'
```