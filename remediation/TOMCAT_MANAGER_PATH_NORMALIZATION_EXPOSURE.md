# Remediation for TOMCAT_MANAGER_PATH_NORMALIZATION_EXPOSURE

## Remediation Steps for Apache Tomcat Manager Path Normalization Panel Exposure

Apache Tomcat Manager Path Normalization Panel Exposure is a severe security issue that can allow attackers unauthorized access to sensitive content. It is crucial to rectify this vulnerability promptly.

### Step 1: Update Apache Tomcat Version 
The vulnerability may be due to using an out-of-date version of Apache Tomcat. Update to the latest version.

```bash
sudo apt-get update
sudo apt-get install tomcat9
```

### Step 2: Restrict Access To Certain IP Addresses
Configure Tomcat to only allow trusted IP addresses access to the administrative features.

Edit the `context.xml` file in the `META-INF` directory of the Tomcat Manager application.

```xml
<Context antiResourceLocking="false" privileged="true" >
  <Valve className="org.apache.catalina.valves.RemoteAddrValve"
         allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" />
</Context>
```
In the example above, only local host has access.

### Step 3: Configure User Roles and Permissions 
Edit the `tomcat-users.xml` file to add user roles and permissions.

```xml
<tomcat-users>
  <role rolename="manager-gui"/>
  <role rolename="manager-script"/>
  <role rolename="manager-jmx"/>
  <role rolename="manager-status"/>

  <user username="admin" password="password" roles="manager-gui,manager-script,manager-jmx,manager-status"/>
  <user username="tomcat" password="password" roles="manager-gui"/>
</tomcat-users>
```
Apply strong, complex credentials. The example shown is for illustrative purposes only.

### Step 4: Regular Software and Security Updates
Perform frequent checks for software updates, patches, and security advisories. Apply these updates promptly to keep your Apache Tomcat install secure against known vulnerabilities.

```bash
sudo apt-get update
sudo apt-get upgrade
```
Always test updates in a non-production environment first to avoid unexpected disruptions.

