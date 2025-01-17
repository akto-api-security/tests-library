

## Remediation Steps for AWS Misconfigured CDN Cache Poisoning
AWS Misconfigured CDN Cache Poisoning is a serious security issue which can compromise clients' sensitive data by serving malicious content when they requests data from your AWS CloudFront distribution.
### Step 1: Reviewing and Updating Header Configurations
Headers play an important role in preventing cache poisoning by influencing caching behavior of your AWS CloudFront. Ensure that you have set such headers that decide the caching behavior in accordance with your requirements and specifications. 

Various headers include `Cache-Control`, `Pragma`, and `Expires`. Always include the `Vary` HTTP header to inform CloudFront about the multi-variant nature of your cached data.
```json
{
    "parameters": {
        "lambdaFunctionAssociations": {
            "lambdaFunctionARN": "ARN_Of_Your_AWS_Resource",
            "eventType": "origin-response",
            "includeBody": false
        },
        "responseHeadersPolicy": {
            "cacheControl": {
                "behavior": "override",
                "value": "public, max-age=86400"
            },
            "vary": {
                "behavior": "override",
                "value": "*"
            }
        }
    }
}
```
### Step 2: Changing Default TTL and Max TTL values
Ensure that you have set apt `Default TTL` (Time to Live) and `Max TTL` values for your Cloudfront distribution. This decides for how long Cloudfront shall cache an object before it checks the origin again to see if the content has been updated.
```json
{
    "distributionConfig": {
        "defaultTTL": 86400,
        "maxTTL": 31536000
    }
}
```
### Step 3: Implement AWS WAF to Prevent Cache Poisoning Attacks
AWS WAF(WAF - Web Application Firewall) service can be used to put conditional rules that inspect HTTP/S requests coming to your CloudFront distributions or API Gateway.
```json
{
    "name": "BlockCachePoisoning",
    "priority": 1,
    "statement": {
        "IPSetReferenceStatement": {
            "arn": "ARN_of_AWS_WAF_IPSet"
        }
    },
    "visibilityConfig": {
        "sampledRequestsEnabled": true,
        "cloudWatchMetricsEnabled": true,
        "metricName": "SecurityMetrics"
    }
}
```
### Step 4: Regular Monitoring and Audit
Keep regular track of your Cloudfront distribution behavior, HTTP headers settings and AWS WAF logs for any suspicious activities.
```bash
aws cloudfront get-distribution --id EDFDVBD632BHDS5
aws wafv2 get-webacl --name 'WebACL_For_CloudFront_Distribution' --scope REGIONAL --id 'WebACL_ID'
```