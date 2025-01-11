# Remediation for NGINX_DEFAULT_PAGE_ENABLED

## Remediation Steps for Nginx Default Page Enabled

Having the default Nginx page enabled is a security issue because it informs potential attackers that your server is running Nginx and that you have not changed the default settings, making it easier for them to exploit any vulnerabilities.

### Step 1: Backup The Default Configuration
Before making changes, backup the current configuration.
```bash
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak
```

### Step 2: Modify Nginx Default Configuration File
Open the default Nginx configuration file.
```bash
sudo nano /etc/nginx/sites-available/default
```

Replace the contents of the file with the following to set your own landing page. Replace `/var/www/html` with the path to your own default web page.
```bash
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

### Step 3: Test The New Configuration
```bash
sudo nginx -t
```

If there aren't any errors, restart Nginx to apply the changes.
```bash
sudo systemctl restart nginx
```

### Step 4: Verify That The Default Nginx Page No Longer Displays

You can verify by visiting your site's URL in a web browser.