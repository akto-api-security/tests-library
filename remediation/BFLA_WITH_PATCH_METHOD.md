# Remediation for BFLA_WITH_PATCH_METHOD

## Remediation Steps for Broken Function Level Authorization - Vertical Privilege Escalation

Broken function level authorization - vertical privilege escalation is a critical security issue. This issue happens when a user is able to gain access to functionalities belonging to a user with a higher privilege level by manipulating the method used in an HTTP request, such as sending a PATCH request instead of a GET request.

### Step 1: Authorization Checks

The application should always perform the function level access control check at the server side every time a function is accessed. 

If you are using an Express.js server for instance, it might look something like this:

```javascript
app.patch('/api/path', authController.verifyToken, authController.allowIfLoggedin, authController.grantAccess('updateAny', 'resource'), (req, res, next) => {
 // function logic here
});
```

Here, `authController.verifyToken` ensures the token provided in the request is valid, `authController.allowIfLoggedin` checks if the user is logged in, and `authController.grantAccess('updateAny', 'resource')` ensures that the logged in user has the access right to update any resource.

### Step 2: Least Privilege

Enforce the principle of least privilege. Each user should be given the least amount of privilege needed to perform his/her tasks. 

### Step 3: Sever-side validation

Always replicate all client-side validation on server side. Apply the same validation of input and enforce authentication and authorization checks again, including data from API and service endpoints that may not have a user interface.

### Step 4: Regular Audit and Update

Ensure your function level authorization logic is regularly updated and tested for any possible security loopholes. Continuous integration and delivery, including regular audits, will help maintain a secure environment.