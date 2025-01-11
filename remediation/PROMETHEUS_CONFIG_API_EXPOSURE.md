# Remediation for PROMETHEUS_CONFIG_API_EXPOSURE

## Remediation Steps for Prometheus Config API Endpoint Exposure

Prometheus Config API endpoint exposure is a crucial security issue. If the Prometheus Config API endpoint is exposed, it may permit unauthorized access to system metrics and potential data leaks.

### Step 1: Disable Configuration API

Firstly, we have to ensure that the Prometheus configuration API (--web.enable-admin-api) is not enabled unless absolutely necessary. If it is not required, disable it to minimize the exposure.

```bash
./prometheus --web.enable-admin-api=false
```

### Step 2: Firewall Configuration

Next, we need to configure firewall settings to efficiently block unwanted outbound/inbound traffic to the Prometheus' default port, which is 9090.

```bash
sudo ufw deny out from any to any port 9090
sudo ufw deny in from any to any port 9090
```

### Step 3: Access Control

Use reverse proxy (Nginx, Apache) and apply Basic Auth or any other authentication process to have an extra layer of security.

Here is a basic example with Nginx:

```bash
server { 
    listen     80; 

    location / { 
        auth_basic "Private Property"; 
        auth_basic_user_file /etc/nginx/.htpasswd; 
        proxy_pass http://localhost:9090; 
    } 
}
```