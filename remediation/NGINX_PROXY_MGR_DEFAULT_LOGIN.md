# Remediation for NGINX_PROXY_MGR_DEFAULT_LOGIN

## Remediation Steps for Nginx Proxy Manager Default Login
The default administrator account for the Nginx Proxy Manager is a security vulnerability, as it can potentially grant an attacker unauthorized access if not properly secured.

### Step 1: Change the Default Login Credentials
Initially, the Nginx Proxy Manager uses default login credentials, typically 'admin@example.com' for the username and 'changeme' for the password. On first login, you are forced to change the email address and password. 
```bash
# Open Nginx Proxy Manager UI in a web browser. 
# URL being something like - http://ip_address:81
# Log in with the default credentials and you'll be forced to update them.
```

### Step 2: Enforce Strong Password Policies
While changing the default password, ensure that you adapt a complex password that complies with password best practices. This includes, at least, a mix of upper and lower case letters, numbers, and special characters.

```bash
# No code is needed as this a manual action.
# Just follow the strong password guidelines while setting the password.
```

### Step 3: Regularly Update Your Password
Finally, it's also a good practice to regularly update your password or use a password manager.
```bash
# No code is needed as this a manual action.
# Regularly check back into the Nginx Proxy Manager UI to update password.
```

### Step 4: Restrict Access to the Admin Interface
Restrict the access to the Nginx Proxy Manager admin interface to trusted networks only.
```bash
# For example, if using UFW as a firewall
# Deny access from all
sudo ufw default deny incoming
# Allow access from trusted IP
sudo ufw allow from trusted_IP to any port 81
```
Remember to replace 'trusted_IP' with the actual trusted IP address. You may also use netmasks (/24, /16, etc.) to allow larger IP ranges.

### Step 5: Regular Audit and Update
Just like any other system, keep your Nginx Proxy Manager updated to the latest version.
```bash
# Pull the latest version of Nginx Proxy Manager
docker pull jc21/nginx-proxy-manager:latest
# Restart your Nginx Proxy Manager container
docker restart nginxProxyManager
```