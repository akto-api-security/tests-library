# Remediation for SSTI_IN_TWIG

## Remediation Steps for Server Side Template Injection (SSTI) in Twig

SSTI in Twig is a serious security issue where an attacker can gain unauthorized control over the template, potentially leading to Remote Code Execution (RCE). Such vulnerability can be effectively mitigated by validating and sanitizing input and restricting access to potentially dangerous Twig features. 

### Step 1: Use Auto-escaping
Turn on auto-escaping to help prevent XSS and other types of injection attacks. This can be done on a global or individual template level.

```twig
{% autoescape 'html' %}
    {{ user_input }}
{% endautoescape %}
```

### Step 2: Filter and Validate User Input
Filter out anything non-alphanumeric to prevent malicious input. Ensure all user input is validated and sanitized before use.

```php
$user_input = filter_input(INPUT_GET, 'user_input', FILTER_SANITIZE_STRING);
$user_input = preg_replace("/[^A-Za-z0-9 ]/", '', $user_input);
```

### Step 3: Restrict Twig Filesystem Access
You should restrict access to the filesystem to prevent template injection attacks. This can be done by setting the `FilesystemLoader` to only load templates from a defined directory.

```php
$loader = new \Twig\Loader\FilesystemLoader('/path/to/templates');
$twig = new \Twig\Environment($loader);
```

### Step 4: Disable Unsafe Twig Features
Disabling unsafe filters and functions like 'include', 'sandbox' can help to prevent SSTI vulnerability.

```php
$policy = new Twig\Sandbox\SecurityPolicy(
    [],    // If tags are defined here, only these tags are allowed in the templates.
    [],    // If filters are defined here, only these filters are allowed in the templates.
    [],    // If methods are defined here, only these methods are allowed in the templates.
    [],    // If properties are defined here, only these properties are allowed in the templates.
    false  // If set to true, the use of the PHP function() construct is allowed in templates.
);
$twig->addExtension(new Twig\Extension\SandboxExtension($policy, true));
```

Finally, always ensure that your Twig version is up-to-date as many security vulnerabilities will be fixed in the most recent version. 

>
>Note: Allowing the Twig's `auto_reload` option will result in performance hits. If performance is an issue, you might want to disable it in production after you made sure your templates are not too dynamic. The option is true by default when environment is set to 'development'.