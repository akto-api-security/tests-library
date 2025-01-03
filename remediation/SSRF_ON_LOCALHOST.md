# Remediation for SSRF_ON_LOCALHOST

## Remediation Steps for Exposed Localhost Details due to SSRF (Server Side Request Forgery)

Exposing sensitive localhost details via replacing URI parameter with localhost/admin due to SSRF is a serious security issue. Attackers might exploit this vulnerability to gain unauthorized access to internal resources and sensitive information of an application. 

### Step 1: Validate and whitelist server-side URLs

You can add a whitelist of URLs that the application server is permitted to redirect to. Here is an example implementation in Python.

```python
URL_WHITELIST = ['https://trusted.com']

def is_url_valid(url):
    return url in URL_WHITELIST
```
### Step 2: Create an outbound proxy

Firewall allows you to create rules to block requests. You could redirect the outbound traffic to a proxy, which makes the SSRF exploitation significantly harder.

```bash
iptables -t nat -A OUTPUT -p tcp --dport 80 -j DNAT --to-destination ip_of_proxy:5000
iptables -t nat -A OUTPUT -p tcp --dport 443 -j DNAT --to-destination ip_of_proxy:5000
```

### Step 3: Use a Web Application Firewall (WAF)

A Web Application Firewall (WAF) acts as a shield between your server and the internet. It helps to identify and block common web-based threats, helping protect your server from attackers.

```bash
sudo apt-get install mod-security-crs
```

### Step 4: Regularly update and audit your systems

Maintaining the security of your systems includes regular auditing and updating to ensure all security measures are up-to-date.

```bash
sudo service apache2 restart
```