# Remediation for SSRF_ON_FILES

## Remediation Steps for Exposed AWS Details via SSRF

AWS credentials exposed through SSRF vulnerabilities can offer attackers unauthorized access to the cloud resources. Properly configuring access to AWS resources can help prevent this security issue.

### Step 1: Remove Direct Internet Access to Localhost

Making the localhost inaccessible from the internet denies SSRF attacks since they can't reach the metadata endpoint.

```javascript
//Express Middleware
const blockHostMiddleware = (req, res, next) => {
    const host = req.hostname;
    if(host === 'localhost' || host === '127.0.0.1') {
        return res.send({error: "Invalid request"});
    }
    next();
}
app.use(blockHostMiddleware);
```

Above, we are using an Express middleware in Node.js which denies any requests that try to access `localhost`.

### Step 2: Employ Allowlists

Develop a list of known URLs and only allow those that you trust. This shields against SSRF by preventing requests to URLs outside of the list.

```javascript
// Some configurations or setups 
const trusted_domains = ["trusted1.com", "trusted2.com"];

// Middleware
const allowlistMiddleware = (req, res, next) => {
    const domain = getUrlDomain(req.url);
    if (!trusted_domains.includes(domain)) {
        return res.send({error: "Invalid request"});
    }
    next();
}
app.use(allowlistMiddleware);
``` 

### Step 3: Add Firewall Rules

Setting up firewall rules to blacklist metadata related IP (`169.254.169.254`) can prevent unauthorized access.

```bash
sudo iptables -A OUTPUT -d 169.254.169.254 -j DROP
```

### Step 4: Implement IAM Roles

Use AWS IAM roles instead of embedding AWS credentials within your application. The IAM roles can be then restricted to only have the required permissions.

Refer to AWS documentation for setting this up as it requires AWS management console or AWS CLI.