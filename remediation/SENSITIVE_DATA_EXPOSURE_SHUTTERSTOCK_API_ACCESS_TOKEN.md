

## Remediation Steps for Shutterstock API Access Token Exposure
Sensitive data exposure is a serious security risk. If the Shutterstock API Access Token is exposed, it could lead to unauthorized usage, possibly causing financial loss or data breach. Follow the steps below to secure your API Access Token:

### Step 1: Store Tokens securely
Avoid hardcoding your API Access Token directly in your code. Instead, store them in environment variables or other secure means such as key vaults.

```javascript
// Bad Practice
const ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN';

// Good Practice
const ACCESS_TOKEN = process.env.SHUTTERSTOCK_API_ACCESS_TOKEN;
```

In the example above, replace `'YOUR_ACCESS_TOKEN'` with the actual access token value in your environment variable.

### Step 2: Restrict Token Permissions 
Ensure that your Shutterstock API Access Token only has necessary permissions. Avoid creating tokens with full access, unless absolutely necessary.

### Step 3: Token Refreshment/Rotation
In Shutterstock API, there is no direct way to manually expire an access token but the entire App can be removed to void all access tokens. This is not a good practice as it can disrupt all existing services. Instead, regular renewal and rotation of access tokens can lower chances of misuse, should they be leaked.

### Step 4: Use HTTPS
Ensure all API calls are via HTTPS (not HTTP) to prevent Man-In-The-Middle attacks.

```javascript
const axios = require('axios');
axios({
    method: 'get',
    url: 'https://api.shutterstock.com/v2/images/search',
    headers: {
      'Authorization': `Bearer ${process.env.SHUTTERSTOCK_API_ACCESS_TOKEN}`
    },
    params: {
      query: 'puppies',
      image_type: 'photo',
      orientation: 'horizontal',
      per_page: 50,
    }
  })
```