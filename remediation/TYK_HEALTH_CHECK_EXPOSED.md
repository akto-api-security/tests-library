# Remediation for TYK_HEALTH_CHECK_EXPOSED

## Remediation Steps for Tyk Health Check Exposure
Tyk Health Check exposure is a serious security concern. If not adequately protected, attackers may fetch sensitive information about the system, which can be exploited further for more sophisticated attacks.

### Step 1: Limit Access to Tyk Health Check
The first remedial step is to limit access to Tyk's health check endpoint. It should not be publicly exposed and should only be accessible by system administrators or necessary applications.

If you are using a platform such as NGINX, you can enforce access rules in the server files. Here's a sample code block:

```bash
location /tyk/health {
      allow 192.168.1.0/24; #Allow a specific IP or network
      deny all; #Deny all other IP addresses
}
```

### Step 2: Implement Authentication
Add an authentication layer to the health check endpoint. You can achieve this by using Tyk's built-in security features or by implementing it at a network level (like using VPN, IP Whitelisting, etc.).

To implement with basic HTTP authentication on NGINX, you can use the following code:

```bash
location /tyk/health {
     auth_basic "Administrator’s Area";
     auth_basic_user_file /etc/nginx/.htpasswd;
}
```

### Step 3: Enable SSL/TLS
Secure the connection between Tyk and users by enabling SSL/TLS. If you are using NGINX as a proxy server, you can configure it as following:

```bash
server {
    listen 443 ssl;
    ssl_certificate /etc/nginx/ssl/nginx.crt;
    ssl_certificate_key /etc/nginx/ssl/nginx.key;
    location /tyk/health {
        proxy_pass http://backend;
    }
}
```

Replace `/etc/nginx/ssl/nginx.crt` and `/etc/nginx/ssl/nginx.key` with paths to your certificate and key files respectively, and replace `http://backend` with the address to your Tyk instance.