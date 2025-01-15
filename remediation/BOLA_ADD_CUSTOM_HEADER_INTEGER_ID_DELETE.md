# Remediation for BOLA_ADD_CUSTOM_HEADER_INTEGER_ID_DELETE

## Remediation Steps for Exploiting BOLA (Broken Object Level Authorization) By Adding Custom Header with Integer IDs 

Broken Object Level Authorization (BOLA) exploitation is a severe security vulnerability. Attackers can manipulate IDs within the HTTP headers or API requests to gain unauthorized access to resources. They may use this to make unauthorized DELETE requests, threatening the integrity of the system. Here is how this can be remediated:

### Step 1: Validate User Roles and Permissions
Before you allow an operation on any object, double check if the user has access to this object and if they are allowed to perform the requested action. You could use Java Spring Security for this.

```java
@GetMapping("/api/object/{objectId}")
public ResponseEntity<Object> getObject(@PathVariable Integer objectId, UserPrincipal currentUser) {
    Object object = objectService.findById(objectId);

    if (!currentUser.canAccessObject(object)) {
        throw new AccessDeniedException("You are not authorized to access this resource.");
    }

    return ResponseEntity.ok(object);
}
```
### Step 2: Enforce Access Control
Enforce Direct Object Reference (IDOR) protections at the API gateway level by validating request headers and parameters against the authenticated user context. Here is an example using Node.js Steps.
```javascript
app.delete('/api/resource/:id', (req, res, next) => {
  authMiddleware(req, res, next);
  idValidatorMiddleware(req, res, next);
  deleteResource(req, res, next);
});
```