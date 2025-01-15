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