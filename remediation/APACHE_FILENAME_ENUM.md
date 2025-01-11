# Remediation for APACHE_FILENAME_ENUM

## Remediation Steps for Apache Filename Enumeration Test

This security issue occurs when the Apache HTTP servers are incorrectly or insufficiently configured, potentially allowing an attacker to enumerate names of sensitive files and directories.

### Step 1: Hide Apache Version and Server Signature

By default, Apache reveals its version number and other details in the error pages. You can hide this information by editing the configuration file. This is important because it prevents potential attackers from determining any software vulnerabilities simply based on the version number.

```bash
sudo nano /etc/apache2/apache2.conf
```

Find the line starting with `ServerTokens` and `ServerSignature`, and edit as follows:

```bash
ServerTokens Prod
ServerSignature Off
```

### Step 2: Enable `mod_rewrite` and `mod_security`

`mod_rewrite` and `mod_security` are Apache modules that allow for server side redirection and provide a firewall respectively.

```bash
sudo a2enmod rewrite
sudo a2enmod security2
```

### Step 3: Configure .htaccess file

A .htaccess file (Hypertext Access file) is a directory-level configuration file used by Apache-based web servers. It can be used to hide file and directory listings.

```bash
sudo nano /var/www/html/.htaccess
```
Add this line to the .htaccess file:

```apache
Options -Indexes
```
This option will disable directory browsing.

### Step 4: Restart Apache Server

After the configuration changes, the Apache server needs to be restarted for the changes to take effect.

```bash
sudo service apache2 restart
```
