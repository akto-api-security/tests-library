

## Remediation Steps for Sensitive Data Exposure in Grafana

Sensitive data exposure in Grafana is a critical security issue. When an attacker gains access to sensitive data, it can threaten the integrity and confidentiality of your data.

### Step 1: Set up HTTPS for Grafana
Using HTTPS is recommended for Grafana. Here is how to do it:

```bash
# Navigate to the Grafana configuration directory
cd /etc/grafana

# Backup your current Grafana configuration
sudo cp grafana.ini grafana.ini.bak

# Open the configuration file
sudo nano grafana.ini
```

Inside the configuration file, uncomment (remove the ;) the following lines in the `server` section:

```bash
protocol = https
http_port = 443
domain = mygrafanadomain.com
root_url = https://mygrafanadomain.com
```

And under the `security` section, you may set `cookie_secure` as true.

### Step 2: Generate SSL Certificates

Generate the self-signed SSL certificates. You can generate these certificates from Let’s Encrypt or any other service you prefer.

```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./ssl.key -out ./ssl.crt -subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=mygrafanadomain.com"
```

Once the SSL certificates are generated, specify the directory of SSL certificates in your Grafana configuration:

```bash
# Open the configuration file
sudo nano grafana.ini
```

And add the following lines in the `server` section:
```bash
cert_file = /etc/grafana/ssl.crt
cert_key = /etc/grafana/ssl.key
```

### Step 3: Restart Grafana Service

Finally, restart the Grafana service to apply the changes:

```bash
sudo systemctl restart grafana-server
``` 