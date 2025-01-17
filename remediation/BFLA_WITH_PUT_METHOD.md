

## Remediation Steps for Broken Function Level Authorization - Vertical Privilege Escalation

Broken Function level authorization is a critical security issue. Without aptly managing function level authorizations, malicious users could escalate their privileges and gain unauthorized access to sensitive data and functionalities.

### Step 1: Validate User Roles and Privileges

In every function that requires some form of authorization, verify the role and privileges of the authenticated user.

```python
def function_requiring_auth(user, required_privilege):
  if not user.has_privilege(required_privilege):
    raise Exception("Unauthorized")

function_requiring_auth(active_user, "admin")
```

### Step 2: Implement Role-Based Access Control (RBAC)

An efficient way of handling this issue is by implementing Role-Based Access Control (RBAC). With RBAC, you can specify exactly what actions a particular role can perform.

```python
class User:
  def __init__(self, roles):
    self.roles = roles

  def has_role(self, required_role):
    return required_role in self.roles

def function_requiring_role(user, required_role):
  if not user.has_role(required_role):
    raise Exception("Unauthorized")
```

### Step 3: Apply Principle of Least Privilege

Ensure that users have the minimum levels of access – or permissions– that they need to perform their work functions.

### Step 4: Consistent Auditing and Updating of User Access Controls

Regularly audit user roles and access controls, and update them as required to prevent unauthorized access.

```python
def audit_roles(user):
  # Perform auditing on user roles
  pass

def update_roles(user, new_roles):
  # Update the roles of the user
  user.roles = new_roles
```

In case of using PUT, a method when updating user privileges or roles make sure the request's body or params are properly validated to ensure it's not manipulated.

```python
def put_role(user, role):
  if not role_is_valid(role):
    raise Exception("Unauthorized")

  # If valid, proceed with updating the role
  user.roles = role
```