

## Remediation Steps for Node.js Ecstatic Package - Directory Listing
Ecstatic package is a static file server middleware for Node.js. This includes servers created with http & express. It is crucial to avoid directory listing to prevent unauthorized access to directories as it can lead to sensitive data exposure.

### Step 1: Update Ecstatic Package
First, check your current version of Ecstatic by running the following command. If the version is below 2.0.0, your server might have a directory listing vulnerability.
```bash
npm list ecstatic
```
If so, update Ecstatic to the latest version using the following command.
```bash
npm update ecstatic
```

### Step 2: Configure Ecstatic options
The default behaviour of Ecstatic allows directory listing. To turn it off, set `showDir` and `autoIndex` options to false when configuring the middleware.
```javascript
const  ecstatic = require('ecstatic');

app.use(ecstatic({
  root: `${__dirname}/public`,
  showDir : false,
  autoIndex: false
}));
```
This will disable directory listings, even if the `index.html` file is missing in your directory. 