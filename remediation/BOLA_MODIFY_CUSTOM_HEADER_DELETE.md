# Remediation for BOLA_MODIFY_CUSTOM_HEADER_DELETE

## Remediation Steps for Exploiting BOLA by Fuzzing Custom Header for Unauthorized Access
Exploiting BOLA (Broken Object Level Authorization) by fuzzing custom header for unauthorized access, especially for DELETE based APIs, is an serious security vulnerability. If not properly addressed, attackers may gain unauthorized access to modify or delete resources.

### Step 1: Validate User Authority
The very first step is to validate the user's authority to perform a resource modification or deletion.
```javascript
var canUserDelete = function(user, resource) {
  var role = user.role;
  var resourceOwner = resource.owner;
  // replace the following logic with your actual authorization system
  return role === 'admin' || user.id === resourceOwner;
}
if (!canUserDelete(user, resource)) {
  return 'Unauthorized access';
}
```

### Step 2: Safely Verify Object Ownership 
In cases where the users are allowed to manipulate only their own resources, be sure to verify object ownership safely.
```javascript
const userOwnsResource = (userId, resourceId) => {
  const resource = resources.find(r => r.id === resourceId);
  return resource && resource.ownerId === userId;
};
```

### Step 3: Harden API Against Fuzzing
To prevent attackers from guessing API endpoints through fuzzing, use randomness in API keys and methodically change them.

```python
import secrets
api_key = secrets.token_hex(16)
```
### Step 4: Employ Rate Limiting
Limit the frequency of DELETE requests a single user or IP address can make in a given amount of time.

```python
from flask_limiter import Limiter
limiter = Limiter(app, key_func=get_remote_address)
@app.route("/delete_resource", methods=["DELETE"])
@limiter.limit("5/minute") # limit to 5 requests per minute
def delete_resource():
    # your delete logic here
```

### Step 5: Regular Audit and Update
Make it a routine to conduct regular security audits and updates to your authorization and authentication systems. Remember to also log and monitor DELETE requests to prevent unauthorized access and modifications. 

```log
WARNING - DELETE request made on 2022-03-30 13:33:28 by user 1234, IP address 192.168.1.2
```

Regular updates and audits will ensure your systems are up-to-date with the recent security practices and no unauthorized deletions have been successful.