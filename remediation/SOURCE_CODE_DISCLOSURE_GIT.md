

## Remediation Steps for Source Code Disclosure Using Git

Source code disclosure via Git is a common and serious security issue. Without proper Git configuration, attackers may gain unauthorized access to your source code.

### Step 1: Remove Git Configuration Files From Web-Accessible Directories

Firstly, Git configuration files like `.git` directories or `.gitignore` files should not be in directories accessible through the web.

```bash
# Move to the root directory
cd /

# Find .git directories and move them to a non-web-accessible location
find /path/to/web/root -name ".git" -type d | xargs -I '{}' mv {} /path/to/safe/location
```

### Step 2: Configure .htaccess to Deny Access to .git

Set the `.htaccess` file in the web root (or server configuration file in case of Nginx) to deny access to `.git` and `.gitignore`.

If you are using Apache Server, add this to your .htaccess file:

```bash
# Deny access to .git and .gitignore
RewriteRule ^(.*/)?\.git+ - [F,L]
```

In the case of an Nginx server, add this to your server configuration file:

```nginx
# Deny access to .git and .gitignore
location ~ /.git {
    deny all;
}
```

### Step 3: Scan Regularly For Git Configuration Files

Regular scanning of your web root helps keep track and ensure that Git configuration files are not accidentally committed.

```bash
# Recursively search for git config files
find /path/to/web/root -name ".git*" -print
```