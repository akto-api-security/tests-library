# Remediation for WSO2_API_MANAGER_XXE

## Remediation Steps for WSO2 API Manager Blind XXE Test

Blind XML External Entity (XXE) vulnerability allows attackers to retrieve sensitive data and interact with any back-end or external systems that the application itself can access. Here are the steps to secure and fix the vulnerability in WSO2 API Manager.

### Step 1: Adjust XML Processor settings

The XML processor in the server should be properly configured to ignore DOCTYPE declarations from XML requests.

In Java, this can be achieved with:

```java
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();

// Disable DOCTYPE declaration
dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
```

### Step 2: Create a custom XML entity resolver

Create a custom entity resolver to ensure that no external entities or DTDs are being processed. 

In Java:

```java
dbf.setEntityResolver(new EntityResolver() {
    @Override
    public InputSource resolveEntity(String publicId, String systemId) throws SAXException, IOException {
        return new InputSource(new StringReader(""));
    }
});
```

### Step 3: Use less complex data formats

If possible, consider using less complex data formats such as JSON, which doesn't have the support for defining entities.