# Remediation for CONFIGURATION_LISTING

## Remediation Steps for Sensitive Configuration Files Listing
Sensitive configuration files listing is a pressing issue where confidential information and secrets in configuration files are publicly visible. It allows potential attackers to gain knowledge about the system, increasing cybersecurity risks.

### Step 1: Hide Configuration Files
Hide your configuration files from public access. Below is an example of how to do this using .htaccess in Apache.

```bash
<Files "config.php">
   Order allow,deny
   Deny from all
</Files>
```

This prohibits direct access to the `config.php` file by clients.

### Step 2: Use .env Files
Store sensitive information like API keys, database passwords, etc. in .env files. And don't forget to add `.env` to your `.gitignore` file. Below is an example in Python:

```bash
DB_PASSWORD=<your_database_password>
```

You can access this in your Python code using:

```python
import os
password = os.getenv("DB_PASSWORD")
```

### Step 3: Encryption
Encrypt sensitive data in your configuration files. Here is an example in Python using Fernet:

```python
from cryptography.fernet import Fernet
# Put this somewhere safe! 
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
plain_text = cipher_suite.decrypt(cipher_text)
```

### Step 4: File Permissions
Ensure the correct file permissions are set for your configuration files. They should be writable only by the user, and possibly readable by the group if the application requires it. No other users should have any access.

```bash
chmod 600 filename
```