# Remediation for BOLA_ADD_CUSTOM_HEADER_DELETE

## Remediation Steps for Exploiting BOLA by adding Custom Header for Unauthorized Access for DELETE method APIs
Broken Object Level Authorization (BOLA) often allows attackers to bypass authorization and perform unauthorized tasks. This issue could lead to huge data theft and unwanted data manipulation.

### Step 1: Validate User Authorization
Regardless of the method in use (GET, POST, PUT, DELETE, etc.), always validate if the user is authorized to perform the operation. Implement a strong mechanism to validate User ID or Token.

Java-based solution:
```java
public boolean isUserAuthorized(User user, String resource) 
{
    //implement your authorization logic here
    return false;
}
```

### Step 2: Enforce Object Level Authorization
Enforce object level authorization on each individual resource, not solely on the URI. Always ensure control enforcement must not be bypassed by simply replacing ID in the URI.

Java-based solution:
```java
public boolean isAccessAllowed(User user, MyResource resource)
{
    //the implementation logic of this method should verify if the user owns 
    //the resource or has the needed permissions on it
    return false;
}
```

### Step 3: Treat Server Data as Untrusted
Whenever dealing with server data, handle it as untrusted. Never solely rely on requests payload to perform client operations, for it may be tampered. 

Java-based solution:
```java
public MyResource getResource(long resourceId, User user) 
{
    // fetching resource from the database
    MyResource resource = resourceDAO.getById(resourceId)
    
    if (!isAccessAllowed(user, resource)) 
    {
        throw new UnauthorizedException();
    }
    
    return resource;
}
```

### Step 4: Regular Audit and Update
Always ensure to regularly audit and update your security systems, patches, and hiccups. Keep up to date with new threats and vulnerabilities, and counter them proactively.

```bash
# Appropriate command for security audits & updates vary greatly depending on system & application specifics.
# Implement a strategy involving regular audits, updates and security scans.
``` 

**Endnote**: Don't forget to include error handling, logging the necessary information, and keeping the user's experience in mind while designing your checks.