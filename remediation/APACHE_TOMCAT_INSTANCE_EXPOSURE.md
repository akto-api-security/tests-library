# Remediation for APACHE_TOMCAT_INSTANCE_EXPOSURE

## Remediation Steps for Apache Tomcat Instance Exposure Detection

Apache Tomcat Instance Exposure Detection is a serious security issue. If Tomcat's status page is available to unauthorized users, this can leak sensitive information such as server configuration, installed applications, and potentially sensitive operating system information. Follow the steps below to remediate.

### Step 1: Modify Tomcat Configuration
Ensure that Tomcat is properly configured to restrict access to the status page. Modify the `web.xml` file in your Tomcat's `conf` directory.

```xml
<!-- Define a security constraint on this application -->
<security-constraint>
  <web-resource-collection>
    <web-resource-name>Status page</web-resource-name>
    <url-pattern>/status</url-pattern>
  </web-resource-collection>
  <auth-constraint>
    <role-name>manager-gui</role-name>
  </auth-constraint>
</security-constraint>
```

Please replace `/status` with the path to the page you want to secure and replace `manager-gui` with the role you want to restrict access to.

### Step 2: Disable/Remove Unnecessary Applications
Remove unnecessary applications that could potentially expose sensitive information. Applications to consider removing may include host-manager, manager, docs, and others depending upon your specific use case.

The following command can be used to disable/remove an application in Tomcat:

```bash
rm -rf $CATALINA_HOME/webapps/[application_name]
```

Replace `[application_name]` with the name of the application you want to remove.

### Step 3: Regular Audit and Update

Limited exposure to the newest threats requires keeping up-to-date with the latest security patches. 

```bash
$CATALINA_HOME/bin/shutdown.sh
$CATALINA_HOME/bin/startup.sh
```

Regularly restart your Tomcat instance and apply updates as needed. Ensure the version you are running still has support and has not reached its end-of-life. If it has, plan for an upgrade to a supported version.