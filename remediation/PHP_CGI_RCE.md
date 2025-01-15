# Remediation for PHP_CGI_RCE

## Remediation Steps for PHP CGI Remote Code Execution
PHP CGI remote code execution is a critical security risk where an attacker could execute arbitrary code on the server. This typically involves exploiting the PHP-CGI application by sending a manipulated query string to it. 

The remediation steps to this vulnerability are:

### Step 1: Check if you are vulnerable 
Check your PHP version, the versions 5.3.12 and 5.4.2 are known to be vulnerable. Use the following command to check your PHP version:
```bash
php -v
```
### Step 2: Update your PHP version
If you are running a vulnerable PHP version, update it to the latest stable version. It's always good to be on a secure and maintained version of PHP.

```bash
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:ondrej/php
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y php7.4
```
Then check your PHP version again to make sure the update has been successful.
```bash
php -v
```
### Step 3: Disallow access to the .php files
Disable the interpretation of .php files on Apache in `.htaccess`:

```apache
<FilesMatch \.php$>
    SetHandler None
</FilesMatch>
```
This strictly means no PHP files will be executed on the server, which is impractical for many. A more realistic solution is to move the PHP-CGI binary out of PATH:

```bash
mv /usr/bin/php-cgi /usr/bin/php-cgi.bak
```
### Step 4: Use PHP-FPM instead of PHP-CGI
PHP-FPM (FastCGI Process Manager) is an alternative PHP FastCGI implementation with some additional features useful for sites of any size, especially busier sites. Check if PHP-FPM is installed:

```bash
php-fpm -v
```
If not, install it:

```bash
sudo apt-get install php7.4-fpm
```
Then, configure your web server to use PHP-FPM. For example, in Nginx, modify the PHP processing section of your site's configuration file (usually located in `/etc/nginx/sites-available/`) to look like the following:

```nginx
location ~ \.php$ {
    include snippets/fastcgi-php.conf;
    fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
}
```
After updating your server's configuration, make sure to restart your web server to apply changes.

For Nginx:

```bash
sudo service nginx restart
```
Please adapt steps as necessary for your specific environment. Always ensure to backup your environment before making changes.