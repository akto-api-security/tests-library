

## Remediation Steps for Apache Server Status Exposure via localhost

Apache Server Status exposure via localhost is a serious security issue. When server status is exposed, attackers can gather sensitive information about the server and possibly even take control of the server.

### Step 1: Open Apache Configuration

Open your Apache configuration file (httpd.conf or apache2.conf). The location of this file can vary based on your system. If you are using CentOS, for example, the file will located at `/etc/httpd/conf/httpd.conf`. If you are using Ubuntu, it will be located at `/etc/apache2/apache2.conf`.

```bash
sudo nano /etc/httpd/conf/httpd.conf
```

### Step 2: Locate "mod_status" Section

Scroll through the file until you locate the mod_status section of the configuration file. This will start with:

```bash
<Location /server-status>
```

### Step 3: Restrict Access 

Update your configuration file to restrict access to localhost or a specified IP address only. Replace `Require host localhost` line with `Require ip YOUR_IP_ADDRESS`.

```bash
<Location /server-status>
    SetHandler server-status
    Require host localhost
    Require ip YOUR_IP_ADDRESS
</Location>
```

### Step 4: Restart the Apache service

Now that you've updated your Apache configuration, save and close the file, then restart your Apache server so the changes can take effect.

```bash
sudo service httpd restart
```

Following these steps should limit the exposure of your Apache server-status pages to only those located on the localhost or the IP address that you've specified, effectively limiting the risk of this information being accessed by unauthorized users. 

Remember to always validate the changes you've implemented by checking the accessibility of /server-status from different locations! Each time you make changes to your security settings, ensure that they are working as expected.