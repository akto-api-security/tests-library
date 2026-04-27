

## Remediation Steps for Exploiting BOLA via UserIDs in URL Path

Exploiting Broken Object Level Authorization (BOLA) by inserting User IDs in the URL path is a serious security concern. Attackers can gain unauthorized access to DELETE contracts by manipulating the ID in the route path.

### Step 1: Avoid Direct Object References
Instead of using the actual ID of objects in the URLs, use indirect references.

```java
// In a java context
String userId = session.getAttribute("userId");
User user = database.getUser(userId);
user.delete();
```

### Step 2: Use JWT based Authentication
Ensure every API uses JWT token for user authentication, and these tokens should be stored securely.

```java
// Generate a JWT
String token = Jwts.builder().setSubject(?userId?).signWith(key).compact();

// Later to validate the token and extract the userId
Claims claims = Jwts.parserBuilder().setSigningKey(key).build().parseClaimsJws(token).getBody();
String userId = claims.getSubject();

// Continue processing with belove code
User user = database.getUser(userId);
user.delete();
```

### Step 3: Implement Role-based Access Control (RBAC)
Implement RBAC to enforce access controls. This ensures only authorized users can access the DELETE APIs.

```java
// Validate user role before deleting 
if(user.role.equals("admin")) {
    String objectID = request.getParameter("objectID");
    Object object = database.getObject(objectID);
    object.delete();
} else {
    throw new AccessDeniedException("Not authorized");
}
```