# Remediation for SERVER_VERSION_EXPOSED_VIA_RESPONSE_HEADER

## Remediation Steps for Server Version Exposure Via Response Headers

Exposing server version via response headers can be a security issue. An attacker who knows your server's version can exploit any known vulnerabilities of that specific version. 

### Step 1: Disable Server Version in Apache
If you are using an Apache server, then you can hide your Apache version by modifying the httpd.conf file.

```bash
sudo vi /etc/httpd/conf/httpd.conf
```

Then add these lines at the end of your `httpd.conf` file

```bash
ServerTokens Prod
ServerSignature Off
```

Don't forget to restart Apache

```bash
sudo service httpd restart
```

### Step 2: Disable Server Version in Nginx
If you are using an Nginx server, then you can hide your Nginx version by modifying the nginx.conf file.

```bash
sudo vi /etc/nginx/nginx.conf
```

Then add this line inside http{ } block in your `nginx.conf`

```bash
server_tokens off;
```

Restart Nginx to apply the changes

```bash
sudo service nginx restart
```

### Step 3: Regular Audit and Update
Keep your server version up to date and conduct regular audits to find and fix potential vulnerabilities. 

Note: Even though the version number is hidden, there are ways an attacker might still detect service versions. They might exploit default characteristics of specific versions and sometimes server software might leak version information through other means. Therefore, hiding version numbers should be one component of a multi-layered security approach. The most important protective measure is to keep server software updated.