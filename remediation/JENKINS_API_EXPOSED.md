

## Remediation Steps for Jenkins API Exposure
Exposing Jenkins API is a serious security issue. Without properly securing Jenkins APIs, attackers may gain unauthorized access to project's data and environment. Follow the steps below to fix the vulnerability:

### Step 1: Disable Jenkins Remote Access API
Ensure that the Jenkins remote access APIs are disabled. This ensures that a potential attacker cannot interface with Jenkins instance programmatically.

```bash
JENKINS_URL= Insert Jenkins URL here
wget ${JENKINS_URL}'/jnlpJars/jenkins-cli.jar'
java -jar jenkins-cli.jar -s ${JENKINS_URL} groovy = < "println Jenkins.instance.getDescriptor('jenkins.security.apitoken.ApiTokenPropertyConfiguration').getCreationOfLegacyTokenEnabled()"
java -jar jenkins-cli.jar -s ${JENKINS_URL} groovy = < "Jenkins.instance.getDescriptor('jenkins.security.apitoken.ApiTokenPropertyConfiguration').setCreationOfLegacyTokenEnabled(false)"
```

### Step 2: Use API Tokens for Authentication
Opt for API tokens rather than using username-password for authentication for API. The users' page provides a way to generate API token.

### Step 3: Enable Access Control
Enable access control, to limit the accessible functionalities based on user roles.

```bash
java -jar jenkins-cli.jar -s ${JENKINS_URL} groovy = < 'println Jenkins.instance.getAuthorizationStrategy().allowsSignup()'
java -jar jenkins-cli.jar -s ${JENKINS_URL} groovy = < 'Jenkins.instance.setSecurityRealm(hudson.security.HudsonPrivateSecurityRealm(false))'
```