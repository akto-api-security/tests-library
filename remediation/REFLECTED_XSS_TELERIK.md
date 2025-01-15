# Remediation for REFLECTED_XSS_TELERIK

## Remediation Steps for Reflected XSS Telerik Reporting Module
Reflected XSS (Cross-Site Scripting) vulnerabilities allow an attacker to inject their own script into web pages viewed by other users. The Telerik Reporting Module can be particularly vulnerable to this type of attack, but there are steps that can be taken to mitigate this.

### Step 1:Enable Content Security Policy (CSP)
Enabling content security policies can help prevent XSS attacks. Implement a CSP header that only allows scripts from trusted sources.
```csharp
public class Startup
{
    public void Configure(IApplicationBuilder app)
    {
        app.UseCsp(options => options
        .DefaultSources(s => s.Self())
        .ScriptSources(s => s.Self().CustomSources("trustedsource.com"))
        .StyleSources(s => s.Self().UnsafeInline())
        .ImageSources(s => s.Self())
        .FontSources(s => s.Self())
        );
    }
}
```
### Step 2: StringBuilder for User Inputs
User inputs are a common source of vulnerabilities. Use a StringBuilder to build your HTML and protect against script injection.
```csharp
StringBuilder sb = new StringBuilder();
string userInput = GetFormInput(); //example
sb.Append(HttpUtility.HtmlEncode(userInput));
```
### Step 3: Use AntiXSS Library
The AntiXSS Library from Microsoft is one useful tool to prevent XSS attacks. It contextually encodes output and prevents scripts from executing.
```csharp
string input = "<img src=1 onerror='alert(1)'>"; //example
string safe = Microsoft.Security.Application.Encoder.HtmlEncode(input);
```