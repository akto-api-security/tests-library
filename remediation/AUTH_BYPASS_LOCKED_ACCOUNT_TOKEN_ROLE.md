# Remediation for AUTH_BYPASS_LOCKED_ACCOUNT_TOKEN_ROLE

## Remediation Steps for Authentication Bypass with Locked Account Token Role Test

Authentication Bypass with Locked Account Token Role Test is a significant security issue. This situation arises when a user manages to surpass the authentication process for a locked account using an account token. By doing this, they may gain unauthorized access to sensitive data or resources. The steps below outline how to patch this vulnerability.

### Step 1: Implement Account Lockout Constraints

The first measure to rectify this issue entails implementing account lockout policies. In your authentication process, add a feature that locks an account after a predefined number of failed login attempts.

```java
if (loginAttempts > MAX_ATTEMPTS) {
    userAccount.setLocked(true); 
}
```

### Step 2: Invalidate Account Tokens after Locking

Once an account is locked due to many failed login attempts, make sure to invalidate all active tokens for that account immediately.

```java
if (userAccount.isLocked()) {
    userAccount.invalidateAllTokens();
}
```

### Step 3: Token Verification

Ensure that any action involving tokens requires the token validity to be checked. If the token pertains to a locked account, the action should be denied.

```java
if (tokenService.isTokenValid(token)) {
    if(userAccount.isLocked()) {
        throw new AccountLockedException("This account is locked");
    }
    // continue processing the request.
} else {
    throw new InvalidTokenException("The token is invalid");
}
```