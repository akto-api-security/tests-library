# Remediation for NGINX_CONFIG

## Remediation Steps for Nginx Config File Disclosure
Nginx Config file disclosure can lead to serious security issues as unauthorized users might get sensitive information. Following the steps below will help in preventing this vulnerability.

### Step 1: Setting Up Correct File Permissions
By limiting user permissions, we can protect sensitive data from being disclosed. For the nginx config file, you should only give read/write access to the necessary users such as the root user and the nginx user.

```bash
chown root:nginx /etc/nginx/nginx.conf
chmod 640 /etc/nginx/nginx.conf
```
In the above code, `chown root:nginx /etc/nginx/nginx.conf` changes the owner of the file to root and group to nginx. And `chmod 640 /etc/nginx/nginx.conf` sets the permission so that the owner can read and write the file, the group can read, and others get no permissions.

### Step 2: Disallow Config File in Nginx Configuration
Another approach is to explicitly disallow access to the nginx configuration file in the nginx server block itself. 

```nginx
location ~ /etc/nginx/ {
   deny all;
}
```
In the above code, `location ~ /etc/nginx/` selects requests with uri starting with /etc/nginx. And `deny all;` will not allow any type of access to it.

### Step 3: Regular Audit
Regularly verifying your server and file permissions is a good habit. 

```bash
ls -l /etc/nginx/nginx.conf
```
This command should only return the permission of the Nginx config file.

### Step 4: Update Nginx Regularly
Ensure your server is regularly updated as improvements and patches are released frequently.

```bash
sudo apt update
sudo apt upgrade nginx
```

The `sudo apt update` command updates the package lists for upgrades. `sudo apt upgrade nginx` installs the newest versions of all installed Nginx.