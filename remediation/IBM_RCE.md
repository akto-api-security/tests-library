# Remediation for IBM_RCE

## Remediation Steps for IBM WebSphere Java Object Deserialization RCE

IBM WebSphere Java Object Deserialization Remote Code Execution (RCE) is a critical security vulnerability that can potentially allow attackers to execute arbitrary code in the context of the system.

### Step 1: Update to the Latest Version
The first and foremost step in mitigating this security vulnerability is to update the IBM WebSphere application server to the most recent version. IBM often releases patches and updates to fix known security vulnerabilities.

```bash
sudo yum update WebSphere
```

### Step 2: Enable Serialization Filtering

Java provides a mechanism to prevent deserialization of untrusted object types.

You can use the process-wide `jdk.serialFilter` system property

```java
System.setProperty("jdk.serialFilter", "com.myApp.MyClass;!*");
```

Or, provide a filter for a specific ObjectInputStream

```java
ObjectInputStream ois = ...;
ois.setObjectInputFilter(filter);
```

These filters will block deserialization of untrusted object types.

### Step 3: Adhere to Least Privilege Principle

Implementing the principle of least privilege can significantly reduce the potential impact of an RCE vulnerability. An attacker can only exploit the privileges of the component that has been compromised. 

Ensure that all services are running with the least privileges needed for their function.