

## Remediation Steps for Broken Authentication Test - Username Enumeration on Captcha Endpoint
Username enumeration allows an attacker to determine the existence of a specific user on a system. This could be exploited to attempt 'password guessing' for existing accounts. Therefore, protecting endpoints from username enumeration is crucial for enhancing security.

### Step 1: Implement Rate Limiting
Rate limiting should be implemented for every user interaction, especially ones that can reveal sensitive information, like the captcha endpoint. Rate limiting can be achieved using a middleware mechanism. Below is a sample code using Node.js with Express:

```javascript
const rateLimit = require("express-rate-limit");

// Enable rate limit
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});

app.use("/captcha-endpoint", limiter);
```

### Step 2: Add data for Non-Existent Users
Respond with intentionally invalid or random data when queried for non-existent users. This prevents attackers from distinguishing between existing and non-existing users based on the captcha endpoint's response.

