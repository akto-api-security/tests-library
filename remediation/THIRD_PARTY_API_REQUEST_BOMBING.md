# Remediation for THIRD_PARTY_API_REQUEST_BOMBING

## Remediation Steps for Denial of Service Test on 3rd Party API Endpoints
Third party API endpoints must be properly secured to prevent Denial of Service (DoS) attacks. An attacker can attempt a DoS attack by excessively replaying requests, which can overwhelm the API server and cause a service outage or slowdown. 

### Step 1: Rate Limiting
The most common way to protect against this is to use Rate Limiting. Depending on your API server or application platform, implementation of this may vary. 

In Python, you can use the Flask-Limiter extension. 

```python
from flask import Flask
from flask_limiter import Limiter

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address, default_limits=["200 per day", "50 per hour"])

@app.route('/')
@limiter.limit("20 per minute")  # adjust this limit based on your needs
def index():
    return "Hello, World!"
```
Remember to adjust the limits according to your capacity and needs. 

### Step 2: Caching Responses
Another way to protect against DoS attacks is to cache responses, so repeated requests will not reach the server after first time.

Here's a simple example using Redis cache in NodeJS:

```javascript
const express = require('express');
const redis = require('redis');
const axios = require('axios');

const client = redis.createClient();
const app = express();

app.get('/data', (req, res) => {
    const requestData = req.query;

    return client.get(`cachedData:${requestData}`, async (error, data) => {
        if (error) throw error;

        if (data) {
            return res.send({
                data: JSON.parse(data),
                message: "data retrieved from the cache"
            });
        } else {
            const response = await axios.get('https://external-api.com/data');
            client.setex(`cachedData:${requestData}`, 3600, JSON.stringify({ source: 'Redis Cache',...response.data}));

            return res.send({
                data: response.data,
                message: "cache miss"
            });
        }
    });
});
```

### Step 3: Regular Audits
Ensure to perform regular audits of the server logs to detect any suspicious activity or patterns within the API Requests.

### Step 4: Have a Crisis Plan
Even with safeguards, things can go wrong. Always have a disaster recovery plan and capability for rapid response to potential incidents.