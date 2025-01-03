# Remediation for SPRING_BOOT_CONFIG_PROPS_ACTUATOR_EXPOSED

## Remediation Steps for Spring Boot Configuration Properties Actuator Exposure

The exposure of Spring Boot Configuration Properties Actuator is a serious security issue. This allows unauthorized access to sensitive configuration details that may lead to a highly successful attack on the Spring Boot application.

### Step 1: Disable the Actuator Endpoint

In your `application.properties` file, disable the endpoint:

```properties
management.endpoint.configprops.enabled=false
```

### Step 2: Limit Access to the Actuator Endpoints

Allow only authorized personnel to access sensitive actuator endpoints. This can be accomplished by implementing Spring Security.

For example, in your Spring Security configuration file, you can limit access to the actuator endpoints to a specific role:

```java
http
    .authorizeRequests()
    .requestMatchers(EndpointRequest.to("configprops")).hasRole("ACTUATOR_ADMIN")
    .requestMatchers(EndpointRequest.toAnyEndpoint()).permitAll()
    .and()
    .httpBasic();
```

### Step 3: Regular Code Audit and Update

Regularly audit your codebase to ensure that new actuator endpoints are not unintentionally exposed. Ensure you are familiar with all enabled endpoints and their potential risks.

### Step 4: Use Spring 2.0 or higher versions

Spring Boot 2.0 changed the default behavior to not expose any endpoints over HTTP, therefore it is a good idea to use Spring 2.0 or higher versions.

```properties
# expose only health and info
management.endpoints.web.exposure.include=health,info
# do not expose any endpoint
management.endpoints.web.exposure.exclude=*
```