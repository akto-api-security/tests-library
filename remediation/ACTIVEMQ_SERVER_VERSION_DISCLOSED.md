# Remediation for ACTIVEMQ_SERVER_VERSION_DISCLOSED

## Remediation Steps for ActiveMQ Server Version Disclosure
ActiveMQ Server version disclosure can lead to potential security threats. An attacker may exploit known vulnerabilities for specific ActiveMQ versions if the version is publicly disclosed. Here's how you can mitigate this issue:

### Step 1: Configure jetty.xml
Locate the jetty.xml file in the ActiveMQ configuration directory (%ACTIVEMQ_HOME%/conf/) and add following into the jetty.xml file under the `<Call name="addConnector">` section:
```xml
  <Set name="sendServerVersion">false</Set>
```
Full example of the "<Call name="addConnector">" section:
```xml
<Call name="addConnector">
  <Arg>
      <New class="org.eclipse.jetty.server.nio.SelectChannelConnector">
        <Set name="host"><SystemProperty name="jetty.host" /></Set>
        <Set name="port"><SystemProperty name="jetty.port" default="8161"/></Set>
        <Set name="maxIdleTime">300000</Set>
        <Set name="Acceptors">2</Set>
        <Set name="statsOn">false</Set>
        <Set name="confidentialPort">8443</Set>
        <Set name="lowResourcesConnections">20000</Set>
        <Set name="lowResourcesMaxIdleTime">5000</Set>
        <Set name="sendServerVersion">false</Set>
      </New>
  </Arg>
</Call>
```

### Step 2: Restart the ActiveMQ Server
```bash
sudo service activemq stop
sudo service activemq start
```
Please note that these steps only reduce the exposure of information, it's essential to ensure you patch or upgrade your ActiveMQ server regularly to prevent exploitation of known vulnerabilities. 

Also, ensure to adequately secure your ActiveMQ server with techniques like strong authentication, network isolation, etc., to mitigate other potential security risks.