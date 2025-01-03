# Remediation for APACHE_CRLF

## Remediation Steps for Apache mod_userdir CRLF Injection
Apache mod_userdir CRLF injection is a serious security issue. To handle this, Apache HTTP server should be upgraded to the version that fixes this vulnerability immediately. Alternatively, use of mod_userdir can be disabled.

### Step 1: Upgrade Apache HTTP server

The first and foremost step is to upgrade your Apache HTTP server to the latest version which has fixed the CRLF injection issue. 

```bash
sudo apt-get update
sudo apt-get install apache2
```
Replace above commands as per your package manager (In case of machine other than Ubuntu)

### Step 2: Disable mod_userdir

If you don't have option to upgrade Apache, you can disable the mod_userdir, removing the vulnerability.

```bash
sudo a2dismod userdir
sudo service apache2 restart
```

### Step 3: Adjust Configuration files 

If you wish to use mod_userdir, you can adjust the server directives to prevent CRLF injection. The following configuration settings could block this type of attack:

```apache
<IfModule mod_headers.c>
    Header set Set-Cookie: "key=value; HTTPOnly"
</IfModule>
```

Replace this line in the existing apache configuration file.

### Step 4:  Regular Audit and Update

In order to keep your system secure, it's recommended to constantly monitor and update your software.

```bash
sudo apt-get update && sudo apt-get upgrade
```

Remember: replace the above command specific to your package manager.

### Source

1. [Apache HTTP Server 2.4 vulnerabilities](https://httpd.apache.org/security/vulnerabilities_24.html)
2. [Apache mod_userdir documentation](https://httpd.apache.org/docs/2.4/mod/mod_userdir.html)