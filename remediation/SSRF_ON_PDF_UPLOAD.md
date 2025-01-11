# Remediation for SSRF_ON_PDF_UPLOAD

## Remediation Steps for Exposed AWS Details via Replace PDF Param due to SSRF

Server Side Request Forgery (SSRF) is a serious security issue in which a server is tricked into making requests that it should not be making. When this happens in context with AWS, it can potentially expose sensitive AWS details.

### Step 1: Implement Input Validation and Whitelisting

Validate user input to ensure it is in the format you expect. Whitelisting is a powerful technique to block off unwanted external entities from making requests.

```python
import re

def is_valid_url(url):
    pattern = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    )
    return pattern.match(url) is not None

def whitelisted_url(url, whitelist):
    # hostname can be 'mywebsite.com' or 'api.mywebsite.com'
    hostname = url.split("//")[-1].split("/")[0].split(":")[0].lower()
    return any(allowed in hostname for allowed in whitelist)
```

### Step 2: Implement Network Layer Access Controls

Implement firewall rules to prohibit outbound requests to internal network subnets, AWS instance metadata endpoint, etc. This may be achieved at the network level or at the application level.

```bash
aws ec2 authorize-security-group-egress --group-id sg-05******* --protocol tcp --port 8080 --cidr 203.0.113.1/24
```

### Step 3: Regular Scanning and Patching

Regularly check for SSRF vulnerabilities in your codebase and apply patches.

```bash
pip install safety
safety check
```

### Step 4: Use Secrets Manager or Parameter Store

To store sensitive information like AWS details, use AWS Secrets Manager which has built-in integrations for replacing plaintext secrets in common text files (like JSON) with encrypted values.

```bash
aws secretsmanager create-secret --name MyAwesomeSecret --secret-string '{
  "username":"aws-user",
  "password":"aws-password"
}'
```

### Step 5: IAM Roles and Policies

Ensure that IAM roles and policies are correctly configured to limit the permissions that your application has.

```bash
aws iam create-role --role-name myrole --assume-role-policy-document file://Policyfile.json
```