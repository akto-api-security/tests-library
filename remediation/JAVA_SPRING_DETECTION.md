

## Remediation Steps for Java Spring Framework Detection

Sensitive information about your application's architecture can be exploited by attackers if Java Spring Framework detection is made possible. In order to reduce the potential for such attacks, it is vital to restrict access to or mask identifiable information.

### Step 1: Remove Version Information

In the case of a Spring Boot application, version information tends to be available in HTTP responses under the "X-Application-Context" header. You can resolve this issue by setting `server.servlet.application-display-name` to an empty string or irrelevant text in your application properties, e.g., `server.servlet.application-display-name=My Application`.

```java
SpringApplication app = new SpringApplication(MyApplication.class);
app.setDefaultProperties(Collections
  .singletonMap("server.servlet.application-display-name", "My Application"));
app.run(args);
```

### Step 2: Secure Processors

Add a custom bean of type `ErrorAttributes` that will control how error attributes are populated. This way, you can remove or mask sensitive data when handling errors.

```java
import org.springframework.boot.web.servlet.error.DefaultErrorAttributes;
import org.springframework.web.context.request.WebRequest;

public class CustomErrorAttributes extends DefaultErrorAttributes {

  @Override
  public Map<String, Object> getErrorAttributes(WebRequest webRequest, boolean includeStackTrace) {
    Map<String, Object> errorAttributes = super.getErrorAttributes(webRequest, includeStackTrace);
    errorAttributes.remove("sensitive info"); // replace "sensitive info" with actual sensitive data key
    return errorAttributes;
  }
}
```