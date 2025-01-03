# Remediation for PHPFASTCACHE_PHPINFO_EXPOSURE

## Remediation Steps for phpfastcache phpinfo Resource Exposure
Exposure of phpinfo Resource in phpfastcache is a severe security issue. Without properly securing the phpinfo resource, attackers may gain unauthorized access to sensitive information such as PHP Environment, HTTP Headers, etc.

### Step 1: Remove all phpinfo() calls
The `phpinfo()` function is generally used for debugging purposes. Heightened exposure risk occurs when phpinfo is accessible in a production environment. Remove or comment out any `phpinfo()` calls in your PHP code.
```php
// Avoid
phpinfo();

// Better
//phpinfo();
```

### Step 2: Limiting phpinfo() output
If the use of `phpinfo()` is necessary, use it together with a parameter that limits the output. For instance, setting the parameter to `INFO_GENERAL` only outputs general information about the PHP environment.
```php
// Only outputs general information
phpinfo(INFO_GENERAL);
```

### Step 3: Use a safe method to display PHP information
Instead of using `phpinfo()`, which exposes all information, including potentially sensitive data, use `phpversion()`, which only gives PHP version data.
```php
echo 'Current PHP version: ' . phpversion();
```

### Step 4: Implement an IP Allow-List for Debug Endpoints
If there's absolutely a need for having a `phpinfo()` call accessible, restrict the access to a set of trusted IPs. Place the IP-allow-lister before the `phpinfo()` call.
```php
$allowed_ips = ['127.0.0.1', '::1', '192.168.0.1'];
if (in_array($_SERVER['REMOTE_ADDR'], $allowed_ips)) {
    phpinfo();
} else {
    http_response_code(403);
    die('Forbidden');
}
```

### Step 5: Regular Audit and Update
Perform regular audits of your code quality and keep your frameworks and dependencies updated to the latest stable version. Always ensure least privilege principles are maintained across your PHP applications. Update your IDE and static analysis tools to catch insecure coding practices. 

Remember, it's always better to prevent the issues from occurring than trying to fix them later.