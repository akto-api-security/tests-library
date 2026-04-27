

## Remediation Steps for FTP Credentials Exposure
Exposure of FTP credentials, typically the username and password, constitutes a serious security vulnerability. If these credentials fall into the wrong hands, it can lead to unauthorized access to sensitive data and possible manipulation of that data. Here are the remediation steps:

### Step 1: Change FTP Account Password
As an initial step, always update the password for your FTP account(s). This can typically be done through your hosting provider's dashboard or control panel. Make sure to use a strong password that combines letters, numbers, and special characters. 

```bash
ftp> prompt
ftp> open {your_ftp_server_host_name_or_ip}
ftp> {FTP_USER}
ftp> {NEW_STRONG_PASSWORD}
```

### Step 2: Disable Anonymous FTP Logins

Disabling anonymous FTP logins will prevent anyone without a valid username/password from accessing your FTP server. This can usually be accomplished through the server's control panel or FTP server configuration.

```bash
# For servers using vsftpd, edit the vsftpd configuration file:
sudo vi /etc/vsftpd.conf
# change 'anonymous_enable=YES' to 'anonymous_enable=NO'
```

### Step 3: Enable SFTP or FTPS

When possible, use SFTP or FTPS which encrypt the transmission of data, including your credentials, instead of FTP which sends data in plain text. Most FTP clients and servers support these safer protocols. For SFTP, you can do:

```bash
# Connect to SFTP with your credentials
sftp username@hostname
```