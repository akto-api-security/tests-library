

## Remediation Steps for Python Flask-Security Open Redirect
Open Redirect is a security issue where a user can be redirected to an untrusted site without their knowledge. It occurs when an application does not validate if the redirect target is a trusted server or not.

In Python Flask-Security, you can mitigate such risks using a safe redirect check. This ensures all redirections are to trusted and secure locations.

### Step 1: Install Flask-Security Package
``` bash
pip install flask-security
```

### Step 2: Implement Safe Redirect Check
In your application, you need to implement a check for the redirect target. The `is_safe_url` helps ensure that the target sent as part of the request is safe.

Create and use a function, such as the following:

``` Python
from urllib.parse import urlparse, urljoin
from flask import request, url_for, redirect

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

@app.route('/login', methods=['POST'])
def login():
    target_url = request.form.get('next')
    if not is_safe_url(target_url):
        return flask.abort(400)
    # continue with login process
    ...

@app.route('/dashboard')
@flask_login.login_required
def dashboard():
    return render_template('dashboard.html')
```
This code block creates a function `is_safe_url` that verifies if the redirect URL sent as part of login is safe or not. If it's not safe, it aborts the process sending a 400 Bad Request.

By taking control of the redirection mechanism in your application, you can mitigate the risk of Python Flask-Security Open Redirect Vulnerability. 

NOTE: Always check `next` request parameter to ensure the redirection URL is safe.