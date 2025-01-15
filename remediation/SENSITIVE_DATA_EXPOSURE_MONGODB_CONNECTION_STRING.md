# Remediation for SENSITIVE_DATA_EXPOSURE_MONGODB_CONNECTION_STRING

## Remediation Steps for MongoDB Connection String Exposure
Exposing sensitive information, such as MongoDB connection strings, can lead to unauthorized access to databases. This can have serious implications on data privacy and the integrity of your application. Therefore, it is of utmost importance to keep such details hidden and secure.

### Step 1: Store Connection String in Environment Variables
Instead of hardcoding the connection string into your source code, use environment variables to store the string.

Here is an example in Node.JS:

```javascript
const mongoose = require("mongoose");
const connectionString = process.env.MONGODB_URI;

mongoose.connect(connectionString, { useNewUrlParser: true, useUnifiedTopology: true })
```

Here, `MONGODB_URI` is an environment variable that contains the MongoDB connection string. 

### Step 2: Use .env Files
For a more organized way of handling environment variables, you can make use of .env files. Do not forget to add the .env file to .gitignore to ensure that it does not get committed to version control.

```bash
touch .env
echo "MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority" >> .env
```
And in your Node.js file:

```javascript
require('dotenv').config();
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true })
```

### Step 3: Use A Secrets Manager
For further security, consider using a secrets manager, such as AWS Secrets Manager or HashiCorp Vault, to store sensitive data like connection strings. This helps in securely storing, retrieving, and managing secrets across your infrastructure.
