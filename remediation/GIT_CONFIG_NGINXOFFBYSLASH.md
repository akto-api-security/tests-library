# Remediation for GIT_CONFIG_NGINXOFFBYSLASH

## Remediation Steps for Nginx - Git Configuration Exposure

If your Nginx server configuration is mistakenly set up in such a way that it allows users to access the `.git` directory of your project, then you may potentially expose sensitive information. This Git configuration exposure can lead to serious security issues.

### Step 1: Locate your Nginx server configuration file

```bash
 sudo find / -name nginx.conf
```

### Step 2: Edit Nginx server configuration file

Open the Nginx server configuration file (typically located at `/etc/nginx/nginx.conf` or `/etc/nginx/sites-available/default` depending on your setup), and add the following code inside the server block. Replace `example.com` with your domain.

```bash
  nano /etc/nginx/sites-available/example.com
```

Add the following code:

```nginx
location ~ /\.git {
    deny all;
}
```

This configuration will prevent access to any `.git` directory within your server.

### Step 3: Test the configuration file

After making these modifications, verify if the configuration file is error-free.

```bash
  sudo nginx -t
```

### Step 4: Restart the Nginx server

If the configuration is successful, restart the server to effect the changes.

```bash
  sudo systemctl restart nginx
```

Remember to carry out regular audits and updates to make sure your server remains secure. Your `.git` directory should now be inaccessible to the public, effectively resolving the Git Configuration Exposure issue.