

## Remediation Steps for Sensitive Data Exposure of HashiCorp Access Token

Sensitive data exposure, such as a HashiCorp access token, can lead to unauthorized access. The following steps can limit the exposure of these sensitive credentials.

### Step 1: Revoke the compromised HashiCorp access token
```bash
vault token revoke <<token>>
```

In the above script, replace `<<token>>` with the compromised access token to revoke it.

### Step 2: Rotate/Update the Access Token
Generate a new HashiCorp access token using the below command:

```bash
vault token create -policy=my-policy -period=4320h
```

This will create a new token with the associated policy and period.

### Step 3: Use Environment Variables to Store Sensitive Data
Never hard code secrets in your source code. Instead, use environment variables:

```bash
export VAULT_TOKEN=new_token
```

### Step 4: Use HashiCorp Vault Secrets Engine
The Vault secrets engine generates dynamic credentials on demand:

```bash
vault secrets enable -path=secret kv
vault kv put secret/my-secret my-value=s3cr3t
```


### Step 5: Avoid track secrets in version control systems
.gitignore file helps prevent tracking secrets:

```bash
echo ".env" >> .gitignore
```

In case the git history contains the sensitive information, you may need to rewrite the entire git history to completely remove that. Tools like 'BFG Repo-Cleaner' or 'git-filter-repo' can be used.


Note: Always consider the principle of least privilege while assigning access token privileges. Use HashiCorp Vault's policies to manage access and permissions effectively.