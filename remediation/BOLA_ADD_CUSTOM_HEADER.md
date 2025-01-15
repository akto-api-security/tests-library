# Remediation for BOLA_ADD_CUSTOM_HEADER

## Remediation Steps for BOLA (Broken Object Level Authorization) Exploitation by Adding Custom Header
BOLA (Broken Object Level Authorization) is a security vulnerability that can be exploited when an attacker manipulates object id's in the endpoint path. Using unauthorized access techniques such as adding custom headers can exacerbate the problem. The remediation steps are mentioned below -

### Step 1: Validate User Authorization
Always validate if a user is authorized to access the object/data they are requesting. This can be done on server-side using any server-side language, for example in Python with Flask framework:

```python
@app.route('/object/<objectId>', methods=['GET', 'POST'])
def handle_object(objectId):
    #Assuming getCurrentUser() returns the currently logged in user
    user = getCurrentUser()
    
    #Assuming userHasAccess() checks if the user has necessary permissions
    if not userHasAccess(user, objectId):
        return jsonify({"error": "Unauthorized access"}), 401
    
    #Your code when user is authorized...
```

### Step 2: Use Random and Unpredictable GUIDs
For your object IDs, use UUIDs or GUIDs which are neither predictable nor sequential.

```python
import uuid

# Generating a random UUID
objectId = uuid.uuid4()
```

### Step 3: Include User ID in the Path and check authorization
To ensure the right user is accessing his/her objects/data, include user id in the path and always check if the user id matches with the currently logged in user id. This prevents one user accessing another user's objects.
```python
@app.route('/user/<userId>/object/<objectId>', methods=['GET', 'POST'])
def handle_user_object(userId, objectId):
    # Assuming getCurrentUser() returns the currently logged in user
    currentUser = getCurrentUser()

    if currentUser.userId != userId:
        return jsonify({"error": "Unauthorized access"}), 401

    # Your code when user is authorized...
```

