# Remediation for XSTREAM_RCE

## Remediation Steps for XStream API Remote Code Execution
XStream is a simple library to serialize objects to XML and back again, which can lead to Remote Code Execution if not properly used. Here, we provide some steps to mitigate these vulnerabilities.

### Step 1: Updating Version
Make sure you are using a non-vulnerable version of XStream API suite.
Check for the latest version [here](http://x-stream.github.io/download.html). If you are using Maven, update your `pom.xml`:
```xml
<dependency>
  <groupId>com.thoughtworks.xstream</groupId>
  <artifactId>xstream</artifactId>
  <version>1.4.18</version> <!-- use latest version here -->
</dependency>
```
### Step 2: Setting the Security Framework
Call `XStream.setupDefaultSecurity` to limit XStream API to not serialize potentially harmful classes.
```java
XStream xstream = new XStream();
xstream.setupDefaultSecurity(null); 
```
### Step 3: Allowing Specific Classes
You should allow only those classes which you own or trust. This can prevent an attacker from injecting malicious classes during deserialization.
Add explicit call to each of classes that needs to be process.
```java
XStream xstream = new XStream();
Class<?>[] classes = new Class[] { MyClass1.class, MyClass2.class, MyClass3.class };
xstream.allowTypes(classes);
```
### Step 4: Reject Unknown Elements
You can ask XStream to reject unknown elements in the XML document, that is elements that do not correspond to a field of the object being unmarshalled.
```java
xstream.ignoreUnknownElements();
```
### Step 5: Apply A Custom Converter
For potentially unsafe types, consider applying a custom converter that will control exactly what gets serialized and deserialized.
```java
xstream.registerConverter(new MyClassConverter());
```