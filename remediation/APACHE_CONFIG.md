# Remediation for APACHE_CONFIG

## Remediation Steps for Apache Config File Disclosure 

Apache Config file disclosure is a critical security issue. Without proper access restrictions, attackers may gain unauthorized access to sensitive configuration information that can be exploited to undermine the system.

### Step 1: Update permissions for apache config files

Permissions of configuration files should be restricted such that only authorized users can access these. In Linux environments, this can be done using the following commands:

```bash
sudo chown root:root /etc/apache2/apache2.conf
sudo chmod 640 /etc/apache2/apache2.conf
```

### Step 2: Disable Directory Indexing 

Directory indexing should be disabled to prevent users from browsing files on your server.

The following code needs to be added or checked in the apache config file to ensure directory indexing is disabled:

```bash
<Directory /var/www/>
  Options -Indexes
  Order allow,deny
  Allow from all
</Directory>
```

### Step 3: Implement .htaccess Files 

.htaccess files can be used to override specific configurations on a per-directory basis. To prevent certain files from being accessed, create an .htaccess file in the relevant directory:

```bash
sudo nano /var/www/html/.htaccess
```

Add a rule to prevent access to the specific file. For example, to block access to `config.php`, put the following content in your `.htaccess` file:

```
<Files "config.php">
  Order Allow,Deny
  Deny from all
</Files>  
```