# Remediation for NGINX_PLUS_REST_API_EXPOSURE

## Remediation Steps for NGINX Plus REST API Exposure

NGINX Plus REST API exposure is a severe security issue that may lead to unauthorized access to server resources. To remediate the issue, the access to the API must be restricted by implementing proper access control measures.

### Step 1: Disable the NGINX Plus API

The first remediation step is to disable the NGINX Plus API if it is not being used. This can be done by commenting out or removing the API directive in your configuration file.

```bash
# Inside your nginx.conf file, comment out or remove the api directive

# location /api {
#   api write=on;
# }
```

### Step 2: Restrict Access to the API

If the NGINX Plus API must remain enabled for certain operation needs, restrict its access by using the `allow` and `deny` directives. You can whitelist IP addresses that require access and deny all others.

```bash
# Inside your nginx.conf file

location /api {
    api write=on;

    # Replace '192.0.2.0/24' with the IP address or CIDR range that you wish to allow.
    allow 192.0.2.0/24;

    # Deny all others
    deny all;
}
```

### Step 3: Enable HTTPS

Ensure that communication between the client and the server is secure by enabling HTTPS. Obtain an SSL certificate and add it to your NGINX configuration file.

```bash
# Inside your nginx.conf file

server {
    listen 443 ssl;
    server_name your-domain-name.com;

    ssl_certificate /etc/nginx/ssl/nginx.crt;
    ssl_certificate_key /etc/nginx/ssl/nginx.key;
    ...
}
```

### Step 4: Review and Reload Configuration

After making all the changes, it's crucial to check the configuration syntax and reload NGINX Plus to apply changes.

```bash
# Check configuration syntax
sudo nginx -t

# If syntax is ok, reload Nginx
sudo service nginx reload
```

Deploy these steps and regularly review access logs to ensure that unauthorized access attempts are blocked. Regular updates and patches are a must to prevent any vulnerability exploitation.