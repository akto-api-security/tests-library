# Remediation for ROBOMONGO_CREDENTIAL

## Remediation Steps for MongoDB Credential Disclosure
MongoDB credential disclosure is a serious security concern. Without properly securing MongoDB, attackers may gain unauthorized access to sensitive data and use it maliciously. 

### Step 1: Enable Access Control
Enabling access control will require all clients to identify themselves before they can perform actions on the database.

You can enable access control using the `--auth` parameter when starting the `mongod` process.

```bash
mongod --auth
```

### Step 2: Create User Administrator
Once access control is enabled, you need to create the user administrator. The user administrator is a special user capable of adding, removing and managing other MongoDB users.

In the MongoDB shell, use the following commands:

```bash
use admin
db.createUser(
  {
    user: "myUserAdmin",
    pwd: "abc123",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
  }
)
```

### Step 3: Authentication
To authenticate as the user administrator, you need to disconnect the MongoDB shell and reconnect with credentials.

```bash
mongo --port 27017 -u "myUserAdmin" -p "abc123" --authenticationDatabase "admin"
```

### Step 4: Create Additional Users
Once connected as the user administrator, you can create additional users as needed.

```bash
use myDatabase
db.createUser(
  {
    user: "myDBUser",
    pwd: "abc123",
    roles: [ { role: "readWrite", db: "myDatabase" } ]
  }
)
```

### Step 5: Regular Audit and Update
Ensure MongoDB is regularly updated and audited for any lingering or potential security threats. 

Moreover, avoid sharing sensitive information, like MongoDB credentials, within your application code and use environment variables instead. 

```bash
export MONGO_USER=<username>
export MONGO_PASSWORD=<password>
```

In your MongoDB connection string, replace the hardcoded username and password with these environment variables. 

```javascript
const mongoUser = process.env.MONGO_USER;
const mongoPassword = process.env.MONGO_PASSWORD;

const mongoUri = `mongodb://${mongoUser}:${mongoPassword}@localhost:27017/myDatabase`;
```
Remember to restart your application after setting the environment variables.