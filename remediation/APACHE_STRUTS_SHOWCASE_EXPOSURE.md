

## Remediation Steps for Apache Struts - ShowCase Application Exposure

Apache Struts ShowCase Application Exposure is a serious vulnerability that could allow an attacker to gain unauthorized access to application data. By exploiting this vulnerability, an attacker could manipulate the Struts configuration files to execute arbitrary code.

### Step 1: Identify & Update Affected Versions
```bash
# Verify the version of Struts
java -jar struts2-showcase.war --version

# If version < 2.3.35 or between 2.5.0 and 2.5.16, it might be vulnerable
# Update Struts to the latest version
wget 'https://downloads.apache.org/struts/latest/struts-2.5.26-all.zip'
unzip struts-2.5.26-all.zip -d /path/to/webapps/
```
Please replace `/path/to/webapps/` with the actual path where your web applications are stored.

### Step 2: Remove Showcase App
```bash
# By default, ShowCase App is included in Struts package. 
# The real problem is the 'Showcase' app that should not be deployed in the production environment.
# Remove the showcase app
rm -rf /path/to/webapps/struts2-showcase
```
Ensure you replace `/path/to/webapps/` with your actual web applications directory.

### Step 3: Secure Access to the Configuration Files
```bash
# Secure access to Struts configuration files. They should not be accessible to the external users.
chmod o-rwx /path/to/webapps/struts*/WEB-INF/classes/struts.xml
```
Replace `/path/to/webapps/` with your actual web applications directory.

### Step 4: Regular Updates and Security Audits
Ensure your Apache Struts is regularly updated and frequently undergoes security checks to avoid such vulnerabilities in the future. 

```bash
# Regularly update Struts to the latest versions to get security patches
java -jar struts2-showcase.war --update
```