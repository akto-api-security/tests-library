# Remediation for SENSITIVE_DATA_EXPOSURE_AWS_SQS_URL

## Remediation Steps for Sensitive Data Exposure - AWS SQS URL

Exposing sensitive data like AWS SQS URLs could provide an unauthorized user endpoint access. Here's how to secure it:

### Step 1: Protect AWS SQS URL
Do not embed or hardcode AWS SQS URL in the source code. Store it in a secure environment variables or use AWS Secrets Manager to manage secrets.

In Python:

```python
import boto3
import os

def get_sqs_url():
    sqs_url = os.getenv('SQS_URL')
    return sqs_url

def main():
    sqs_url = get_sqs_url()
    sqs = boto3.client('sqs')

    response = sqs.receive_message(
      QueueUrl=sqs_url,
      MaxNumberOfMessages=1
    )

if __name__ == '__main__':
    main()
```

### Step 2: Use IAM roles and policies
Use IAM roles and policies to give needed permissions for AWS SQS. Avoid highly privileged role.

Policy example in JSON:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sqs:SendMessage",
            "Resource": "arn:aws:sqs:us-east-1:123456789012:MyQueue"
        },
        {
            "Effect": "Allow",
            "Action": "sqs:ReceiveMessage",
            "Resource": "arn:aws:sqs:us-east-1:123456789012:MyQueue"
        }
    ]
}
```

### Step 3: Enable server-side encryption (SSE) for SQS
Your data (both in transit and at rest) should be encrypted. AWS provides server-side encryption (SSE). 

Here is a Python boto3 example of how to create a queue with SSE enabled:

```python
import boto3

sqs = boto3.client('sqs', region_name='us-east-1')
queue = sqs.create_queue(
    QueueName='MyQueue',
    Attributes={
        'KmsMasterKeyId': 'alias/aws/sqs',  # Use the default AWS managed CMK
        'KmsDataKeyReusePeriodSeconds': '300'  # 5 minutes
    }
)
```