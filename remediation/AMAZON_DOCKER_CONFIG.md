

## Remediation Steps for Dockerrun AWS Configuration Exposure

Dockerrun AWS Configuration Exposure is a serious issue that could reveal the sensitive configuration details related to your AWS deployment. To remediate this vulnerability, you will need to manage access to your Dockerrun file, encrypt sensitive data, and ensure regular audits.

### Step 1: Control Access to Dockerrun Files

To minimize this exposure, you need to limit access to Dockerrun.aws.json files. These files must remain private.

```bash
chmod 700 Dockerrun.aws.json
```

### Step 2: Secure Your AWS Credentials

You will also want to manage your AWS credentials using AWS Secrets Manager or AWS Identity and Access Management (IAM). Never put any secret keys directly in the Dockerrun.aws.json.

```bash
# Example of saving secrets in Secrets Manager
aws secretsmanager create-secret --name MyAwsSecrets \
--secret-string file://secrets.json

# Your Dockerrun.aws.json should reference these secrets, like so:
{
   "AWSEBDockerrunVersion": "1",
   "Authentication": {
     "Bucket": "my-bucket",
     "Key": "my-key"
   },
   ...
}
```

### Step 3: Regular Security Reviews

Ensure regular audits of access logs and regularly update the security methods used.

```bash
# Regularly audit your AWS account
aws configure set aws_access_key_id <Your_Access_Key>
aws configure set aws_secret_access_key <Your_Secret_Key>
aws cloudtrail lookup-events --lookup-attributes AttributeKey=Username,AttributeValue=root
```

### Step 4: Consider Using Instance Profiles 

Consider using instance profiles to delegate permissions to make requests from the instances that host your application to other AWS service resources.

```bash
# Example to create a role and assign to instance profile
aws iam create-role --role-name my-instance-profile-role --assume-role-policy-document file://TrustPolicyForEC2.json
aws iam create-instance-profile --instance-profile-name my-instance-profile
aws iam add-role-to-instance-profile --role-name my-instance-profile-role --instance-profile-name my-instance-profile
```