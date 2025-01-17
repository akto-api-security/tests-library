

## Remediation Steps for Old API Version Test for Detecting Shadow APIs
Shadow APIs refer to APIs that remain in the system unnoticed and no longer maintained or updated. They pose as security risks as hackers can exploit them. Hence, it's crucial to regularly discover and manage these APIs. Below are the steps to mitigate this issue:

### Step 1: Discover shadow APIs
Use automated discovery tools or scanner programs to detect shadow APIs. A regular system audit can also be helpful.

```bash
# Using npm install command for installing Swagger Stats
npm install swagger-stats

# Using the express app for API
var swStats = require('swagger-stats');
var express = require('express');
var app = express();
app.use(swStats.getMiddleware({}));
```

### Step 2: Update or Deprecate Old API Versions
If the old API versions are not required, you should deprecate and remove them from your system.

```javascript
const express = require('express');
const router = express.Router();

// Example of version control
router.use('/api/v1', require('./v1'));
router.use('/api/v2', require('./v2'));

app.use(router);
```

### Step 3: Implement Access Control
Ensure proper authentication mechanisms are in place before allowing access to any API in your system.

```javascript
app.use('/api/', function(req, res, next) {
    if (!req.user) {
        res.status(401).json({error: 'Unauthorized access'});
    } else {
        next();
    }
});
```