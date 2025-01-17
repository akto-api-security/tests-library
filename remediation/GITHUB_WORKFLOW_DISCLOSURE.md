

## Remediation Steps for Github Workflow Disclosure

Github workflow disclosure poses a security risk as it can reveal sensitive information about the application deployment processes and environment set up to a potential attacker. This information can be used to plan and execute targeted attacks on your infrastructure.

### Step 1: Use Secrets for Sensitive Information
Sensitive information such as authentication credentials, tokens and keys should be stored as Github Secrets, not directly in the workflow file. They can be accessed in workflow files as environment variables.

```yml
  steps:
    - name: Access Secret
      run: echo "Token is ${{ secrets.TOKEN }}"
```

### Step 2: Restrict Permissions
By default, Github workflows run with read/write permissions for all repositories. Restrict these permissions to least privilege by defining them in the workflow.

```yml
permissions:
  issues: write
  contents: read
```

### Step 3: Limit Usage of Third Party Actions
Limit the usage of third party GitHub Actions as they may have access to the same secrets as your workflows and may inadvertently expose them.

```yml
uses: actions/checkout@v2
```