# Remediation for STRUTS_OGNL_CONSOLE_ENABLED

## Remediation Steps for Struts OGNL Console Enabled

Struts OGNL Console Enabled is a significant security vulnerability. If not properly secured, attackers could use the OGNL console to execute arbitrary code remotely on your systems, which would effectively compromise the security.

### Step 1: Identify the Vulnerability
You need to verify if your application is affected. You can do this by accessing the `/console.action` URL of your application. If you see a console, that means  Struts OGNL console is enabled and you need to take further steps to remediate.

### Step 2: Disable OGNL Console 
Disabling the Struts OGNL console is the most straightforward way to fix the vulnerability. Look for the `struts.devMode` setting in your `struts.xml` or `struts.properties` file and set it to `false`.

```xml
<constant name="struts.devMode" value="false" />
```
or 

```java
// in your struts.properties file
struts.devMode = false
```

### Step 3: Review Application Configuration and Update Struts Version
Review your application configuration and make sure there is no other exposed functionality that could be exploited. Moreover, update to the latest version of Struts if not done already. They had have fixed this issue in version 2.3.20 and onwards.

```bash
<dependency>
    <groupId>org.apache.struts</groupId>
    <artifactId>struts2-core</artifactId>
    <version>2.5.22</version> <!-- replace with the latest version -->
</dependency>
```