

## Remediation Steps for Exploiting BOLA (Broken Object Level Authorization) by Inserting User IDs in URL Path for Unauthorized Access for PUT/PATCH Based APIs

Broken Object Level Authorization vulnerabilities can allow attackers to bypass authorization and gain access to resources directly. In the case of exploiting these vulnerabilities by inserting User IDs in the URL Path for PUT/PATCH based APIs, there are some steps to remediate such practice.

### Step 1: Avoid exposing sensitive ID in URL path

Ensure that user IDs or any sensitive identifications are not exposed in API URLs. If necessary, use a surrogate key to reference an object instead of the direct database key.

```java
// BAD PRACTICE: Exposing user Id in URL
@RequestMapping(value = "/api/user/{id}", method = RequestMethod.PUT)
public ResponseEntity<?> updateUser(@PathVariable("id") long id) {
    //... codes to update user
}

// GOOD PRACTICE: Avoid exposing user Id in URL
@RequestMapping(value = "/api/user", method = RequestMethod.PUT)
public ResponseEntity<?> updateUser(@RequestHeader("user-id") long id) {
    //... codes to update user
}
```

### Step 2: Implement Access Control

Always authorize and verify if a user has the adequate permissions to access or modify the resources or data. If not, deny the request.

```java
public ResponseEntity<?> updateUser(@RequestHeader("user-id") long id) {
    if (hasPermission(id)) {  // Checks if the user has the right permission
        //... codes to update user
    } else {
        return new ResponseEntity<>("Unauthorized", HttpStatus.UNAUTHORIZED);
    }
}
```

### Step 3: Validate User

Make sure to validate the user from their server-side session and map it to their own set of data.

```java
public ResponseEntity<?> updateUser(@RequestHeader("user-id") long id) {
    User user = getUserFromSession();  // Gets user from server-side session

    if (user.getId() != id) {
        return new ResponseEntity<>("Unauthorized", HttpStatus.UNAUTHORIZED);
    }

    //... codes to update user
}
```