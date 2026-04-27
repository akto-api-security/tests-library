

## Remediation Steps for User Enumeration using Locked Account Role
User Enumeration using Locked Account Role is a security issue where an attacker is able to determine valid users based on the response from a locked account. This knowledge can aid an attacker in hacking attempts. To mitigate this, we should unify the message returned for either case so that an attacker is not able to confirm whether an account is locked or not.

### Step 1: Generic Error Response
Rather than returning specific error messages such as "account not found" or "account is locked", return a generic error message such as "invalid username or password". This way, the attacker is not given any information about whether the account exists or if it is locked.

```java
@PostMapping("/login")
public String login(@RequestParam String username, @RequestParam String password) {
    User user = userService.findUserByUsername(username);
    
    if (user == null || !passwordEncoder.matches(password, user.getPassword())) {
        throw new LoginFailedException("Invalid username or password");
    }

    if (user.isLocked()) {
        throw new LoginFailedException("Invalid username or password");
    }
    
    // proceed with authenticated session
    return "redirect:/home";
}
```

### Step 2: Implementing Account Lock 
If you don't have account lock implementation yet, make sure to take care when implementing the user lock functionality. Don't reveal to an unauthenticated user that the account is locked.

```java
public class LoginFailedException extends RuntimeException {

    public LoginFailedException(String message) {
        super(message);
    }
}
```

### Step 3: Login Attempts and Account Lock
Account lock policies can also be useful to prevent brute force attacks. After a certain number of failed attempts, the account is locked, and the user must have it unlocked by an administrator.

Please remember that you should still return the general error message "Invalid username or password" even if the account is locked due to failed attempts.

```java
public User authenticate(String username, String password) throws LoginFailedException {

    User user = userDao.findByUsername(username);
    
    if (user != null) {

        if (user.isLocked()) {
            throw new LoginFailedException("Invalid username or password");
        }

        if (!passwordEncoder.matches(password, user.getPassword())) {
            user.incrementLoginAttempts();
            
            if (user.getLoginAttempts() > MAX_LOGIN_ATTEMPTS) {
                user.setLocked(true);
            }
            
            userDao.save(user);
            throw new LoginFailedException("Invalid username or password");
        }
        
        user.resetLoginAttempts();
        userDao.save(user);
    } else {
        throw new LoginFailedException("Invalid username or password");
    }
    return user;
}
```