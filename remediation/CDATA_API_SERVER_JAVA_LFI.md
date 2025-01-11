# Remediation for CDATA_API_SERVER_JAVA_LFI

## Remediation Steps for CData API Server Java Local File Inclusion

A local file Inclusion vulnerability allows an attacker to read and execute local files on the server that they are not supposed to have access to. Thus, it is important to fix this vulnerability in CData API Server Java to ensure the security of server files.

### Step 1: Validate User Input

Consider user input validation as the primary defence mechanism. This will be done by verifying user input to make sure it contains only the expected values.

```java
String userFile = request.getParameter("file");
if (userFile.contains("../") || userFile.contains("..\\")){
    response.sendError(HttpServletResponse.SC_FORBIDDEN);
    return;
}
```

### Step 2: Use a Safe Method for File Access

Take advantage of Java's `getRealPath()` method which returns null, if the path contains ".." thus preventing directory traversal.

```java
ServletContext context = getServletContext();
String fullPathToFile = context.getRealPath("/WEB-INF/" + userFile);
```
This will only allow requested files from the WEB-INF directory, and no parent or other child directories.

### Step 3: Restrict File Permissions

Make sure file permissions are properly configured and restrictive. Regular users should not have unnecessary access to files.

```bash
chmod 700 sensitive_file
```