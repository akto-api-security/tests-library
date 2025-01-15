# Remediation for SFTP_CONFIG_EXPOSURE

## Remediation Steps for SFTP Config File Disclosure
SFTP config file disclosure can lead to serious security issues as unauthorized individuals may gain access to sensitive information. Here's how you can mitigate this issue.

### Step 1: Set Appropriate User Permissions
Ensure that the SFTP config file is only accessible by the root user.

```bash
sudo chown root /etc/ssh/sshd_config
sudo chmod 600 /etc/ssh/sshd_config
```
These commands change the owner of the config file to root and set permissions so that only the owner has read and write access.

### Step 2: Restrict User Access through SSH
Edit the `/etc/ssh/sshd_config` file and change the SSH settings to limit user access.

```bash
sudo nano /etc/ssh/sshd_config
```
In the config file, find and modify these lines:
```
# Prevent root login
PermitRootLogin no

# Allow only certain users
AllowUsers [username]

# Disallow password authentication
PasswordAuthentication no
```
Remember to replace `[username]` with the actual username of the account that should be allowed to connect.

### Step 3: Restart SSH Service
Finally, restart the SSH service to apply the changes.

```bash
sudo systemctl restart ssh
```
Making these changes will prevent the disclosure of SFTP config files to unauthorized individuals. Regular audit and update of settings are required for optimum security. 