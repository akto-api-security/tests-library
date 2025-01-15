# Remediation for ARANGODB_INTERFACE_EXPOSURE

## Remediation Steps for ArangoDB Web Interface Exposure

ArangoDB Web Interface Exposure presents a substantial security issue. Without properly securing the interface, it can be exploited allowing unauthorized amendments to the database or access to sensitive information.

### Step 1: Limit Access to Web Interface

Configure the ArangoDB to bind to localhost (127.0.0.1) only to prevent connections from other hosts. You can do this by modifying the arangodb.conf file:

```bash
sudo nano /etc/arangodb3/arangod.conf
```

Locate [network] section and change the endpoint to loopback IP:

```bash
[network]
endpoint = tcp://127.0.0.1:8529
```

Save and close the configuration file.

### Step 2: Restart ArangoDB Service

After the configuration changes, ensure to restart ArangoDB service for the changes to take effect:

```bash
sudo systemctl restart arangodb3
```

### Step 3: Firewall Configuration

Make sure to configure your firewall to only allow ingress traffic on the ArangoDB port (default is 8529) from trusted IP addresses:

```bash
sudo ufw allow from trusted_ip to any port 8529
```
Replace `trusted_ip` with the IP address that you want to allow.