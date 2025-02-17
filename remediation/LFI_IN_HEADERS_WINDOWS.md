

## Remediation Steps for LFI in Headers (Windows)

Local File Inclusion (LFI) is a security vulnerability that allows a hacker to include files on your system remotely. This could potentially lead to sensitive information disclosure or unauthorized command execution. Here are the steps for remedying this vulnerability.

### Step 1: Data Validation

Firstly, always validate user input. This is the most effective countermeasure against LFI attacks, as they typically exploit poorly validated input fields.

In PHP:

```php
<?php
$page = basename($_GET['page']);
if(!preg_match('/^[a-z0-9]*$/i', $page)) {
  die("Illegal characters detected");
} else {
  include($page . ".php");
}
?>
```

The snippet above will only allow alphanumeric character inputs.

### Step 2: Limit File System Access

Limit file system access or enforce directory level access control. This ensures that even if an include happens, important resources are not read. This can be done using `.htaccess` files and configuring the correct permissions on directories and files.

### Step 3: Use Built-in Functions

Make use of existing built-in functions to include files rather than user-supplied input for file paths. This will help prevent an LFI attack by not allowing the including of files from user specified paths.

For example, if your application is a multi-page website, you could have a switch function in PHP:

```php
<?php
switch($_GET['page']) {
  case "home":
    include("home.php");
    break;
  case "about":
    include("about.php");
    break;
  default:
    include("404.php");
}
?>
```
