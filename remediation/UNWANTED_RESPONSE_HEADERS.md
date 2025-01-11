# Remediation for UNWANTED_RESPONSE_HEADERS

## Remediation Steps for Unwanted Response Headers

Unwanted response headers can expose sensitive server information, making your application vulnerable to attacks.

### Step 1: Identify Unwanted Headers

```bash
curl -s -D - http://yourwebsite.com -o /dev/null
```
This command will simulate a HTTP GET request to your site, outputting all the response headers. They may include "Server", "X-Powered-By", "X-AspNet-Version", etc.

### Step 2: Remove Unwanted HTTP Headers

Example for Apache, in .htaccess or httpd.conf:

```apache
<IfModule mod_headers.c>
    Header unset Server
    Header unset X-Powered-By
    Header unset X-AspNet-Version
</IfModule>
```

Example for Nginx, in nginx.conf:

```nginx
server {
    ...
    server_tokens off;
    more_clear_headers Server;
    more_clear_headers X-Powered-By;
    more_clear_headers X-AspNet-Version;
    ...
}
```
You may need to install the HttpHeadersMore module in Nginx. If you're using Express.js, use the helmet library to help manage headers:

```js
const helmet = require('helmet');
app.use(helmet.hidePoweredBy());
```
### Step 3: Verify Your Changes

```bash
curl -s -D - http://yourwebsite.com -o /dev/null
```
Check the response headers again, the unwanted headers should be gone.

Always remember to restart your server after making configuration changes:
```bash
sudo service apache2 restart
# or
sudo systemctl restart nginx
```