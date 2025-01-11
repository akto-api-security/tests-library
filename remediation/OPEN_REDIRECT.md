# Remediation for OPEN_REDIRECT

## Remediation Steps for Open Redirect Vulnerability

Open redirect vulnerabilities present a significant security issue. Unvalidated redirects and forwards can be used to lure users to malicious websites that can collect personal information, launch phishing attacks, install malware, and more. 

### Step 1: Don't Include User Parameters in Destinations

First rule of thumb in preventing open redirect attacks is to avoid including user parameters in the destination URL.

```java
response.sendRedirect("/welcome");
```

### Step 2: Whitelist Known and Trusted URLS

If you can't get rid of user-supplied URLs, use a whitelist of approved URLs. 

```java
List<String> safeUrls = Arrays.asList("https://www.safeURL.com", "https://www.safeURL2.com");
String redirectUrl = request.getParameter("redirect");
if (!safeUrls.contains(redirectUrl)) {
    response.sendRedirect("/error");
} else {
    response.sendRedirect(redirectUrl);
}
```

### Step 3: Verify the Schema and Domain

Verifying that the schema (http, https) and domain (www.example.com) are on a known and safe list.

```java
URL url = new URL(redirectUrl);
if (!(url.getProtocol().equals("http") || url.getProtocol().equals("https"))
    ||!url.getHost().endsWith("safeURL.com")) {
    response.sendRedirect("/error");
} else {
    response.sendRedirect(redirectUrl);
}
```

