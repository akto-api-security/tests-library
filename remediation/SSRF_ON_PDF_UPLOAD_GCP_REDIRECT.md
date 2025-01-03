# Remediation for SSRF_ON_PDF_UPLOAD_GCP_REDIRECT

## Remediation Steps for Exposed Sensitive GCP Details via SSRF

When sensitive Google Cloud Platform (GCP) details are exposed by replacing a PDF parameter with a redirection due to Server Side Request Forgery (SSRF), it's a severe security risk. Such an issue could allow attackers to gain unauthorized access to your GCP resources and potentially manipulate them. Here are steps on how to remediate this issue:

### Step 1: Validate the incoming URLs
The application needs to validate incoming URLs before sending requests to them. This can be accomplished via a URL allowlist.

```python
import urllib

def is_valid_url(url, allowed_domains):
    parsed_url = urllib.parse.urlparse(url)
    return parsed_url.netloc in allowed_domains

# Example usage:
allowed_domains = ["example.com", "subdomain.example.com"]
is_valid_url("http://attackersite.com", allowed_domains)  # Returns False
```
### Step 2: Use a proper outgoing proxy
Your application should use a proper outgoing proxy for making requests.

For example in Python:
```python
import requests

def fetch_url(proxy_url, target_url):
    proxies = {
      'http': proxy_url,
      'https': proxy_url,
    }
    response = requests.get(target_url, proxies=proxies)
    return response.content

# Example usage:
fetch_url("http://localhost:8080", "http://example.com")
```
### Step 3: Restrict outbound connections
Limit the application's outbound connections only to the necessary GCP services.

```bash
sudo ufw deny out to any
sudo ufw allow out to <GCP-services-ip-address> 
```
### Step 4: Regular Audit and Update:
Make sure to regularly audit your application for any signs of security issues and update your GCP IAM roles and permissions as needed.

If your application is running on Compute Engine instances, make sure to use Service Accounts and limit their permissions to the bare minimum that your application needs.

Also, understand and correctly implement [VPC Service Controls](https://cloud.google.com/vpc-service-controls/docs) to limit the exposure of your GCP resources.