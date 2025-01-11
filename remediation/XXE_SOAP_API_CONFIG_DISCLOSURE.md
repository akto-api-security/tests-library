# Remediation for XXE_SOAP_API_CONFIG_DISCLOSURE

## Remediation Steps for XML External Entity (XXE) on SOAP API for Configuration Disclosure

The XXE (XML External Entity) attack is a type of attack against an application that parses XML inputs. Here, the attacker can view files on the application server filesystem and interact with internal systems. Particularly in a SOAP API, this can lead to significant information disclosure if not well-secured.

Here are the steps to remediate the issue:

### Step 1: Disable DTD (Document Type Definitions)
Disable Document Type Definitions (DTD) in your XML parser configuration to prevent XXE attacks. This will block any external entity declaration and can be done during the XML parsing process.

For Java, this can be done usually by the following parts:
```java
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
String FEATURE = null;
try {
    // Disable DTDs (External Entities) altogether
    FEATURE = "http://apache.org/xml/features/disallow-doctype-decl";
    dbf.setFeature(FEATURE, true);
} catch (ParserConfigurationException e) {
    // Handle the Exception
}
```

### Step 2: Securely Configure XML Parsers
You should properly configure XML parsers and disable the use of External Entities (XXE) in Document Builders. This will minimize the possibility of content disclosure and denial of service attacks.
```java
dbf = DocumentBuilderFactory.newInstance();
String FEATURE = null;
FEATURE = "http://xml.org/sax/features/external-general-entities";
dbf.setFeature(FEATURE, false);
FEATURE = "http://xml.org/sax/features/external-parameter-entities";
dbf.setFeature(FEATURE, false);
FEATURE = "http://apache.org/xml/features/nonvalidating/load-external-dtd";
dbf.setFeature(FEATURE, false);
dbf.setXIncludeAware(false);
dbf.setExpandEntityReferences(false);
```