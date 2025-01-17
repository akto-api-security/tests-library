

## Remediation Steps for XML External XInclude Injection

The XInclude Injection is a serious security flaw. Attackers can exploit this vulnerability to read system files by crafting specific XML documents that are processed by the vulnerable application. 

### Step 1: Disable XInclude in XML Parser 

In most XML parsers, XInclude feature is enabled by default. Your utmost priority should be to disable this feature of XML parser. The method to disable XInclude depends on the parser in use. 

For example, in .Net XML Parser: 
```csharp
// Create an XmlReaderSettings object.
XmlReaderSettings settings = new XmlReaderSettings();

// Disable XInclude processing.
settings.ProhibitDtd = true;

// Create an XmlReader object. 
XmlReader reader = XmlReader.Create("input.xml", settings);
```
In Python using lxml:
```python
from lxml import etree

# Parse XML without XInclude
parser = etree.XMLParser(resolve_entities=False)

#parse
tree = etree.parse("input.xml", parser)
```
### Step 2: Data Validation

Always validate data that is coming from untrusted sources to prevent injection attacks. One of the effective way is to use XML Schema Definition (XSD). 

For example, in .Net XML Parser: 
```csharp
// Create the XmlReader object.
XmlReaderSettings settings = new XmlReaderSettings();
settings.Schemas.Add("http://www.contoso.com/books", "contosoBooks.xsd");
settings.ValidationType = ValidationType.Schema;

XmlReader reader = XmlReader.Create("contosoBooks.xml", settings);
```
```
### Step 3: Implement Least Privilege Principle

Give the XML parser the lowest permissions possible, so even if there is an XML External XInclude Injection attack, the attacker won't be able to read sensitive files on your server. 

For example,
```bash
# Change the XML parser user to a user with limited permissions 
sudo chown limited-permission-user:path-to-your-parser 
```