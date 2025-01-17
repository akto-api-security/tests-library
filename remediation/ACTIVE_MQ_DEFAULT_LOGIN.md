

## Remediation Steps for ActiveMQ Default Login  
ActiveMQ default login is a security risk that offers attackers an easy route to unauthorized access and potential manipulation of data. By default, ActiveMQ uses the username 'admin' and the password 'admin', which is common knowledge and thus a vulnerability. 

### Step 1: Change Default Passwords  
Change the default password used by ActiveMQ to a secure password of your choosing. This process can be done by navigating to the `jetty-realm.properties` file in the ActiveMQ configuration directory .

```bash
vi /opt/activemq/conf/jetty-realm.properties
```
Replace 'admin' string with a secure password of your choosing. 

It should look like this: 
```bash
admin: yourSecurePassword, admin 
user: yourSecurePassword, user
```
Replace `yourSecurePassword` with a secure password of your choice.

### Step 2: Restart the ActiveMQ Service  
After making the password change, save your changes and restart the ActiveMQ service to apply these modifications. 

```bash
sudo systemctl restart activemq
```
