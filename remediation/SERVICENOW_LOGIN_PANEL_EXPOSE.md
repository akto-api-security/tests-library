

## Remediation Steps for ServiceNow Login Panel Exposure

ServiceNow login panel exposure could be a serious security risk as it may allow unauthorized access to the system. The following steps will help you to remediate this issue.

### Step 1: Enable Multi-Factor Authentication

Enabling Multi-Factor Authentication (MFA) will add an extra layer of protection to your ServiceNow accounts. You can do it using the following steps on service now:

```javascript
//Navigate to Multi-Provider SSO > Identity Provider
//Open an existing Identity Provider, or create a new one
//In the Advanced Parameters related list, set the 'x509.user.mfa' to true
```

### Step 2: Restrict Public Access

Ensure you only allow access to your ServiceNow instance from trusted IP addresses. Use the IP Address Access Control Lists (ACL) to accomplish this:

```javascript
//Navigate to System Definition > Interactive Filter
//Use Smart Filters to help create rule base definitions
//Set the 'Source IPs' field to the specific IP addresses you want to whitelist
```

### Step 3: Use Encrypted Sessions

All connections to the ServiceNow platform should be encrypted using SSL (Secure Sockets Layer).  

```javascript
//Navigate to System Properties > Security
//Enable the 'glide.ui.session_secure' parameter to enforce the use of secure HTTP connections
```