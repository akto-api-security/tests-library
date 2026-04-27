

## Remediation Steps for Broken Function Level Authorization

Broken Function Level Authorization is a common security issue where certain functions within an application do not have proper authorization checks in place, which allow a lower-privileged user to perform functions reserved for higher-privileged users, like an admin. This is referred to as Vertical Privilege Escalation.

To remediate this issue, let's follow the steps below using Node.js and the Express.js Framework as an example:

### Step 1: Incorporate Middleware to Check for Required Permissions

In this step, you will need to include a middleware function that will verify authorization before the function is accessed.

The middleware can look something like this:

```javascript
function hasRequiredPermissions(requiredPermissions) {
   return function(req, res, next) {
      const userPermissions = req.user.permissions;
   
      const allPermissionsPresent = requiredPermissions.every(permission => {
         return userPermissions.includes(permission);
      });
   
      if (allPermissionsPresent) {
         return next();
      } else {
         res.status(403).json({ message: "Insufficient permissions" });
      }
   }
}
```

### Step 2: Apply Middleware to Relevant Routes

Apply the middleware function to relevant router endpoints using the `.use()` function.

```javascript
router.use('/admin', hasRequiredPermissions(['ADMIN']));
```

### Step 3: Implement Proper User Roles and Permissions

Ensure that user accounts are assigned the correct permissions during creation or modification.

```javascript
const createUser = (username, password, role) => {
  // Create a new user
  const user = new User({
    username,
    password,
    role
  });

  // Save the user
  user.save()
    .then(() => console.log("User created"))
    .catch(error => console.log("Error: ", error));
};

// A function to assign permissions based on user roles
const assignPermissions = (role) => {
  switch(role) {
    case 'ADMIN':
      return ['READ', 'WRITE', 'DELETE', 'ADMIN'];
    case 'USER':
      return ['READ'];
    default:
      return [];
  }
};
```

### Step 4: Test Your Implementation

Use Authorization Testing tools or manual testing techniques to verify proper authentication is now being accomplished for function level authorization. 

```bash
curl --request GET \
  --url http://localhost:3000/admin \
  --header 'authorization: Bearer {YOUR_TOKEN}'
```