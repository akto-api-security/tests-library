# Remediation for SOURCE_CODE_DISCLOSURE_USING_FILE_EXTENSIONS

## Remediation Steps for Source Code Disclosure Using File Extensions

Source Code Disclosure using file extensions is a considerable security issue. Neglecting it may lead to exposing important server-side code to attackers, providing them the opportunity to exploit any potential vulnerabilities in the software. Addressing this issue involves configuring your web server not to disclose the source code. Here are the steps for mitigating this problem.

### Step 1: Configure Web Server to Disallow Serving File Types

Depending upon your web server, the method to prevent serving certain file types will vary. Here's an example for Apache and Nginx.

#### Apache
Edit .htaccess file (create one if it doesn't exist) and add the following:
```bash
<FilesMatch "\.(engine|inc|info|install|make|module|profile|test|po|sh|.*sql|theme|tpl(\.php)?|xtmpl)$">
  Order allow,deny
</FilesMatch>

<Filesmatch "\.(yml|twig|tpl|png|html|ttf|css|go|pl|doc|pdf|xls|tar|zip|gz|rdf|txt|xml|xsl|sql|MDB|ACCDB|ppt|odt|ods|math)$">
  Order deny,allow
</FilesMatch>
```

#### Nginx
For Nginx, update the server configuration file:
```bash
location ~* \.(engine|inc|info|install|make|module|profile|test|po|sh|.*sql|theme|tpl(\.php)?|xtmpl)$|^/(\..*|Entries.*|Repository|Root|Tag|Template)$ {
    deny all;
}
```

### Step 2: Regular Audit and Update

It is best to review the server configuration and access logs to ensure the files with scripted extensions do not serve source code. 

To check the Apache configuration files, use configuration test (`configtest`) command:
```bash
apachectl configtest
```
Always remember to keep your server software, including Apache or Nginx, updated to the latest security patches. 

Please note that this solution only addresses a part of the problem of source code disclosure. Awareness among developers about the secure coding practices is equally important, and the code should always be written to avoid exposure in case of failures.