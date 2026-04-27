

## Remediation Steps for Apache Yarn Resource Manager Exposure

Exposure of Apache Yarn Resource Manager could allow unauthorized access to sensitive information or cause a Denial of Service (DoS). Here are the remediation steps to handle the security issue:

### Step 1: Configure YARN to Run in Secure Mode
This will require Kerberos to be working on your cluster. Apache YARN can be configured to run in secure mode, which relies on Kerberos to authenticate all user-service and service-service interactions. 

```bash
sudo nano /etc/hadoop/conf/yarn-site.xml
```
Add the following properties:

```xml
<property>
  <name>yarn.resourcemanager.webapp.address</name>
  <value>${yourResourceManagerAddress}:8090</value>
</property>
<property>
  <name>yarn.resourcemanager.webapp.https.address</name>
  <value>${yourResourceManagerAddress}:8090</value>
</property>
<property>
  <name>yarn.acl.enable</name>
  <value>true</value>
</property>
<property>
  <name>yarn.admin.acl</name>
  <value>*</value>
</property>
```
And save the changes made to your `yarn-site.xml` file.

### Step 2: Restart YARN
After making the necessary configuration changes, restart YARN by restarting the relevant services.

```bash
sudo service hadoop-yarn-resourcemanager restart
sudo service hadoop-yarn-nodemanager restart
sudo service hadoop-mapreduce-historyserver restart
```

### Step 3: Inspect Log Files Regularly
Check the log files regularly to identify any unusual or suspicious activity. Log files are usually located in the `/var/log/hadoop-yarn` directory.

Don't forget to update your Apache and Kerberos regularly to fix any system vulnerabilities.