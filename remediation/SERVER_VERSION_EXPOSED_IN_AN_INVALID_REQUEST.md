

## Remediation Steps for Server Version Exposure Via Response Header

Exposing server version details via response headers can become a serious security issue. Attackers can exploit known vulnerabilities specific to the server version if it's exposed in response headers. Here are the remediation steps.

### Step 1: Update the Server Configuration

For Apache server, using `.htaccess` file or update `httpd.conf`:

```bash
ServerTokens Prod
ServerSignature Off
```

For Nginx server, update the `nginx.conf`:

```bash
server_tokens off;
```

### Step 2: Restart the Server

For Apache:

```bash
sudo apachectl restart
```

For Nginx:

```bash
sudo service nginx restart
```

### Step 3: Verify the Changes

You can do this by sending a request to your server and checking the headers in the server's response. Here is a sample command:

```bash
curl -I http(s)://domain-name-or-ip
```