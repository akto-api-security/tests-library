

## Remediation Steps for Sensitive Files Exposed Due to SSRF

Server Side Request Forgery (SSRF) is a type of vulnerability that allows an attacker to make requests to any servers reachable from the server that has the vulnerability.  

### Step 1: Validate all incoming requests
Ensure that all incoming requests are validated against a list of known good inputs. This can be achieved through a white-listing method that only allows certain requests to be processed.

```python
def is_valid(request):
    # Assuming `valid_requests` is a pre-defined list of valid requests
    valid_requests = ['http://example1.com', 'http://example2.com']
    return request in valid_requests
```

### Step 2: Block Outgoing Requests
Block unnecessary outgoing requests from the server. This means ensuring that the server isn't making any outgoing requests to resources that it shouldn't need. It will require understanding and analyzing the server's normal behavior to determine what outbound connections are permissible.

```bash
sudo iptables -A OUTPUT -p tcp --dport 80 -j DROP
sudo iptables -A OUTPUT -p tcp --dport 443 -j DROP
```

### Step 3: Run regular vulnerability scans
Ensure that regular vulnerability scans are run on the server, and any issues are patched immediately. This will help in identifying any new SSRF vulnerabilities that may be introduced in the system during updates or system changes.

```bash
sudo yum install openvas
sudo openvas-setup
```

### Step 4: Audit server logs regularly
Ensure that the server logs are audited regularly to identify and block any IP addresses or URLs that are repeatedly making suspicious requests.

```bash
cat /var/log/apache2/access.log | awk '{print $1}' | sort | uniq -c | sort -nr | head -10
```

### Step 5: Protection at code level
Prevent SSRF vulnerabilities at the code level by limiting URL redirection and remote file inclusion, validating all user input, and safe usage of APIs. Consider using sandboxing for potential harmful actions. 

```java
import java.net.URL;

public URL makeURL(String str) throws MalformedURLException {
    URL url = new URL(str);
    if (!"http".equals(url.getProtocol())) {
        throw new MalformedURLException("Only 'http' URLs are allowed.");
    }
    return url;
}
```
Remember, this list isn't exhaustive, and treating the symptoms (such as patching specific SSRF vulnerabilities) is not enough – treat the root cause by incorporating security into your coding standards and perform regular code reviews to catch these issues before they become a critical problem.