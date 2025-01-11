# Remediation for HTTP_VERB_TUNNELING

## Remediation Steps for Bypassing Access Controls Using HTTP Verb Tunneling
This security issue revolves around an attacker exploiting HTTP methods such as PUT, DELETE, or CONNECT to bypass firewall and proxy restrictions. These are usually implemented to allow specific HTTP methods for their services. In many scenarios, only safe HTTP methods like GET and POST are allowed but not others like DELETE or PUT.

This is how one might bypass these controls using HTTP verb tunneling, where the attacker uses an allowed method such as POST to tunnel other HTTP methods through the application to the server.

Here's how you can fix this vulnerability.

### Step 1: Validate HTTP Methods 
Every application should strictly validate allowed HTTP methods. For example, in a Node.js Express app, you might do the following:

```javascript
app.all('*', function(request, response, next) {
  if (['GET','POST'].indexOf(request.method) >= 0) {
    // permitted
    next();
  } else {
    // unpermitted
    response.status(405).send({status: 'error', message: 'Method not allowed'});
  }
});
```
Here, only GET and POST methods are allowed, any other request will return a "405 Method Not Allowed" status code.

### Step 2: Disable Allow Any HTTP Method in IIS
IIS (Internet Information Services) is a set of Internet-based services for servers using Microsoft Windows. In IIS 7 and above, you can use:
```xml
<system.webServer>
    <security>
        <requestFiltering>
	   <verbs>
               <!-- remove any verb not defined -->
               <remove verb="*" />
              <add verb="GET" allowed="true" />
              <add verb="POST" allowed="true" />
            </verbs>
        </requestFiltering>
    </security>
</system.webServer>
```

### Step 3: Disable HTTP Tunneling in IIS
Disable HTTP tunneling by turning off the `Allow HTTP Verb Tunneling` settings option in IIS.

```xml
<system.webServer>
    <handlers>
        <remove name="ExtensionlessUrlHandler-Integrated-4.0" />
        <add name="ExtensionlessUrlHandler-Integrated-4.0" path="*." verb="*" type="System.Web.Handlers.TransferRequestHandler" preCondition="integratedMode,runtimeVersionv4.0" />
    </handlers>
</system.webServer>
```

These steps should provide robust protection against bypassing access controls using HTTP verb tunneling. Regularly audit and update your system to keep the security controls effective. 