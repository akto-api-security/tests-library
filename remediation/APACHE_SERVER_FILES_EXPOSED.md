# Remediation for APACHE_SERVER_FILES_EXPOSED

## Remediation Steps for Apache Server Files Exposure
Apache Server Files exposure can significantly impact the security of your server. Unauthorized individuals may gain access to sensitive files, which could lead to a potential data breach. Therefore, it is crucial to properly secure your Apache Server Files.

### Step 1: Update Apache to the Latest Version
```bash
sudo apt-get update
sudo apt-get install apache2
```
### Step 2: Disable Directory Indexing
To disable directory indexing, you need to update your Apache configuration.
Open the configuration file for editing. This can be `/etc/apache2/apache2.conf` or a specific site configuration in `/etc/apache2/sites-available/`.

```bash
nano /etc/apache2/apache2.conf
```
Look for a section that looks like the following and comment out the `Options Indexes FollowSymLinks` line.
```bash
<Directory /var/www/>
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>
```
Change it to:

```bash
<Directory /var/www/>
    #Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>
```
Save and exit the editor. Then restart Apache to apply the changes.
```bash
service apache2 restart
```
### Step 3: Ensure Correct File Permissions
All files should be owned by the root user and the Apache group:

```bash
chown -R root:www-data /var/www
```

Then, set correct permissions:

```bash
find /var/www -type d -exec chmod 755 {} \;
find /var/www -type f -exec chmod 644 {} \;
```

### Step 4: Regularly Monitor Apache Access and Error Logs
```bash
tail -f /var/log/apache2/access.log
tail -f /var/log/apache2/error.log
```

This monitors the logs in real-time and helps identify any potential unauthorized access attempts.