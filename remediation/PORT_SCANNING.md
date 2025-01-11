# Remediation for PORT_SCANNING

## Remediation Steps for Server Side Request Forgery (SSRF) in Port Scanning
SSRF in port scanning is a serious security issue where the attacker can abuse functionality on the server to read or update internal resources.

### Step 1: Restrict Outgoing Traffic
Firewall rules restricting outgoing traffic from your server can be a good way to limit the potential impact of SSRF vulnerabilities.

```bash
sudo iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A OUTPUT -p tcp --dport 443 -j ACCEPT
sudo iptables -A OUTPUT -j DROP
```
In the above example, firewall (iptables) restricts outbound traffic except for ports 80 and 443 which are generally used for HTTP and HTTPS traffic respectively.

### Step 2: Whitelist or Blacklist IP Addresses and Ports

Depending on the requirements, you can setup a whitelist of IPs that can be accessed.

```python
# example in Python
allowed_ips = ['192.0.2.0', '203.0.113.0']

def connect(ip_address):
    if ip_address not in allowed_ips:
        raise Exception('Connection to this IP is not allowed.')
    # connection logic here
```

### Step 3: Use a Web Application Firewall (WAF)

Use a WAF that has capability to detect and block SSRF attacks.

### Step 4: Avoid Exposing Unnecessary Services.

This can reduce the attack surface.

```bash
sudo netstat -tunl
# Look for any unnecessary services and disable them
```