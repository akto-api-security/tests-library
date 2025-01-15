# Remediation for MONGO_EXPRESS_RCE

## Remediation Steps for Mongo-Express Remote Code Execution
The remote code execution issue in Mongo-Express allows an authenticated user, by sending a crafted HTTP request, to execute arbitrary JavaScript code with the privileges of the Mongo-Express service.

### Step 1: Update Mongo-Express
The issue has been addressed in the newer versions of Mongo-Express, thus, the most straightforward remediation is to update it to the latest version.

```bash
npm update mongo-express
```

### Step 2: Enforce password protection
Ensure that your instance of Mongo-Express is running with password protection enabled.

In your `config.js` file for Mongo-Express:

```javascript
module.exports = {
  //... other settings,
  mongodb: {
    //... other settings,
    admin: { // change to your db's name
      username: 'your_username', // Use your username
      password: 'your_password', // Use your password
    },
    //... other settings,
  },
  //... other settings,
};
```