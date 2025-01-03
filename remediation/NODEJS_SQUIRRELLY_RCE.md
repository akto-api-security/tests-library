# Remediation for NODEJS_SQUIRRELLY_RCE

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
### Step 3: Regular Audits and Updates

Always keep the Node.js environment and its packages updated. Outdated packages often have unfixed vulnerabilities.
NPM provides auditing tools to identify packages with security issues. 

```bash
npm audit
```

This command will print a report of known vulnerabilities in the dependencies and will suggest how to fix them.

In a continuous integration pipeline, consider using `npm audit` to fail the build when the code has vulnerabilities.

Note: Always thoroughly test your application after any update or modification to ensure functionality is not broken.