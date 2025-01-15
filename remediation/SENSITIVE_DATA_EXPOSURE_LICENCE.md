# Remediation for SENSITIVE_DATA_EXPOSURE_LICENCE

## Remediation Steps for Sensitive data exposure for LICENCE
Sensitive data exposure is a serious security issue. Sensitive data, such as software license information, can be unintentionally exposed and may lead to unauthorized access and licence violation.

### Step 1: Hide LICENSE file from Public Access
Remove the LICENSE file from the public directory. Use the following command:

```bash
mv LICENCE ~/private_directory/
```
Replace `~/private_directory/` with the path to a secure directory.

### Step 2: Exclude LICENSE File in .gitignore
To prevent the LICENSE file from being unintentionally committed and pushed to a public repository, you should add it to a `.gitignore` file. Append the following line to your `.gitignore` file:

```
LICENCE
```

The result should look something similar to this:

```bash
nano .gitignore

# existing ignored files
# ...
 
# Ignore the LICENSE file
LICENCE
```

### Step 3: Remove LICENSE file from Git History
You also need to ensure that the LICENSE file is removed from your git history. Use the following command:

```bash
git filter-branch --force --index-filter \
'git rm --cached --ignore-unmatch LICENCE' \
--prune-empty --tag-name-filter cat -- --all
```