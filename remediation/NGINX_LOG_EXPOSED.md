# Remediation for NGINX_LOG_EXPOSED

## Remediation Steps for Nginx Log Exposure
Nginx log exposure is a serious security issue. If your logs are exposed, they can provide attackers with valuable information about your system and its vulnerabilities. 

Here is how you can mitigate this vulnerability:

### Step 1: Restrict Access to Log Files
Firstly, you need to restrict access to the log files. Only the necessary users should have the permissions to view these logs.

```bash
sudo chmod -R 640 /var/log/nginx/
sudo chown -R nginx:nginx /var/log/nginx/
```
### Step 2: Enable Access Logs
You might want to enable access logs in Nginx web server to monitor your website’s traffic in detail. This information is extremely helpful in troubleshooting, performance evaluation and system resource planning.

```bash
sudo nano /etc/nginx/nginx.conf
```

In the opened configuration file, add or uncomment the line:

```bash
access_log /var/log/nginx/access.log;
```

Save the changes and exit the text editor. To effect the changes, you'll need to restart Nginx:

```bash
sudo systemctl restart nginx
```

### Step 3: Configure Log Rotation
The logs should be rotated regularly to avoid filling up the disk space. This can be achieved using the logrotate utility.

Create a new configuration file for Nginx log rotation:

```bash
sudo nano /etc/logrotate.d/nginx
```

Add the following content to the file and save it:

```bash
/var/log/nginx/*log {
     daily
     missingok
     rotate 52
     compress
     delaycompress
     notifempty
     create 640 nginx adm
     sharedscripts
     postrotate
           /bin/kill -USR1 `cat /run/nginx.pid 2>/dev/null` 2>/dev/null || true
     endscript
}
```

Ensure logrotate is correctly set up by checking its status:

```bash
sudo logrotate --debug /etc/logrotate.d/nginx
```

### Step 4: Regular Audit and Update
Routinely check your logs to monitor for unusual activities and keep your Nginx server updated to the latest version to obtain new security patches.

```bash
sudo apt-get update
sudo apt-get upgrade nginx
```