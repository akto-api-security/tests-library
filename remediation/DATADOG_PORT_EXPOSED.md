

## Remediation Steps for Datadog Port Exposure
Datadog port exposure can lead to security vulnerabilities. Attackers might be able to sniff network traffic or attack the monitoring system directly. Here is the step by step guide to fix this vulnerability:

### Step 1: Firewall Configuration
Firstly, disallow all incoming traffic on the specific port Datadog is using (by default it's 8126 for the Datadog Agent):
```bash
sudo ufw deny from any to any port 8126
```

### Step 2: Limit access to Datadog agent
Next, limit the access to the Datadog agent by allowing connections only from trusted IP addresses. Replace `trusted_ip_address` with the IP address you trust:
```bash
sudo ufw allow from trusted_ip_address to any port 8126
```

### Step 3: Enable Datadog Agent Authentication 
You can enable basic HTTP authentication on the Datadog agent to further secure the endpoint:
```yml
# /etc/datadog-agent/datadog.yaml
api_key: your_api_key
apm_config:
  enabled: true
  apm_non_local_traffic: true
  receiver_port: 8126
  connection_limit: 1000
  ignore_resources: # add if any
  receiver_socket: /var/run/datadog/apm.socket
  apm_dd_url: https://trace.agent.datadoghq.com
  env: none # default to none
  extra_sample_rate: 1.0
  max_traces_per_second: 10
  max_memory: 1200000000
  max_cpu_percent: 50
  log_file: /var/log/datadog/apm.log
  log_level: INFO
  log_throttling: true
```

### Step 4: Restart the Datadog service
```bash
sudo service datadog-agent restart
```
