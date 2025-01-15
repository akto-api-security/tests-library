# Remediation for SOURCE_CODE_DISCLOSURE_WEB_INF

## Remediation Steps for Source Code Disclosure via WEB-INF

The security issue of Source Code Disclosure via WEB-INF happens when the web server is not correctly configured to restrict access to the WEB-INF directory, enabling an attacker to view the web app's source code, configurations, and other sensitive data.

### Step 1: Configure Your Web Server
First, you need to configure your web server to prevent access to WEB-INF. Here's how you can do it in Apache HTTP server:

```bash
<Directory /path/to/your/WEB-INF/>
    Order deny,allow
    Deny from all
</Directory>
```

### Step 2: Secure your web.xml
You also need to ensure that your `web.xml` (usually located in WEB-INF directory) is secure. It should not contain any sensitive data and should be adequately configured. Here's a sample secure configuration in `web.xml`:

```xml
<web-app>
    <display-name>Sample Application</display-name>
    <servlet>
        <!-- servlet configurations -->
    </servlet>
    <servlet-mapping>
        <!-- servlet-mapping configurations -->
    </servlet-mapping>
    <!-- No sensitive data should be below -->
</web-app>
```