# Remediation for NODE_SRV_LFI

## Remediation Steps for Node-srv Local File Inclusion

Local File Inclusion (LFI) is a type of vulnerability that allows an attacker to read files from the server. The attacker can exploit this vulnerability on a Node-srv server if the user input is improperly sanitized. Here are the steps to remediate this vulnerability:

### Step 1: Sanitize User Input 

The first line of defense against LFI attacks is to sanitize the user input properly. 

Node.js's in-built function 'normalize' can be used to avoid path manipulation and resolve '..' segments.

```javascript
const path = require('path');
let userPath = path.normalize(userInput);
```
### Step 2: Use Whitelisting Approach
Instead of relying solely on user input, you can take a whitelisting approach by using a switch statement.

```javascript
let filePath;
switch(userInput) {
    case 'file1': 
        filePath = '/path/to/file1';
        break;
    case 'file2': 
        filePath = '/path/to/file2';
        break;
    default: 
        filePath = '/path/to/default/file';
        break;
}
```

### Step 3: Implement Correct Error Handling
Make sure the error messages shown to the user do not give away any information about the structure of the server's files.

```javascript
app.use(function(err, req, res, next) {
  console.error(err.stack);
  res.status(500).send('An error occurred, please try again later.');
});
```