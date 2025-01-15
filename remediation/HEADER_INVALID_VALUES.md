# Remediation for HEADER_INVALID_VALUES

## Remediation Steps for Header Invalid Values
Potential security issues arise when the application does not validate or verify the HTTP headers properly. This could make the application susceptible to attacks like HTTP Response Splitting, Cross-site scripting (XSS), Clickjacking and other Injection Attacks. 

Here are steps to implement remediation for invalid header values.

### Step 1: Validate and Sanitize Inputs 

This is the first and most important step. Always verify and sanitize headers from the client-side.
One logical way to perform this is to use an allow list of accepted values. If the header does not meet these values, reject it.

```java
if(!ALLOWED_HEADERS.contains(header from client)){
    throw new SecurityException("Invalid Header Value");
}
```
### Step 2: Set HTTP Security Headers

Next, to secure HTTP Headers, ensure the server responses include the following security headers.

* Content-Security-Policy
* X-Content-Type-Options
* Strict-Transport-Security
* X-Frame-Options
* X-XSS-Protection

These headers can be set in the configuration file or at the server level. Here's an example how to do that in a Node.js Express server.

```javascript
const helmet = require('helmet');

app.use(helmet.hidePoweredBy());
app.use(helmet.frameguard()); 
app.use(helmet.xssFilter());
app.use(helmet.noSniff()); 
app.use(helmet.ieNoOpen());
app.use(helmet.hsts({ 
  maxAge: 7776000000,
  includeSubDomains: true
}));
```