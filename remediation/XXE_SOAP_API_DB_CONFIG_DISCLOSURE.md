

## Remediation Steps for XML External Entity (XXE) on SOAP API for Database Configuration Disclosure

An XML External Entity (XXE) attack on SOAP APIs can lead to disclosure of confidential data, denial of service, and server-side request forgery. Therefore, it's critical to properly secure your SOAP APIs against XXE attacks.

### Step 1: Disable DTDs

In SOAP 1.2, DTDs should be disabled. DTDs allow XML documents to define general entities with public identifiers that can be reused throughout the document. Attackers can use these identifiers to create recursive payloads causing DoS attacks or to inject malicious data.

For Java applications, this may include setting up appropriate properties when creating a `DocumentBuilderFactory`:

```java
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
```

### Step 2: Disable External Entities

Explicitly disable the use of external entities in your SOAP API parser. This can prevent the server from fetching any external resources.

In a java-based SOAP application, it can be achieved as follows:

```java
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
dbf.setFeature("http://xml.org/sax/features/external-general-entities", false);
dbf.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
dbf.setFeature("http://apache.org/xml/features/nonvalidating/load-external-dtd", false);
```

### Step 3: Use Less Complex Data Formats

Consider using less complex data formats such as JSON, and avoid serialisation of sensitive data.


### Step 4: Implement Positive Server-Side Input Validation

Implement strong server-side input validation to reject any unexpected or malicious inputs.

```java
String safeInput = ESAPI.validator().getValidInput("User Input", userInput,"SafeString", 200, false);
```

### Step 6: Use Security Header

Enable a security header like X-Content-Type-Options which mitigates Cross-site Scripting (XSS) attacks by preventing the browser from interpreting files as something else than declared by the content type in the HTTP headers.

```java
response.setHeader("X-Content-Type-Options", "nosniff");
```