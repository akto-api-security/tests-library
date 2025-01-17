

## Remediation Steps for Kibana API Exposure
Kibana API exposure can lead to serious security issues. If not properly secured, attackers might gain unauthorized access to your Elasticsearch data. To avoid this, follow the steps below.

### Step 1: Secure Kibana with a password
1. Open Kibana configuration file
```bash
sudo nano /etc/kibana/kibana.yml
```
2. Add `elasticsearch.username` and `elasticsearch.password` in the kibana configuration
```yaml
elasticsearch.username: "my_kibana"
elasticsearch.password: "my_password"
```

### Step 2: Enable TLS/SSL
1. Enable encryption by setting `server.ssl.enabled` to true
2. Set the locations of the key and certificate
```yaml
server.ssl.enabled: true
server.ssl.certificate: /path/to/your/server.crt
server.ssl.key: /path/to/your/server.key
```

### Step 3: Enable X-Pack security
1. Set `xpack.security.enabled` to true
```yaml
xpack.security.enabled: true
```

### Step 4: Restart Kibana
In order for settings to take effect, Kibana must be restarted
```bash
sudo service kibana restart
```

> Note: Kibana requires a restart for any changes made in the kibana.yml to take effect.