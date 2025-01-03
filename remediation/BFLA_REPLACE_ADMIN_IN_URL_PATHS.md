# Remediation for BFLA_REPLACE_ADMIN_IN_URL_PATHS

## Remediation Steps for Broken Function Level Authorization - Vertical Privilege Escalation Test
Broken function level authorization can lead to unauthorized users gaining access to functionalities they should not have access to. One way of exploiting this is through vertical privilege escalation by replacing URL subpaths with the 'admin' keyword. To remediate this, you should implement Role-Based Access Control (RBAC) and thoroughly validate the user role before providing specific functionality.

### Step 1: Implement Role Based Access Control (RBAC).
You need to define roles within your system, and each role should have access to specific functionalities.

```typescript
enum Roles {
  ADMIN = 'admin',
  USER = 'user',
}

const users: Array<{id: string, role: Roles}> = [{
  id: '001',
  role: Roles.USER,
}, {
  id: '002',
  role: Roles.ADMIN,
}];
```

### Step 2: Validate User Role.
Whenever a user makes a request, validate that their role allows them to access the requested functionality. To do this, you should map the roles to the functionalities they can access.

```typescript
const roleToURLMapping: {[key in Roles]: string[]} = {
  [Roles.ADMIN]: ['/admin-url-1', '/admin-url-2'],
  [Roles.USER]: ['/user-url-1', '/user-url-2'],
}
```

### Step 3: Middleware for role validation.

In this step, you should implement a middleware function that checks if the role of the current user has access to the requested functionality.

```typescript
function roleValidationMiddleware(req: Request, res: Response, next: NextFunction) {
  const url = req.path;
  const userId = req.userId; // Assume the user ID is available in the request after authentication.
  const user = users.find(user => user.id === userId);

  if (!user || !roleToURLMapping[user.role].includes(url)) {
    res.status(403).send('Unauthorized');
  } else {
    next();
  }
}
```

Please note that you must replace the code parts to fit your actual use case. The code provided here is only for reference and is written in TypeScript for a NodeJS backend. All strings and variables should be substituted accordingly in a real-world case.