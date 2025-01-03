# Remediation for GRAFANA_LOGIN_PANEL_EXPOSURE

## Remediation Steps for Grafana Login Panel Exposure

Grafana Login Panel Exposure can be a significant security issue. An unprotected Login Panel can be exploited to gain unauthorized access to your Grafana dashboards, potentially interfering with your system monitoring and data visualization.

Below are remediation steps to secure your Grafana login panel:

### Step 1: Change default credentials
The first line of defense against any unauthorized access is a strong password policy. If currently not set, ensure to update Grafana's default username and password. You can use the following command to alter credentials on Grafana's CLI:

```bash
grafana-cli admin reset-admin-password <new_password_here>
```

### Step 2: Use SSL for Grafana login

In order to secure the login data being transferred, it's important to enforce the useof SSL for your Grafana login panel by enabling it in your Grafana configuration file.

Here is the setting to turn on SSL in the Grafana config file (`/etc/grafana/grafana.ini`):

```ini
[server]
protocol = https
cert_file = /path/to/cert.pem
cert_key = /path/to/key.pem
```

### Step 3: Use a Reverse Proxy

Hosting Grafana behind a reverse proxy with a firewall can add an additional layer of security to your login panel. Assuming the use of Nginx as the reverse proxy, see the configuration below:

```nginx
server {
  listen 80;
  server_name grafana.domain.com;
  return 301 https://$host$request_uri;
}

server {
  listen 443 ssl;
  server_name grafana.domain.com;

  ssl_certificate /etc/nginx/ssl/nginx.crt;
  ssl_certificate_key /etc/nginx/ssl/nginx.key;

  location / {
      proxy_pass http://localhost:3000;
  }
}
```

### Step 4: Regular Audit and Update

Always update your Grafana to the latest version to ensure that the most recent security updates are in place. Maintaining this routine practice can strengthen your system:

```bash
sudo apt-get update
sudo apt-get upgrade grafana
```

### Step 5: Hide your login form

If you do not want the login form to appear publicly, you can use the below configuration under the `[auth.anonymous]` section in `grafana.ini`

```ini
[auth.anonymous]
# enable anonymous access
enabled = true
# specify organization name that should be used for unauthenticated users
org_name = Main Org.
# specify role for unauthenticated users
org_role = Viewer
# hide user profile switcher in the side menu
hide_sign_out_menu = true
```
Always remember to restart the Grafana server after performing these changes:

```bash
sudo service grafana-server restart
```