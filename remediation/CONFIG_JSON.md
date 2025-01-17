

## Remediation Steps for Config File Exposure

Config file exposure is a severe security issue. In many cases, config files can contain sensitive information like database username, password, API secrets, etc. If these files get exposed to unintended parties, it can lead to severe security vulnerabilities.

### Step 1: Protect Config Files
First and foremost, keep these files in a protected directory that is not accessible publicly. Depending upon the server you are using, you may use different methods to achieve this.

For example, If you are using Apache, you can use `.htaccess` to deny access to the directory containing config files.

```htaccess
<Directory "/path/to/config/directory">
    Deny from all
</Directory>
```
If you are using Nginx, you can do something similar in the server configuration.
```nginx
location /path/to/config/directory {
    deny  all;
}
```
### Step 2: Store Sensitive Information in Environment Variables
Instead of hardcoding sensitive information like database username, password, and secrets in the config file, you can use Environment Variables to store these pieces of information. 

Here is an example in Python:
```python
import os

db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
```
You can set these environment variables in your server or your .env file.

### Step 3: File Permissions
Ensure that sensitive config files have restricted permissions. Only the users and services that need access to these files should have read permission, and preferably nobody should have write permission. 

You can change file permissions using the `chmod` command in Linux:
```bash
chmod 600 path/to/config.file
```

