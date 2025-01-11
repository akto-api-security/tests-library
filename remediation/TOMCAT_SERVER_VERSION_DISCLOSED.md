# Remediation for TOMCAT_SERVER_VERSION_DISCLOSED

## Remediation Steps for Tomcat Server Version Disclosure
Tomcat Server's version disclosure can pose a security risk as it can provide a hacker with helpful information that may assist them in exploiting a known vulnerability in the server version that is in use.

### Step 1: Setting the serverInfo Property
One can customize or hide the server version by setting the `serverInfo` property of the `org.apache.catalina.util.ServerInfoFactory` system property to a custom value in the `catalina.properties` file.

```bash
org.apache.catalina.util.ServerInfoFactory.serverInfo=My Custom Server
```
You can also leave the values blank if you want.

### Step 2: Editing the 'Server' HTTP Response Header
In order to modify the `Server` HTTP response header, you will need to add a `header` element to the `http` connector in the `server.xml` file.

```xml
<Connector port="8080" protocol="HTTP/1.1"
         connectionTimeout="20000"
         redirectPort="8443" 
       server="My Custom Server">
```
You can also leave the server attribute blank if you want to fully hide the version details.

### Step 3: Restart the Tomcat Server
After the above changes are made, restart your Tomcat server to apply the changes.

```bash
sudo service tomcat restart
```