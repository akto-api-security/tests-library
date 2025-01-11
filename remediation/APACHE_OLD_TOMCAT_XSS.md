# Remediation for APACHE_OLD_TOMCAT_XSS

## Remediation Steps for Apache Old Version Tomcat Cross-Site Scripting

Apache's older version of Tomcat has potential Cross-Site Scripting (XSS) issues that can cause severe security risk. A potential attacker may use XSS attacks to insert malicious scripts to web pages viewed by other users. Here are the remediation steps:

### Step 1: Update to the Latest Tomcat Version
The best remediation for this issue is to always be on the latest version of Apache Tomcat, which has built-in prevention mechanisms for this kind of vulnerabilities.

Here is how to update:

```bash
cd /path/to/your/tomcat
wget http://www-eu.apache.org/dist/tomcat/tomcat-9/v9.0.56/bin/apache-tomcat-9.0.56.tar.gz
tar -xvf apache-tomcat-9.0.56.tar.gz
rm -rf apache-tomcat-9.0.56.tar.gz

# Backup the old version before moving the new one
mv apache-tomcat old-apache-tomcat-backup
mv apache-tomcat-9.0.56 apache-tomcat
```

### Step 2: Enable XSS Protection HTTP Header
Regardless of the version, it's also important to add some extra HTTP headers into each response for enhanced security. Add the below in your project's web.xml to enable HTTP security headers.

```xml
<filter>
    <filter-name>httpHeaderSecurity</filter-name>
    <filter-class>org.apache.catalina.filters.HttpHeaderSecurityFilter</filter-class>
    <async-supported>true</async-supported>
    <init-param>
        <param-name>xssProtectionEnabled</param-name>
        <param-value>true</param-value>
    </init-param>
</filter>
<filter-mapping>
    <filter-name>httpHeaderSecurity</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

### Step 3: Relaunch Tomcat and Audit Regularly
After applying these updates, relaunch your Tomcat server. 

```bash
cd /path/to/your/tomcat/bin
./shutdown.sh
./startup.sh
```
