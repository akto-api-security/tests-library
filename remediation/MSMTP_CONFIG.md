# Remediation for MSMTP_CONFIG

## Remediation Steps for Msmtp Config Exposure

Msmtp Config Exposure implies that the major configurations of msmtp mail server are exposed, forming a security threat. Msmtp is an SMTP client that can be used to send mails from Mutt and probably other MUAs (Mail User Agents).

### Step 1: Modify Configuration File Permissions
Ensure the msmtp configuration file permissions are set correctly. So that only the owner of the file can read and write to the configuration file. This can be achieved with the chmod command.

```bash
chmod 600 ~/.msmtprc
```

### Step 2: Use a separate password file
Instead of storing the password directly in the main configuration file. Create a separate password file, permission it appropriately and reference the file in the main configuration.

Create a new file to store the password:
```bash
echo "password" > ~/.msmtp-password
chmod 600 ~/.msmtp-password
```
Then, reference the password file in the msmtp configuration file using the `passwordeval` directive. 

```
defaults
tls on
tls_starttls on
tls_trust_file /etc/ssl/certs/ca-certificates.crt

account default
host smtp.mail.com
port 587
auth on
user your-email@mail.com
passwordeval "cat ~/.msmtp-password"
from your-email@mail.com
logfile ~/.msmtp.log
```

### Step 3: Regularly Rotate Passwords
Make sure to regularly rotate passwords for your mail account to enhance security.