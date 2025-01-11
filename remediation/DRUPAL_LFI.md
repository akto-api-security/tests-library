# Remediation for DRUPAL_LFI

## Remediation Steps for Drupal Local File Inclusion

Local File Inclusion (LFI) is a type of vulnerability that allows an attacker to read and sometimes execute files on the server, which could lead to complete system takeover. Cases of LFI in Drupal applications can often be attributed to poorly sanitized user inputs.

### Step 1: Update to the Latest Version of Drupal

The number one mitigation against LFI attacks in Drupal is simply keeping your installation up to date. Drupal’s security team is quite active and issues are fixed quickly. Hence, updating can help to patch these vulnerabilities.

```bash
drush updatedb
drush pm-update
```

### Step 2: Sanitize User Inputs

Sanitize all user inputs before including them. This can be achieved by using drupal's `check_plain()` function.

```php
$filename = check_plain($filename);
include($filename);
```

### Step 3: Use Drupal's Built-in Functions

Use Drupal's built-in `drupal_get_path_alias()` function which returns path alias given Drupal system path. 

```php
$path = drupal_get_path_alias('user/register');
```

### Step 4: Avoid using PHP’s file inclusion functions

Avoid using PHP’s file inclusion functions like `include`, `include_once`, `require` and `require_once` and use Drupal's built-in functions when possible.

### Step 5: Use Correct File Permissions

Ensure correct file permissions on the server. In general, directories should be 755 and files should be 644 except `settings.php` which should be 444.