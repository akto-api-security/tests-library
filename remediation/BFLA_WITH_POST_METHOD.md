

## Remediation Steps for Broken Function Level Authorization - Vertical Privilege Escalation

This security issue involves the vertical escalation of privileges through unauthorized use of certain API functions. Exploiting these vulnerabilities can give an attacker more privileges than intended, including administrative ones.

### Step 1: Principle of Least Privilege
Ensure that each user and role in your application is assigned the minimum permissions necessary to perform their functions.

```java
//In Java, use the AccessController and Permission classes to manage user permissions.
AccessController.doPrivileged(new PrivilegedAction<Object>(){
    public Object run(){
        //limit actions here
        return null;
    }
}, new AccessControlContext(new ProtectionDomain[]{
    new ProtectionDomain(null, permissions)
}));
```

### Step 2: Implement Role-Based Access Control

Give different users and roles different levels of access to the API functions based on their roles.

```python
# In Python, use decorators for role-based access control
from flask_login import current_user
from functools import wraps

def role_required(role):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.role == role:
                return 'Access Denied', 403
            return f(*args, **kwargs)
        return decorated_function
    return wrapper
```

### Step 3: Validate Every API Request 

Validate every API request to determine if the user or role making the request has enough permissions to perform the action.

```php
// In PHP, options for request validation can be done through
if (!in_array($user_role, $roles_allowed_for_this_request)) {
    http_response_code(403);
    die('Forbidden');
}
```