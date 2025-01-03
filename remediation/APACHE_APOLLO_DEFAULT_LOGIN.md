# Remediation for APACHE_APOLLO_DEFAULT_LOGIN

## Remediation Steps for Apache Apollo Default Login Vulnerability

The Apache Apollo Default Login Vulnerability is a major security risk. By exploiting this, attackers may gain unauthorized access to Apache Apollo Message-Queue system, therefore, compromising the integrity and confidentiality of your messages.

### Step 1: Change Default Apollo Administrator Credentials

The default administrator username and password in Apollo are both 'admin'. This must be changed to prevent unauthorized access.

Apache Apollo doesn't provide a command or console interface to change the default credentials. You must manually edit the `apollo.xml` config file to change the username and password.

Below is an example of how to do it using `nano` text editor in Linux.

Open the `apollo.xml` file

```bash
sudo nano /etc/apollo/apollo.xml
```

Locate this section in the file:

```xml
<authentication_user id="admin" password="password" roles="admin,operator"/>
```

Update 'admin' in the `id` attribute to your desired username and 'password' in the `password` attribute to your desired password. An example change could be:

```xml
<authentication_user id="new_admin" password="your_secure_password" roles="admin,operator"/>
```
After you've made your changes, save and close the file.

### Step 2: Restart Apache Apollo

Restart the Apache Apollo service to apply the configuration changes

```bash
sudo service apollo restart
```

### Step 3: Regular Audit and Update

Make sure to regularly audit and update your Apollo configurations and installations. Regular security practices like using strong passwords and changing them often apply as well.

No source code is needed to fix this vulnerability. The aforementioned steps should be enough to mitigate the Apache Apollo Default Login Vulnerability.