# Remediation for NGINX_STATUS_VISIBLE

## Remediation Steps for NGINX Status Disclosure

NGINX status disclosure is a security issue where critical information about the server is revealed. This can potentially provide useful information to attackers planning to exploit the server. Therefore, it's important to ensure that the NGINX status module is properly secured or obscured.

### Step 1: Open NGINX Configuration File

```bash
sudo nano /etc/nginx/nginx.conf
```

### Step 2: Locate and Comment the Status Module

In the configuration file, locate the line(s) that enable the status module. This is typically in a "location" block. It might look something like this:

```bash
location /nginx_status {
  stub_status on;
  allow 127.0.0.1;
  deny all;
}
```

Comment out this entire block of code by adding a `#` character at the start of each line, like so:

```bash
# location /nginx_status {
#  stub_status on;
#  allow 127.0.0.1;
#  deny all;
# }
```

By doing this, the status module will be disabled.

### Step 3: Save and Close the Configuration File

Press `Ctrl + X` to save changes and then `Y` followed by `Enter` to confirm saving. The configuration file is now updated.

### Step 4: Test Configuration and Restart NGINX

Before we restart NGINX, it's recommended to test the configuration. Type in the following command.

```bash
sudo nginx -t
```

If the test is successful, restart NGINX.

```bash
sudo service nginx restart
```