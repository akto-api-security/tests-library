# Remediation for NODE_ECSTATIC_INTERNAL_PATH_EXPOSURE

## Remediation Steps for Node.js Ecstatic Package - Internal Path Exposure

Internal path exposure within the ecstatic package for Node.js can lead to unauthorized access to internal files. This vulnerability could allow attackers to read or write files outside of the intended directory. 

### Step 1: Update Ecstatic Package 

First, you need to update the Ecstatic Package. The issue persist in Ecstatic package version below "4.1.2". Make sure you are using version "4.1.2" or later.

The vulnerability is fixed in version "4.1.2". For this, use the following commands:

```bash
npm uninstall ecstatic
npm install ecstatic@4.1.2
```

### Step 2: Verify the package version 
You can use following command to ensure that ecstatic has been updated to 4.1.2 or higher. 

```bash
npm list ecstatic
```

### Step 3: Restrict access to certain directory
Even after updating the Ecstatic package, as a best practice you should limit the access to only certain directory. To do this, you need to specify the root directory in the ecstatic function like this:

```javascript
require('http').createServer(require('ecstatic')({ root: __dirname + '/public' })).listen(8080);
```
This will make ecstatic serve only files from './public' directory.