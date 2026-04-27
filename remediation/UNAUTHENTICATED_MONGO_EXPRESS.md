

## Remediation Steps for Mongo Express Unauthenticated Access

Unauthenticated access to Mongo Express can let unauthorized users view and modify your database. It's important to secure your database with authentication to prevent unauthorized access.

### Step 1: Enable Authentication in MongoDB

MongoDB authentication should be enabled to secure your database. Here's a sample code in Node.js for MongoDB connection with authentication.

```javascript
const mongoose = require('mongoose');

const dbuser = 'admin';
const dbpassword = 'password123';
const url = `mongodb://${dbuser}:${dbpassword}@localhost:27017/myDB`;

mongoose.connect(url, {
  useNewUrlParser: true,
  useCreateIndex: true,
  useUnifiedTopology: true,
});
```

### Step 2: Configure Mongo Express for Authentication

In your `mongo-express` configuration file, make sure to enable authentication.

```javascript  
module.exports = {
    mongodbAdminUsername: 'meAdmin',
    mongodbAdminPassword: 'password123',
    useBasicAuth: true,
    basicAuth: {
        username: 'admin',
        password: 'password123'
   }
}
```

Remember to replace `'meAdmin'`, `'password123'`, and `'admin'` with your own admin username, password, and basic auth credentials.

### Step 3: Use Secure Connection

Always use encrypted connection (HTTPS) when connecting to your Mongo Express instance. 

For example, in Nginx, you can configure SSL as shown below:

```bash
server {
	listen 80;
	server_name yourdomain.com;
	return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:8081;
    }
    ssl_certificate /etc/letsencrypt/live/myblog.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/myblog.com/privkey.pem;
}
```