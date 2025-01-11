# Remediation for APACHE_SERVER_VERSION_DISCLOSED

## Remediation Steps for Apache Server Version Disclosure
Disclosing the Apache server version can be a serious security issue. This information might potentially be used by attackers to adapt their attack strategy to the specific version, increasing the chance of successful exploitation.

### Step 1: Edit the Apache Configuration File
The first step to remediate this issue is to stop Apache from revealing its version number in error pages. You can accomplish this by editing the Apache configuration file (`httpd.conf` or `apache2.conf`), usually located in the `/etc/apache2/` or `/etc/httpd/` directories.

```bash
sudo nano /etc/apache2/apache2.conf
```

Or, depending upon your system's configuration:

```bash
sudo nano /etc/httpd/conf/httpd.conf
```

### Step 2: Update ServerTokens Directive
In the configuration file, find the `ServerTokens` directive and set its value to `Prod`.

Before:

```apache
ServerTokens Full
```

After:

```apache
ServerTokens Prod
```

If `ServerTokens` is not present, add the directive at the end of the file. This directive controls whether server response headers include the Apache version and other information.

### Step 3: Update ServerSignature Directive
Next, find the `ServerSignature` directive and set it to `Off`. This directive controls whether server version and other information are added to server-generated pages.

Before:

```apache
ServerSignature On
```

After:

```apache
ServerSignature Off
```

If `ServerSignature` is not present, add the directive at the end of the file.

### Step 4: Save Changes and Restart Apache
Save the changes and close the editor. To apply the changes, restart the Apache server:

```bash
sudo service apache2 restart
```

Or:

```bash
sudo systemctl restart httpd
```