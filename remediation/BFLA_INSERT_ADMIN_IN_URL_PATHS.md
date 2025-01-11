# Remediation for BFLA_INSERT_ADMIN_IN_URL_PATHS

## Remediation Steps for Broken Function Level Authorization
Broken Function Level Authorization, particularly vertical privilege escalation, is a critical security vulnerability. It can grant unauthorized users access to admin-level privileges by merely altering the URL path. This mechanical error can lead to malicious actors exploiting sensitive endpoints and data which should only be accessible to authorized users.

### Step 1: Ensure User Role Validation
The application should correctly validate the user's role and permissions at every operational level. 

Here's an example in Python using Flask framework:
```python
@app.route('/admin_page')
def admin_page():
    if not current_user.isAdmin: 
        abort(403)
    # usual function implementation
```
The `current_user.isAdmin` part determines if the current user should have access to the function or not. If the user is not an admin, the function will abort the operation and return a 403 HTTP status code indicating forbidden access.

### Step 2: Use Middleware to Authorize Routes
For any routes that require privileged access, apply an authorization middleware to validate the user’s actions.

Example in Node.js Express framework:
```javascript
function isAdmin(req, res, next) {
  if (!req.user.isAdmin) 
    return res.status(403).send('Access Denied.');
  next();
}

app.get('/admin', isAdmin, function(req, res) {
  // Normal functioning here
});
```
The middleware `isAdmin` validates the request. If the user is not an admin, it returns 'Access Denied.', thwarting any attempted security bypass.

### Step 3: Restrict HTTP Methods
Ensure you have set up CORS correctly to restrict HTTP methods and prevent unauthorized API calls.

```javascript
app.use(cors({
  origin: 'yourdomain.com',
  optionsSuccessStatus: 200, 
  methods: "GET,HEAD,PUT,PATCH,POST,DELETE"
}));
```
Remember that a good security practice is to work on the principle of least privilege. Only extend permissions on a need-to-know basis.