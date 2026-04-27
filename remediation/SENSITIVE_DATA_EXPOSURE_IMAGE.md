

## Remediation Steps for Sensitive Image Data Exposure

Sensitive image data exposure is a serious security issue. Leaked image data might contain personal or confidential information. Here are steps to prevent the exposure of image data.

### Step 1: Serve Images through Authorised Routes
Images should be served through routes that require proper authorisation. For instance, in Node.js one might use express-static to serve static files securely. Here, replace the `public_url` with your protected route and `image_path` with path to your images.

```javascript
var express = require('express');
var app = express();
var path = require('path');

app.use('public_url', isAuthenticated, express.static('image_path'));
```

### Step 2: Implement Proper Access Control
Ensure the application implements proper access control on these routes. This can be done by implementing an `isAuthenticated` middleware function in express before serving any content.

```javascript
function isAuthenticated(req, res, next) {
  if (req.isAuthenticated()) { 
    return next(); 
  }
  res.redirect('/login');
}
```

### Step 3: Save Images in Obscure Locations
Save images not directly in the webroot, but in a location outside of it that isn't directly accessible. Direct references to files should not be predictable or enumerable.