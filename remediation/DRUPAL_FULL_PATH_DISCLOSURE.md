# Remediation for DRUPAL_FULL_PATH_DISCLOSURE

## Remediation Steps for Drupal Full Path Disclosure

Full Path Disclosure (FPD) vulnerabilities enable the attacker to see the path to the webroot/file. e.g.: /home/omg/htdocs/file/. Full path disclosure can lead to information disclosure about the server, such as server paths, included files, and other sensitive information.

### Step 1: Ensure that error reporting is turned off
In PHP this can be done by setting the `display_errors` directive to 'Off' in your php.ini file, like this:

```bash
display_errors = Off
```
Make sure to restart your web server to apply the configuration change. 

### Step 2: Turn off Drupal error reporting

In Drupal, you can suppress error messages from being displayed by going to Administration » Configuration » Development » Logging and Errors. Set the Error messages to display setting to "None".

```php
$config['system.logging']['error_level'] = 'hide';
```

### Step 3: Use .htaccess to suppress PHP errors

If changing settings in PHP and Drupal do not suppress PHP error displays, another way to stop PHP errors from being displayed is by adding a line to your `.htaccess` file.

```bash
php_flag display_errors off
```
This also needs to be followed by a server restart.

### Step 4: Regular Drupal audit and update

Ensure Drupal core and modules are regularly updated. This can reduce the risk of any vulnerabilities.

```bash
drush pm-update
```
This command is used by Drush, a command line shell and Unix scripting interface for Drupal. It updates the Drupal installation.

> Note: Always remember to back up your website before making such changes. If anything goes wrong, you then have the option to return to a working version.