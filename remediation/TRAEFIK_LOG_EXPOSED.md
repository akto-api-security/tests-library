# Remediation for TRAEFIK_LOG_EXPOSED

## Remediation Steps for Traefik Log Exposure
Traefik Log Exposure is a critical security issue. If Traefik logs are not properly protected, sensitive information may be compromised or exposed to unauthorized entities.

### Step 1: Configure Log Level
By default, Traefik's log level is set to `ERROR`. However, to reduce the amount of potentially sensitive information being exposed, it can be set to `FATAL`. 
```bash
[log]
level = "FATAL"
```

### Step 2: Enable Access Logs Filtering
Traefik provides the capability to set up a filter for sensitive data which gets exposed in the access logs. It's necessary to set this filter in Traefik's configuration file under `[accessLog.filters]`.
```bash
[accessLog]
  [accessLog.filters]
    statusCodes = ["400-499"]
```
This will ensure that only access logs that contain HTTP status codes between 400 and 499 (inclusive) will be kept.

### Step 3: Hide Sensitive Data
Traefik also allows to redact sensitive information. To hide passwords, authorization tokens and other sensitive data, use the `[accessLog.fields]` filter to remove specific fields.
```bash
[accessLog]
  [accessLog.fields]
    [accessLog.fields.headers]
      [accessLog.fields.headers.names]
        "Authorization" = "redact"
        "Cookie" = "redact"
```

### Step 4: Regular Audit and Update
Similar to all other software services and systems, regularly conduct audits of your Traefik setup and keep your Traefik instance updated to the latest available version. This will ensure you are protected from any known vulnerabilities and are utilizing the latest security features.
```bash
docker pull traefik:latest
docker stop <your_traefik_container>
docker rm <your_traefik_container>
docker run -d -p 80:80 -p 8080:8080 -v $PWD/traefik.toml:/etc/traefik/traefik.toml traefik:latest
```