

## Remediation Steps for Broken Function Level Authorization - Vertical Privilege Escalation

Broken Function Level Authorization is a security vulnerability where a user can escalate their privilege or access functions they are not supposed to due to lack of robust function level checks in the application. Here are the steps to mitigate this vulnerability:

### Step 1: Implement Authentication before Authorization

Always authenticate users before authorization. Only then can we know the specific privileges the logged-in user has. 

```javascript
var express = require('express');
var router = express.Router();
var UserController = require('./user.controller');
var auth = require('./auth.service');

router.get('/:id', auth.isAuthenticated(), UserController.show);
```

In the above Node.js code, `auth.isAuthenticated()` validates whether the user is authenticated or not before executing `UserController.show`.

### Step 2: Role-Based Authorization

Implement a role-based access control system so that even if a user is authenticated, they can only view the content or call the functions that their role allows.

```javascript
router.put('/:id/password', auth.hasRole('admin'), UserController.changePassword);
```

In the above code, the function `auth.hasRole('admin')` checks if the authenticated user has the role of `'admin'`. Here, the `changePassword` function can only be called by users with the administrator role.

### Step 3: Principle of Least Privilege 

Follow the principle of least privilege. Users should be given the minimal set of privileges they need to perform their task.

```javascript
var user = new User();
user.isAdmin = false;
```

In the above code, when new users are created, by default, they are not given admin rights. 

### Step 4: Always Validate API Endpoints

Always validate your API endpoints. Ensure that they provide the expected functionality and do not inadvertently allow privileged escalation.

```javascript
router.get('/:id', auth.isAuthenticated(), auth.hasRole('admin'), UserController.show);
```

In the above code, only users who are authenticated and have the role of `'admin'` can access the API endpoint.