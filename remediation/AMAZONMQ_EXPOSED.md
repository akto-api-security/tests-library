# Remediation for AMAZONMQ_EXPOSED

## Remediation Steps for Exposed AmazonMQ
Exposed AmazonMQ is a severe security issue. Without proper configurations, unauthorized users could potentially gain access to your sensitive data.
### Step 1: Enforce AmazonMQ Access Control
Use IAM policies to manage access to your AmazonMQ resources. Make sure you apply the principle of least privilege, and only give necessary permissions to users.

Here is the example to add a policy:
```bash
aws iam create-policy --policy-name MyAmazonMQPolicy --policy-document file://my-amazonmq-policy.json
```
And the content of `my-amazonmq-policy.json` could be:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "mq:CreateBroker",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "mq:ListBrokers",
            "Resource": "*"
        }
    ]
}
```

### Step 2: Enable AmazonMQ Logging
Logging can provide additional visibility into your AmazonMQ environment and its usage. However, to make sure you're not exposing any sensitive information in logs, restrict access to logs wherever possible.

You can enable AmazonMQ logging by modifying the broker like this:

```bash
aws mq update-broker --broker-id MyBroker --logs Audit=true,General=true
```

### Step 3: Encryption in Transit
To protect data 'in transit', enable SSL encryption. This will ensure that all data flowing through the network between AmazonMQ client and the broker is encrypted.

By enabling the `ssl://` prefix in your broker URL, you can enforce SSL. It should look like this: 
```
ssl://b-example-1.mq.us-east-2.amazonaws.com:61617
```


### Step 4: Encrypt Data at Rest
Use AWS Key Management Service (AWS KMS) managed keys (CMK) to encrypt your data at rest. This protects your data and configurations stored in the broker.

You can specify the `KmsKeyId` parameter when you create a broker:
```bash
aws mq create-broker --broker-name MyBroker --engine-type ActiveMQ --engine-version 5.15.10 --host-instance-type mq.t2.micro --auto-minor-version-upgrade --deployment-mode SINGLE_INSTANCE --kms-key-id alias/aws/mq
```