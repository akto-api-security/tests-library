

## Remediation Steps for Nodejs Squirrelly Remote Code Execution

Remote Code Execution (RCE) in Squirrelly templates is a serious security issue. Attackers can execute arbitrary code on the server using a malicious template.

Here's how to remediate the issue:

### Step 1: Update `squirrelly` package

First thing to do is to update the `squirrelly` package to the latest version that has fixed the vulnerability.
You can use the following command to update it.

```bash
npm update squirrelly
```
You might need to use `sudo` for global installations or installations that require root permissions.

### Step 2: Template User Input Validation

Explicitly control and filter user input in template expressions to prevent execution of malicious code. 

This could be achieved by using a function like the following:

```javascript
function escape(input) {
    return input.replace(/[\\"']/g, '\\$&')
                .replace(/\u0000/g, '\\0')
                .replace(/</g,'&lt')
                .replace(/>/g, '&gt;');
}

let userInput = getUserInput();
let safeInput = escape(userInput);
res.render('template', { input: safeInput });
```