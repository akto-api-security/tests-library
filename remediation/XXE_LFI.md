# Remediation for XXE_LFI

## Remediation Steps for XML External Entity (XXE) Test for Local File Inclusion
An XML External Entity attack is a type of attack against an application that analyzes XML input. This particular security issue can lead to the disclosure of internal files, denial of service, server side request forgery, port scanning from the perspective of the machine where the parser is located.

### Step 1: Disable XXE
The easiest way to prevent XXE attacks is to disable DTDs (Document Type Definitions). Unfortunately, this is parser dependent. Below is an example in Java how to do this:

```java
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
```

### Step 2: Limit XML External Entity impact - Local File Inclusion
For parsers where the XML External Entity vulnerability cannot be completely disabled, consider limiting the impact. 

For instance, using Java, you can restrict access to the file system from your parser with the following:

```java
dbf.setFeature("http://xml.org/sax/features/external-general-entities", false);
dbf.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
dbf.setFeature("http://apache.org/xml/features/nonvalidating/load-external-dtd", false);
```

### Step 3: Update XML Parsers
Make sure all your XML parsers are up-to-date as security patches are regularly issued to fix these vulnerabilities.