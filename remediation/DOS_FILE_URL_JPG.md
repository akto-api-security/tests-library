

## Remediation Steps for Denial of Service Test with Large JPG File

Overloading your system with a large JPG file is a type of Denial-of-Service (DoS) attack. To prevent such attacks, you need to limit the size of files that can be uploaded or processed.

### Step 1: Limit Upload File Size

If you're using an HTTP server such as Nginx, you can limit the client's maximum request body size in the Nginx configuration file.

```bash
server {
    client_max_body_size 10M;   # Allows client request body size of up to 10 megabytes
}
```

### Step 2: Buffer Overflow Protection

Implement buffer overflow protection on your server code. Assuming you're using NodeJS, you can use the `raw-body` and `bytes` NPM modules to check the size of the file before processing.

```javascript
const getRawBody = require('raw-body')
const bytes = require('bytes')

app.use((req, res, next) => {
    getRawBody(req, {
        length: req.headers['content-length'],
        limit: '1mb',  // Limit the request body to 1mb
        encoding: true
    }, function (err, string) {
        if (err) return next(err)
        req.text = string
        next()
    })
});
```

### Step 3: Implement Rate Limiting
Implement rate limiting to prevent the excessive number of requests. This can be done using 'express-rate-limit' if you are using express.js.

```javascript
const rateLimit = require("express-rate-limit");

const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per windowMs
  message: "Too many requests, please try again later."
});

app.use("/api/", apiLimiter); // Only applies to requests that begins with /api/
```