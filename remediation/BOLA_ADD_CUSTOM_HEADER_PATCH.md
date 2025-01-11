# Remediation for BOLA_ADD_CUSTOM_HEADER_PATCH

## Remediation Steps for BOLA Exploitation via Custom Header for Unauthorized Access for PATCH/PUT method APIs

Attacks exploiting Broken Object-Level Authorization (BOLA) vulnerabilities can lead to unauthorized access of web server data, potentially causing significant damage.

Here are steps you can take to mitigate these vulnerabilities:

### Step 1: Use a Secure Policy Design
The primary security measure against these vulnerabilities is adopting a secure policy that limits the role played by user-controlled inputs (headers, parameters). Avoid using these inputs to control access rights.

```java
// Instead of using an user-controlled input, use a system-controlled internal value.
String userId = getAuthenticatedUserIdFromJWTToken();
User authorizedUser = userRepository.findUserById(userId);
```

### Step 2: Always Validate and Authorize User Requests
For each API endpoint that receives user input, make sure the user is authenticated and authorized to make the request.

```java
// Check if the authenticated user owns the object or has permission to modify it
if(authorizedUser.hasPermissionToModify(object) || authorizedUser.owns(object)) {
    object.update(input);
} else {
    throw new UnauthorizedException();
}
```

### Step 3: Setup Proper Logging
Audit logs help you monitor API requests and detect any anomalies indicating a potential attack. They can also aid in identifying compromised data in the event of an attack.

```python
import logging

def process_request(request):
    try:
        # Process request
    except UnauthorizedException:
        logging.error(f"Unauthorized PATCH/PUT attempt by user: {request.user}")
        raise
```