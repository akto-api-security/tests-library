# Remediation for TRACE_METHOD_TEST

## Remediation Steps for TRACE Method Vulnerability

The TRACE method returns the entire HTTP request, including any sensitive data such as authentication tokens, back to the client. It is essentially providing hackers an open window into your application's communications and should therefore be disabled.

### Step 1: Identify the Configuration File

Depending on your server setup, identify the necessary configuration file. 

#### Apache
For Apache, this will typically be found in either '/etc/httpd/conf/httpd.conf' or '/etc/apache2/apache2.conf'.

#### IIS
For IIS, the server configuration is kept within the 'Web.config' file.

### Step 2: Disable TRACE Method

#### Apache
For Apache servers, insert or update the following line in your configuration file:

```bash
TraceEnable off
```

After updating the configuration file, restart the Apache server:
```bash
service apache2 restart
```

#### IIS
For IIS servers, add or modify the `<customHeaders>` section under `<httpProtocol>` in the 'Web.config' file if it exists, otherwise create one:

```xml
<system.webServer>
  <httpProtocol>
    <customHeaders>
      <remove name="X-POWERED-BY"/>
      <add name="X-AspNet-Version" value=" " />
    </customHeaders>
  </httpProtocol>
<system.webServer>
```

Restart IIS after modifying the 'Web.config' file:
```bash
iisreset
```
### Step 3: Confirm TRACE Method is Disabled

Verify that the TRACE method is disabled by sending an HTTP TRACE request to the server.

#### Apache
For Apache, use `curl` or a similar tool to send the TRACE request:
```bash
curl -X TRACE http://yourserver.com
```

#### IIS
In IIS, use a tool like Postman to manually send an HTTP TRACE request to the server.

If the server is not vulnerable, it will return a '405 Method not allowed' response.

***Note:*** *The said instructions assumes Linux as the operating system for Apache and Windows for IIS.*