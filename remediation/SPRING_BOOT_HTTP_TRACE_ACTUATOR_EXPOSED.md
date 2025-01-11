# Remediation for SPRING_BOOT_HTTP_TRACE_ACTUATOR_EXPOSED

## Remediation Steps for Spring Boot HTTP Trace Actuator Exposed
Having Spring Boot HTTP Trace Actuator exposed is a serious security issue. This can potentially allow attackers to execute cross-site tracing attacks, and get unauthorized access to sensitive data. It is highly advised to disable the HTTP TRACE method for all applications.

### Step 1: Disable HTTP TRACE
In your Spring Boot application, the HTTP TRACE method is by default enabled. You have to explicitly disable it. 

Here is an example of how you can disable HTTP TRACE in a Spring Boot application using Java:

```java
import org.springframework.boot.autoconfigure.security.servlet.PathRequest;
import org.springframework.boot.web.embedded.tomcat.TomcatServletWebServerFactory;
import org.springframework.boot.web.server.WebServerFactoryCustomizer;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class TraceMethodDisableConfig {

    @Bean
    public WebServerFactoryCustomizer<TomcatServletWebServerFactory> containerCustomizer() {
        return container -> container.addConnectorCustomizers(connector -> 
            connector.setProperty("rejectIllegalHeader", "true")
        );
    }
}
```
The above configuration will make your Tomcat instance reject HTTP TRACE requests.
