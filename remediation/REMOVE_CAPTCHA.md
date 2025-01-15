# Remediation for REMOVE_CAPTCHA

## Remediation Steps for Removing Captcha from Request

Removing captcha from request can lead to several security vulnerabilities such as bot spamming, DDoS attacks, and brute-force attacks. To fix this security issue, re-add the captcha to the form by following these instructions.

### Step 1: Add back Captcha in HTML Form
Add the Captcha field back into your HTML form. Here's an example with Google's reCAPTCHA.

```html
<form method="post" action="someURL">
    <!-- other input fields -->
    <div class="g-recaptcha" data-sitekey="your-site-key"></div>
    <input type="submit" value="Submit">
</form>
<script src='https://www.google.com/recaptcha/api.js'></script>
```

Your site key will be provided by reCAPTCHA during the setup process.

### Step 2: Validate Captcha in Server-Side Code

Remember, you also need to check the captcha responses server-side, as client-side checks can be bypassed. Here's an example in Python using Flask and the 'requests' library.

```python
import requests
from flask import Flask, request

app = Flask(__name__)
RECAPTCHA_SECRET_KEY = 'your-secret-key'

@app.route('/submit', methods=['POST'])
def submit():
    captcha_response = request.form.get('g-recaptcha-response')

    if is_human(captcha_response):
        # process the form
        pass
    else:
        # return error message
        pass

def is_human(captcha_response):
    payload = {'response': captcha_response, 'secret': RECAPTCHA_SECRET_KEY}
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', payload)

    return response.json()['success']
```

The server must validate the user's captcha response with the reCAPTCHA API. Remember to replace 'your-secret-key' with your reCAPTCHA secret key.