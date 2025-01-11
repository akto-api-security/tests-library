# Remediation for ID_WRAP_ARRAY_OF_PARAMS_JSON_BODY_INTEGER_VAL_PATCH

## Remediation Steps for BOLA: Turning JSON Param into Array of Params with Integer

BOLA (Broken Object Level Authorization) is a security issue where an attacker can manipulate object identifiers to access other objects. In the scenario you described, a JSON param may be converted into an array of params with integers, enabling unauthorized access through APIs using the PUT/PATCH methods.

### Step 1: Validate Request Parameters
Always validate the request parameters on the server-side. The process of validation should include checking types, lengths, and a range of expected parameter values. Here, ensure that a JSON parameter isn't getting converted to an array of parameters.
```java
if (!(param instanceof Map)) {
    throw new IllegalArgumentException("Expected a JSON object, got " + param);
}
```

### Step 2: Implement Proper Authorization 

Make sure every API request runs through proper authorization checks like verifying the user's role and privileges before providing object access.

```java
if(user.getRole().hasPermission("UPDATE", object)){
    object.update(newValues);
} else {
    throw new UnauthorizedException();
}
```

### Step 3: Limit Object Access

Restrict access to objects by only allowing users to access their objects and limit data returned by the PUT/PATCH methods. 

```java
if(user.getOwnedObjects().contains(object)){
    object.update(newValues);
} else {
    throw new UnauthorizedException();
}
```
