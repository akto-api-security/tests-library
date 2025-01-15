# Remediation for JETTY_CONFIG_EXPOSED

## Remediation Steps for Jetty Config Exposure
Jetty Config Exposure represents a critical security issue. Config files may contain sensitive data that, if exposed, can lead to unauthorized access or information leakage that may further compromise the application's environment.

### Step 1: Identifying Exposed Config Files

Identify all the configuration files in all the servers where Jetty runs. An exposed configuration file would generally look like this:

```bash
-rwxrw-r-- 1 jetty jetty  927 Feb 14 15:54 jetty.conf
```

### Step 2: Restrict Access to Config Files

Change Jetty's config file permissions to restrict other users from accessing the file:

```bash
sudo chmod 640 /path/to/your/jetty.conf
```

This will make the file readable and writable to the owner and readable to users in the owner's group. All others will not have any read, write, or execute permissions.

### Step 3: Configure Webserver to Deny Access to Config Files

Configure your webserver to deny HTTP requests for Jetty's config files. Here is an example of how to set it up on Apache:

```apache
<Directory "/path/to/your/jetty/config/files">
   Order Allow,Deny
   Deny from all
</Directory>
```


### Step 4: Verify the Changes

Test the changes you made and verify that the configuration file is no longer accessible:

```bash
curl -I http://localhost/path/to/your/jetty.conf
```

The response should be `403 Forbidden` which means the server understood the request, but it refuses to authorize it.