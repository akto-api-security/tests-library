# Remediation for NEXTJS_LFI

## Remediation Steps for Next.js Local File Inclusion

Local File Inclusion (LFI) in Next.js can enable an attacker to read or execute files on your server that they otherwise shouldn't have access to. Therefore, it's important to guard against it in your Next.js applications.

### Step 1: Validate User Input
To prevent LFI vulnerabilities, ensure to validate all user input data. Never use input data directly in file system operations without sanitization and validation. Use a allow-list of acceptable inputs. You can use libraries like Joi, express-validator or similar.

```javascript
import Joi from 'joi';

const schema = Joi.object().keys({
  file: Joi.string().valid('allow-list-file.txt', 'safe-to-include.txt'),
});

const result = schema.validate(req.body);

if (result.error) {
  throw new Error('Invalid file requested');
}

const file = result.value.file;
```

### Step 2: Avoid Dynamic Requires
Avoid requiring files based on user input data in Node.js or Next.js. This can lead to LFI vulnerability if not handled properly. Here is what a risky use of `require` might look like:

```javascript
function getUserModule(userId) {
  return require('./users/' + userId);
}
```

Instead, statically require known files and select between them:

```javascript
const users = {
  'user1': require('./users/user1'),
  'user2': require('./users/user2'),
  // [.. all users ..]
};

function getUserModule(userId) {
  return users[userId];
}
```

### Step 3: Sanitize File Paths
If you happen to handle file paths, sanitize the input to avoid any relative file path tricks (e.g., directory traversal). Use a node.js built-in module 'path' to normalize the input path, this makes sure you don't resolve to unintended files.

```javascript
import path from 'path';

const safePath = path.normalize(req.body.filePath).replace(/^(\.\.[\/\\])+/, '');
res.sendFile(safePath);
```

### Step 4: Use Static File Serving Mechanism
In Next.js, use the inbuilt static file serving mechanism to handle your public file serving needs, as this has been designed to avoid such vulnerabilities.

```javascript
import {useRouter} from 'next/router'

export default function Document(){
  const router = useRouter();

  if(typeof window !== 'undefined') {
    router.push('/file_location/'+encodeURIComponent(source));
  }

return <div />;
}
```