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