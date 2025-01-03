# Remediation for APACHE_TOMCAT_MANAGER_DEFAULT_LOGIN

## Remediation Steps for Apache Tomcat Manager Default Login Vulnerability 

The Apache Tomcat Manager application provides a clear and handy interface over a tomcat server to help system administrators manage applications deployed on their servers. However, given the potential abuse of its functions, it's crucial to ensure its login security.

Here are the steps to take to fix the Apache Tomcat Manager Default Login vulnerability issue.

### Step 1: Remove default user
The first step is to remove the default Tomcat user if it exists. The default user may be Tomcat or admin. This is done from the Tomcat-users.xml file. 

```xml
<!-- User "tomcat" with "manager-gui" removed -->
<tomcat-users>
</tomcat-users>
```

### Step 2: Create a custom user and password
Create a new user and strong password for Manager GUI applications. Add this to your Tomcat-users.xml file.

```xml
<!-- New user created -->
<tomcat-users>
   <role rolename="manager-gui"/>
   <user username="newuser" password="newpassword" roles="manager-gui"/>
</tomcat-users>
```
Replace `newuser` and `newpassword` with your preferred strong username and password.

### Step 3: Set the user permissions
Ensure you set strict permissions on the above file, allowing only the root user to edit.

```bash
sudo chown root:root /etc/tomcat7/tomcat-users.xml
sudo chmod 600 /etc/tomcat7/tomcat-users.xml
```

### Step 4: Restart Tomcat
Lastly, restart the Tomcat server for the changes to take effect.

```bash
sudo service tomcat7 restart
```

Please ensure to update your credentials regularly, monitor your log files, and perform regular security audits to ensure system integrity.