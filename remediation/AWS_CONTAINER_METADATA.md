

## Remediation Steps for AWS Container Metadata Content Exposure

AWS Container Metadata Content Exposure can lead to serious security breaches if not handled properly. The metadata service provides data about the container that may contain sensitive information. Unauthorized access to this info could lead to a compromise of the container.

### Step 1: Disabling IMDSv1 & Enabling IMDSv2

Firstly, to mitigate this vulnerability, we should disable EC2 instance Metadata Service version 1 (IMDSv1) and only allow version 2 (IMDSv2). This can be done during or after the EC2 instance creation.

During creation, AWS Management Console provides an option to enforce only IMDSv2 as follows:
    
```bash
aws ec2 run-instances --image-id ami-abc12345 --count 1 --instance-type t2.micro \
--metadata-options "HttpTokens=required"
```
  
If the EC2 is already running, modify the instance with modify-instance-metadata-options command
    
```bash
aws ec2 modify-instance-metadata-options --instance-id i-1234567898abcdef0 \
--http-tokens required
```

### Step 2: Update Existing Applications

Make sure all your existing applications adjust to use IMDSv2 by ensuring they include a PUT request to the IMDSv2 session to fetch instance metadata.

```python
import requests
import json

# Make a PUT request to create a token for metadata service
token = requests.put("http://169.254.169.254/latest/api/token", headers = {"X-aws-ec2-metadata-token-ttl-seconds": "21600"}).text

# Get the metadata
metadata = requests.get("http://169.254.169.254/latest/meta-data", headers = {"X-aws-ec2-metadata-token": token}).text

print(metadata)
```