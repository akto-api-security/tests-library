# Remediation for SHELLSHOCK_RCE

## Remediation Steps for ShellShock Remote Code Execution
ShellShock is a security vulnerability that allows Remote Code Execution (RCE) which can potentially allow an attacker to gain unauthorized access and control over a network.

### Step 1: Identify Affected Systems
You need to identify the systems running Bash. You can run the below command to check the bash version which is installed on your system.

```bash
bash --version
```

### Step 2: Test for Vulnerability
You can test if your version of Bash is vulnerable to ShellShock by running this code:

```bash
env 'x=() { :;}; echo vulnerable' 'BASH_FUNC_x()=() { :;}; echo vulnerable' bash -c "echo test"
```
If the system is vulnerable, the output will be:

```bash
vulnerable
test
```

### Step 3: Update Bash
On Debian based systems use apt-get, and on Red Hat based systems use yum. If an update is available, you should use package management tools to update the installed versions.

#### On Debian based systems:
```bash
sudo apt-get update && sudo apt-get install --only-upgrade bash
```

#### On Red Hat based systems:
```bash
sudo yum -y update bash
```

### Step 4: Verify the Update
After updating bash, run the vulnerability test command from Step 2 to ensure that the vulnerability has been corrected.

In case a new version of Bash is not available or the system continues to be vulnerable after the update, you should consult with your operating system vendor for a patch or consider alternatives like using a different shell.

### Step 5: Regular Auditing
Regularly audit your systems for any known vulnerabilities and always keep your systems updated.

### Step 6: Incident Response
In case your system was compromised due to ShellShock, consider your incident response protocol to ensure system security.