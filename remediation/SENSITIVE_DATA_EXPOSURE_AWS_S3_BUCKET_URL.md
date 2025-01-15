# Remediation for SENSITIVE_DATA_EXPOSURE_AWS_S3_BUCKET_URL

## Remediation Steps for AWS S3 Bucket URL Sensitive Data Exposure

Sensitive data exposure through AWS S3 Bucket URLs can lead to unauthorized access to sensitive data. To prevent this, ensure that your S3 buckets are properly secured.

### Step 1: Change the AWS S3 bucket policy
Identify the S3 bucket that is exposing sensitive data and modify its Access Control Lists (ACLs) and bucket policies to restrict public access.

Here is an example using AWS CLI:

```bash
# Get current bucket policy
aws s3api get-bucket-policy --bucket YOUR_BUCKET_NAME

# Put new restricted policy
aws s3api put-bucket-policy --bucket YOUR_BUCKET_NAME --policy file://policy.json
```
The `policy.json` file should look something like this:

```json
{
    "Id": "Policy1589395294458",
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1589395249427",
            "Action": [
                "s3:GetObject"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*",
            "Principal": "*"
        }
    ]
}
```
Replacing `YOUR_BUCKET_NAME` with your bucket name.

### Step 2: Enable bucket versioning:

Versioning allows you to preserve, retrieve, and restore every version of every object in your bucket. This means you can easily recover from both unintended user actions and application failures. You can use versioning to preserve, retrieve, and restore every version of every object in your Amazon S3 bucket.

Here is how to enable it using AWS CLI:

```bash
aws s3api put-bucket-versioning --bucket YOUR_BUCKET_NAME --versioning-configuration Status=Enabled
```

### Step 3: Regularly audit AWS S3 bucket permissions:

Periodic audits of AWS S3 bucket permissions help identify any errant permissions that might expose sensitive data.

`AWS Trusted Advisor` or `AWS Config` could be used for auditing the resources.

### Step 4: Encrypt S3 buckets:

Use AWS S3 default encryption to automatically apply server-side encryption for all new objects in the bucket.

Here’s how to enable default encryption using AWS CLI:

```bash
aws s3api put-bucket-encryption --bucket YOUR_BUCKET_NAME --server-side-encryption-configuration '{"Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]}'
```

Don't forget to replace `YOUR_BUCKET_NAME` with your actual bucket name in all above examples.