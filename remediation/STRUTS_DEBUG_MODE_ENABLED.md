# Remediation for STRUTS_DEBUG_MODE_ENABLED

## Remediation Steps for Struts Debug Mode Enabled
Struts Debug Mode Enabled is a serious security vulnerability. This mode, when enabled, may disclose sensitive information that could aid an attacker in exploiting the application. 

### Step 1: Identify Debug Settings
Search your application for any Struts configuration files (struts.xml, struts-config.xml, etc.) and find where debug mode has been enabled.

### Step 2: Disable Debug Mode in Struts
Modify the configuration to disable debug mode. In the Struts xml configuration file, the 'debug' attribute should be set to 'false'. 

```xml
<constant name="struts.devMode" value="false" />
```
### Step 3: Struts Rebuild and Restart
After modifying the configuration, rebuild your application and restart the server for the changes to take effect.

### Step 4: Regular Audits
Perform regular audits of your configuration files to ensure that debug mode remains disabled in Struts. 

```bash
grep -i "struts.devMode" /path/to/webapp/WEB-INF/classes/struts.xml
``` 

The above command should return 'false' as the value of 'struts.devMode'. If it is 'true', follow the steps above to disable it. 

By ensuring that 'struts.devMode' is set to 'false', you can prevent potential information leaks that could be used to compromise your application.