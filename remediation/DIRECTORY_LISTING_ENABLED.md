

## Remediation Steps for Directory Listing Enabled

Directory Listing is a web server function that displays the directory contents when no index file is found. If Directory Listing is enabled, it can lead to information disclosure as it allows anyone to see all the files and directories on your website.

### Step 1: Disable Directory Listing in Apache Web Server

You can disable directory listing in the Apache web server by editing the configuration file (usually named `httpd.conf` or `apache2.conf`).

```bash
sudo nano /etc/apache2/apache2.conf
```

You'll need to locate the Directory directive and inside it, set the option `-Indexes`. This tells Apache to turn off directory indexing.

```apacheconf
<Directory /var/www/>
    Options FollowSymLinks -Indexes
    AllowOverride None
    Require all granted
</Directory>
```

After editing, save the file and exit then restart the Apache service.

```bash
sudo service apache2 restart
```

### Step 2: Disable Directory Listing in Nginx Web Server

Disabling directory listing in the Nginx web server is straightforward. Open the configuration file.

```bash
sudo nano /etc/nginx/nginx.conf
```

Locate the `autoindex` directive and make sure it's set to `off`.

```nginxconf
server {
    location / {
        autoindex off;
    }
}
```

Save the file and exit, then test the configuration and reload Nginx service.

```bash
sudo nginx -t
sudo service nginx reload
```