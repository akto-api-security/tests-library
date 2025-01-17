

## Remediation Steps for Grafana Exposure

Grafana Exposure is a serious security issue. When Grafana is exposed, an attacker could access sensitive information in your dashboards. Follow the steps below to secure the Grafana environment.

### Step 1: Downgrade Grafana server
In case you are running a Grafana server with a known vulnerability, the best course of action would be to downgrade to a safer version. Here's how to do it:
```bash
sudo apt-get remove grafana
sudo apt-get install grafana=7.3.7
```
Replace `7.3.7` with the version you want to install.

### Step 2: Enable authentication
Grafana, by default, allows anonymous access. It is imperative to disable this and enable authentication.
Open the Grafana default configuration file, located at:
```bash
sudo nano /etc/grafana/grafana.ini
```
Find the `[auth.anonymous]` section, and set `enabled` to false.
```ini
[auth.anonymous]
enabled = false
```
Save the file and close it.

### Step 3: Firewall Configuration
Add a firewall rule to only allow trusted IP ranges to reach the Grafana port.
```bash
sudo ufw deny from any to any port 3000
sudo ufw allow from 192.168.0.0/16 to any port 3000
```
Replace `192.168.0.0/16` with your trusted IP range.

### Step 4: Restart Grafana service
After making the changes, ensure to restart the Grafana service for the changes to take effect.
```bash
sudo service grafana-server restart
```