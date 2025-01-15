# Remediation for SESSION_FIXATION

## Remediation Steps for Session Fixation
Session fixation is a security issue where a malicious client can manipulate a session ID in a manner that allows subsequent requests to be identified as part of that particular session ID. This allows an attacker to eavesdrop on a user session and capture private data.

### Step 1: Invalidate the Pre-Existing Session ID
Make sure all pre-existing session IDs are invalidated before creating a new session for a user. This is particularly necessary upon successful user login.
For example, in PHP this could look like:
```PHP
<?php
// Initialize session
session_start();

// Unset all session values
$_SESSION = array();

// Destroy the session
session_destroy();

// Start a new session
session_start();
?>
```

### Step 2: Issue New Session ID Upon Login and Privilege Level Change
Whenever a user logs in or when their privilege level changes, issue a new session ID. To change the session ID in PHP, for example, you can use:
```PHP
<?php
session_regenerate_id();
?>
```

### Step 3: Add Session Timeouts
Sessions should have timeouts, such as a sliding session timeout, absolute timeouts or an idleness timeout. This reduces the chance that session fixation attacks will be successful.
```PHP
<?php
// Check if the user's session is still active
if (isset($_SESSION['LAST_ACTIVITY']) && (time() - $_SESSION['LAST_ACTIVITY'] > 1800)) {
    // Last request was more than 30 minutes ago
    session_unset();    // Unset all session values
    session_destroy();  // Destroy the session
}
$_SESSION['LAST_ACTIVITY'] = time(); // Update last activity timestamp
?>
```

### Step 4: Use Secure and HTTP Only Cookies
Make sure to flag cookies as secure and set the HTTP-only flag. This will make it much harder for an attacker to intercept and manipulate the session ID.
```PHP
<?php
session_start();
secure_session();
function secure_session() {
    // Secure the session
    session_set_cookie_params(0, '/', '', isset($_SERVER["HTTPS"]), true);
}
?>
```