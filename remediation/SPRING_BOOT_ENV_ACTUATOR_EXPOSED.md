# Remediation for SPRING_BOOT_ENV_ACTUATOR_EXPOSED

## Remediation Steps for Spring Boot Environment Actuator Exposed

Exposing Spring Boot Environment Actuator makes your applications highly vulnerable by showing sensitive environment properties. These can be used maliciously if intercepted by unauthorized entities.

### Step 1: Disable Actuator Endpoints Globally
You can disable the exposure of actuator endpoints globally by setting the following property in the `application.properties` file. 

```java
management.endpoints.web.exposure.include= # to completely disable
```
Or you can disable it selectively like so:
```java
management.endpoints.web.exposure.exclude=env,beans # for disabling specific endpoints
```

### Step 2: Secure Actuator Endpoints With Spring Security
Make use of Spring Security to secure actuator endpoints by adding it as a dependency in your `pom.xml` file:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

Then, configure Spring Security to provide access only to authenticated users:

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
         .authorizeRequests()
         .antMatchers("/actuator/**").authenticated()
         .and()
         .httpBasic();
    }
}
```