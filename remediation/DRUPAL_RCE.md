# Remediation for DRUPAL_RCE

## Remediation Steps for Drupal Remote Code Execution

The Drupal Remote Code Execution vulnerability is a serious security issue that can permit an attacker to execute malicious code on your Drupal site. This can happen when an attack vector occurs in parts of your Drupal code that don't sanitize user inputs properly.

### Step 1 - Update Drupal core

The first step to remediate the Drupal Remote Code Execution vulnerability is to ensure that your Drupal installation is updated to the latest stable version. This includes updating the core, modules, and themes.

```bash
cd /path/to/your/drupal/root
drush pm-update
```

In the command above, replace `/path/to/your/drupal/root` with your Drupal root directory. Running this command will automatically update your Drupal site to the latest stable version.

### Step 2 - Update modules and themes

**It's important** to also keep your Drupal modules and themes updated to the latest stable version to ensure that your Drupal site is secure from the Remote Code Execution vulnerability.

```bash
cd /path/to/your/drupal/root
drush up
```

### Step 3 - Review custom and third-party code

Custom and third-party code can also introduce the Drupal Remote Code Execution vulnerability if user inputs aren't properly sanitized. Regularly review the code of all custom and third-party modules and themes installed on your Drupal site.

### Step 4 - Enable secure configuration

Ensure that your Drupal site is configured to run securely by following the recommendations in Drupal's [security guide](https://www.drupal.org/security/secure-configuration).