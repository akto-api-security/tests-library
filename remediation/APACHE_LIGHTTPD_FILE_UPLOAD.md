# Remediation for APACHE_LIGHTTPD_FILE_UPLOAD

## Remediation Steps for Apache lighttpd Arbitrary File Upload

The Apache event-driven web server, Lighttpd, may allow an attacker to upload arbitrary files in the server. This can lead to serious security vulnerabilities. Follow the remediation steps below to address this vulnerability.

### Step 1: Update lighttpd
Update your instance of lighttpd to the latest version as it may have fixed vulnerabilities in the previous versions. 
```bash
sudo apt-get update
sudo apt-get upgrade lighttpd
```

### Step 2: Restrict file upload permissions
Configure your server to restrict file upload permissions to only specific directories and restrict execution permissions. You can use the configuration file to limit the file upload size to minimize the impact of a potential attack too.

```lighttpd
server.upload-dirs = ( "/dir/to/storage" )
server.max-request-size = 2048
```

### Step 3: Disable dangerous modules
Disable any modules that could be potentially harmful or provide functionality that you're not using on your server, like mod_cgi, mod_fastcgi, mod_scgi.
```lighttpd
server.modules = (
    "mod_access",
    "mod_alias",
    "mod_accesslog" 
)    # Removed potentially harmful modules
```

### Step 4: Use mod_secdownload to protect download URI
This module provides a way to secure downloads by preventing hotlinking and offering expiring URIs.
```lighttpd
secdownload.secret        = "secretstring" 
secdownload.document-root = "/var/www/files" 
secdownload.uri-prefix    = "/download/" 
secdownload.timeout       = 60
```