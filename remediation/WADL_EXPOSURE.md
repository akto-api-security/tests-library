

## Remediation Steps for WADL File Exposure
WADL (Web Application Description Language) file exposure can potentially allow an attacker to have a detailed view of your web service methods and operations, which can lead to attacks exploiting these methods.

### Step 1: Disable WADL Auto Generation 
While WADL exposure can enable easier consumption of your APIs, the risk may outweigh the benefits. To address this, most servers allow disabling of auto-generation of the WADL.

For example, in a JAX-RS server, add the following lines to the configuration file:

```bash
<init-param>
<param-name>com.sun.jersey.config.feature.DisableWADL</param-name>
<param-value>true</param-value>
</init-param>
```

### Step 2: Use Firewall Rules to Block Access
Depending on your network layout, you could use firewall rules to prevent access to certain files. This might serve as a backup measure in the event that your WADL file gets generated due to a configuration error.

```bash
iptables -A INPUT -p tcp --dport 80 -m string --algo kmp --string 'GET /application.wadl' -j REJECT
```