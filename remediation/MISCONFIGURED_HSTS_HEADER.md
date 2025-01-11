# Remediation for MISCONFIGURED_HSTS_HEADER

## Remediation Steps for Misconfigured HTTP Strict-Transport-Security Header
The HTTP Strict-Transport-Security (HSTS) header ensures that all communication from a user's browser to the website is done over a secure HTTPS connection.

If this header is misconfigured, it might lead to man-in-the-middle attacks as information could potentially be transferred over a non-secured connection.

The following are the remediation steps for misconfigured HSTS headers:

### Step 1: Configure HSTS Header
Enable HSTS by adding the strict transport security header to your server. If the server is Apache, use the below code:

```bash
<IfModule mod_headers.c>
    Header set Strict-Transport-Security "max-age=31536000; includeSubDomains"
</IfModule>
```

For Nginx, add the following to your configuration:

```bash
add_header Strict-Transport-Security 'max-age=31536000; includeSubDomains' always;
```

### Step 2: Check HSTS Header
After setting the header, use an online tool such as SecurityHeaders.com to check if it was properly set up.