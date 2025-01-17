

## Remediation Steps for Exploiting BOLA (Broken Object level Authorization) by Fuzzing Custom Header with Integer for Unauthorized Access with DELETE based APIs

Broken Object Level Authorization exploits occur when an API endpoint is vulnerable to manipulation of ID values that belong to objects. Fuzzing of integer in custom headers can be exploited to bypass authorization systems and gain access to unauthorized endpoints of DELETE based APIs. 

### Step 1: Validate Object's Ownership
Ensure that validation check is present for verifying object's ownership before granting access. One can use the source code below written in Python as an example:

```python
def is_owner(user, object_id):
    object = get_object(object_id)
    return user.id == object.owner_id
...
def delete_object(user, object_id):
    if not is_owner(user, object_id):
        raise Unauthorized("You do not have the necessary permissions to delete this object")
    perform_delete(object_id)
```

### Step 2: Implement Strong Authorization Checks
Always implement strong authorization checks on every single API request. This can help prevent unauthorized access of data.
The following JavaScript example can provide a rough idea:

```javascript
router.delete('/delete/:id', function(req, res) {
    let id = req.params.id;
    let token = req.headers.authorization;
    
    // Verifying the given token from the headers
    jwt.verify(token, secretKey, function(err, decoded) {
        if (err) return res.json({status: false, message: 'Failed to authenticate token.'});
        if(decoded.id !== id) return res.json({status: false, message: 'User is not authorized'});
        
        // Delete operation
        data.delete(id).then(resolve => {
            res.json({status: true, message: "Data deleted successfully"})
        }).catch(reject => {
            res.json({status: false, message: "Data deletion failed"})
        })
    });
});
```

In this code, each request comes with a token in headers that is used to verify the ownership of the object that is to be deleted. 

### Step 3: Apply Principle of Least Privilege
Always stick to the "Principle of Least Privilege" where every module (such as a process, a user, or a program, depending on the subject) must be able to access only the information and resources that are necessary for its legitimate purpose. This limits the scope of potential damage.