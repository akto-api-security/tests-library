

## Remediation Steps for Bypass Authentication via URL Modification to HTTP only

Bypassing authentication by manipulating an authenticated URL to a non-secure HTTP connection can expose sensitive information and is a significant security vulnerability. Below are steps to remedy this issue.

### Step 1: Enforce HTTPS Everywhere

The most effective way to protect against this vulnerability is to enforce HTTPS (HTTP over SSL/TLS) everywhere on your site. Implement a server-side redirect from HTTP to HTTPS to ensure that all traffic is secure. 

If you are using Apache server, you can do this with an .htaccess file:

```apache
RewriteEngine On 
RewriteCond %{HTTPS} off 
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

If you are using Nginx server, you can modify your config file as follows:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$host$request_uri;
}
```

### Step 2: Secure Cookies 

Ensure all cookies are secure and served only over HTTPS.

```javascript
res.cookie(name, 'value', { secure: true })
```

### Step 3: Implement HTTP Strict Transport Security (HSTS) 

HSTS is a web security policy that helps to protect websites against protocol downgrade attacks and cookie hijacking on client side. 

In Apache:

```apache
<IfModule mod_headers.c>
    Header always set Strict-Transport-Security "max-age=63072000; includeSubDomains"
</IfModule>
```

In Nginx:

```nginx
add_header Strict-Transport-Security 'max-age=31536000; includeSubDomains';
```