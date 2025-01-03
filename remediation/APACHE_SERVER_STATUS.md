# Remediation for APACHE_SERVER_STATUS

## Remediation Steps for Apache Server Status Exposure

Apache Server Status exposure is a high-priority issue. If left exposed, it could provide a treasure trove of information for potential attackers, such as IP addresses, request URI, etc. 

### Step 1: Edit the Apache Configuration File

Open the Apache Configuration file, `httpd.conf` or `apache2.conf` based on your system, in a text editor with root privileges.

```bash
sudo nano /etc/apache2/apache2.conf
```
For certain Apache installations, you may have to look under:
```bash
sudo nano /etc/httpd/conf/httpd.conf
```
### Step 2: Locate and Modify the Server Status Directive 

Find the `<Location /server-status>` in the configuration file and modify as follows:

```plaintext
<Location /server-status>
    SetHandler server-status
    Order Deny,Allow
    Deny from all
    # Allow from localhost
</Location>
```
If you want to limit access to a certain IP address replace `Allow from localhost` with `Allow from <your-ip-address>`.

### Step 3: Restart Apache 

Restart the Apache service to implement the changes. 

```bash
sudo service apache2 restart
```
Or 
```bash
sudo systemctl restart apache2
```
### Step 4: Regular audit and patching 

Keep the Apache server regularly audited and updated to prevent potential exploits. 

```bash
sudo apt-get update
sudo apt-get upgrade
```

This suggests denying all access to the server status page by default and be sure to replace `<your-ip-address>` with the actual IP from where you will be viewing these stats.