# Remediation for NGINX_SERVER_VERSION_DISCLOSED

## Remediation Steps for Nginx Server Version Disclosure

Nginx Server Version Disclosure can be dangerous as it exposes the server's detailed version information which can potentially be used maliciously by hackers.

### Step 1: Locate Nginx Configuration File

The default location for the Nginx main configuration file is `/etc/nginx/nginx.conf`. If it is located elsewhere, replace the given path in the following source code to the correct path.

```bash
sudo nano /etc/nginx/nginx.conf
```

### Step 2: Remove Version Details

In the `http` or `server` block, add or alter the `server_tokens` directive to `off`. This directive controls the display of the Nginx version on error pages and in the "Server" response header field.

```bash
server_tokens off;
```

Here is a sample configuration of the main `http` block:

```bash
http {
  server_tokens off;
  ...
}
```

### Step 3: Save and Exit

Press `Ctrl+X`, then press `Y` and then `Enter` to save the file and exit nano.

### Step 4: Test Nginx Configuration

Before restarting your Nginx server, it's recommended to test your configuration file for any syntax errors. Use the following command to validate your settings:

```bash
sudo nginx -t
```

### Step 5: Restart Nginx

The final step is to load the new configuration into Nginx by restarting it with the following command:

```bash
sudo systemctl restart nginx
```

After these steps, your Nginx server should no longer expose version information. 

Please ensure to regularly update your server software to stay protected from any newly identified vulnerabilities.