# Remediation for SONARQUBE_PUBLIC_PROJECTS

## Remediation Steps for Sonarqube Public Projects Exposure
Exposing Sonarqube public projects can lead to potential security issues. It can reveal sensitive data or insider information about the project, and attackers may exploit vulnerabilities in the code to gain unauthorized access or induce security breaches.

### Step 1: Change project visibility to private
To change the visibility of a project to private. Login to your Sonarqube instance as an admin user, navigate to the 'Projects Management' page. Then, next to the project name, change the project's visibility from 'Public' to 'Private'.

### Step 2: Restrict access rights
Ensure that only authorized users are granted access to the project. This can be done in the project settings under 'Permissions'. 

```bash
# Example to revoke 'User' role for 'MyProject'
curl -u admin:admin -X POST 'http://localhost:9000/api/permissions/remove_user?login=myuser&permission=user&projectKey=MyProject'
# Example to add 'Admin' role for 'myuser' on 'MyProject'
curl -u admin:admin -X POST 'http://localhost:9000/api/permissions/add_user_to_template?login=myuser&permission=admin&templateName=MyTemplate'
```

### Step 3: Enable Force User Authentication
In the global settings ('Administration' > 'Configuration' > 'Security'), enable the 'Force user authentication' option. This will force all users to authenticate and prevent access to SonarQube data to anonymous users.

### Step 4: Regularly update Sonarqube and plugins
Keep Sonarqube and all its plugins updated to the latest versions to ensure all known vulnerabilities have been patched.

### Step 5: Limit features to trusted users
Some Sonarqube features, such as the ability to execute arbitrary code and the ability to create and manage Quality Gates, should be limited to trusted users to avoid misuse. This can be done under 'Administration' > 'Authorization'.

### Step 6: Protect the database
Protect the database used by Sonarqube as specified by the database documentation. This includes measures like keeping the database updated and ensuring the database server is not publicly accessible. 

```bash
# Example on how to restrict access to MongoDB on Ubuntu
sudo ufw deny from any to any port 27017
```