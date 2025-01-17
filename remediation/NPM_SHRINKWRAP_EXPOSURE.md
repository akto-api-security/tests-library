

## Remediation Steps for NPM ShrinkWrap Exposure

NPM ShrinkWrap Exposure can lead to dependencies with known vulnerabilities being used in your applications. Shrinkwrap files lock down the versions of package's dependencies. If a version is specified in 'npm-shrinkwrap.json', npm will use it, even if there's a newer version that fixes a vulnerability.

### Step 1: Update packages
The primary source of this vulnerability comes from not regularly updating your packages. Therefore, the first step is always to update the packages.

```bash
npm update
```

### Step 2: Generate a new shrinkwrap file
Next we can generate a new shrinkwrap file. This will take into account all the modules installed in node_modules.

```bash
npm shrinkwrap
```

### Step 3: Delete the node modules folder and rebuild
Now we delete the node modules folder and rebuild it. This ensures that any remaining vulnerabilities in node modules are not left over.

```bash
rm -rf node_modules/
npm install
```

### Step 4: Regularly Monitor dependencies for vulnerabilities
From there, you will want to regularly monitor your dependencies for any known vulnerabilities that might pose a security risk.

```bash
npm audit
```

This command will check for and alert you to any known vulnerabilities associated with your dependencies.

### Step 5: Automate using npm scripts
To automate these steps, add the following scripts to your package.json.

```json
"scripts": {
  "shrinkwrap": "npm update && npm shrinkwrap",
  "clean-install": "rm -rf node_modules/ && npm install",
  "audit": "npm audit",
  "secure": "npm run shrinkwrap && npm run clean-install && npm run audit"
}
```

Run the command ```npm run secure``` to automatically update, shrinkwrap, clean install, and audit your node modules.