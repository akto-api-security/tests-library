# Remediation for EMBEDDED_JS_TEMPLATE_INJECTION

## Remediation Steps for Embedded Javascript Template Injection

Embedded Javascript (EJS) Template Injection can lead to severe security issues. Attackers might take advantage of such vulnerabilities to inject malicious script and compromise application security. 

### Step 1: Properly Escape User Input

Before the application places user-controlled data into HTML templates, always strive to properly escape it. This behavior will prevent attackers from injecting malicious code into your application. In JavaScript, you can use a built-in function to escape HTML. 

Here is an example using built-in escaping functions in JavaScript:

```javascript
let username = userInput;
username = username.replace(/&/g, "&amp;");
username = username.replace(/</g, "&lt;");
username = username.replace(/>/g, "&gt;");
username = username.replace(/"/g, "&quot;");
username = username.replace(/'/g, "&#039;");
```

### Step 2: Use Helmet's Content Security Policy 

Helmet's Content Security Policy helps prevent all sorts of injection and cross-site scripting attacks, including EJS injection.

```javascript
const express = require('express');
const helmet = require('helmet');
const app = express();

let scriptSources = ["'self'", "'unsafe-inline'"];
app.use(helmet.contentSecurityPolicy({
    directives: {
        scriptSrc: scriptSources
    }
}));

app.listen(3000);
```
### Step 3: Carefully Use Template Tags

In EJS, use `<%- %>` to render unescaped HTML and `<%= %>` to escape HTML. You should only use `<%- %>` when you can completely trust the dynamic content you're injecting into your templates.

Improper use:

```javascript
let unsafeVariable = "<script> malicious script </script>"
res.render('template', { title: '<%- unsafeVariable %>'})
```

Safe use:

```javascript
let potentiallyUnsafeVariable = "<script> potentially malicious script </script>"
res.render('template', { title: '<%= potentiallyUnsafeVariable %>'})
```

### Step 4: Use Artillery for Load & Testing 

Artillery is great for testing your application against any potential EJS, XSS, or SQL injections, and it can help uncover any vulnerabilities.

```bash
npm install -g artillery
```