# Remediation for NETMASK_SSRF

## Remediation Steps for Netmask NPM Package Server-Side Request Forgery

Server-Side Request Forgery (SSRF) vulnerability in the Netmask NPM package can lead to serious security issues, as it could potentially allow attackers to make requests to internal resources that were previously inaccessible. 

The Netmask NPM Package Server-Side Request Forgery is caused by an octal parsing bug meaning IP addresses with a leading zero are treated as octal and the result could be connecting to an unintended internal IP address.

Here are the steps you can take to mitigate this security issue:

### Step 1: Upgrade Netmask  Package

The first and most direct way to deal with this Vulnerability is to upgrade the Netmask package to version 2.0.1 or later which no longer has this vulnerability.
 
Use this command to upgrade the package:

```bash
npm install netmask@2.0.1
```

### Step 2: Validate IP Addresses 

Perhaps you can't upgrade for some reason or maybe you want an extra layer of protection. In this case, validating IP addresses before using them might be helpful.

The netmask library is typically used to judge if an IP is in a certain range/an IP whitelist. Ensure that none of the IPs in your whitelist have a leading zero, for this you can use a regular expression check before adding IPs to the whitelist. 

```javascript
function validateIPaddress(ipaddress) {
  if (/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/.test(ipaddress)) {
    return (true)
  }
  alert("You have entered an invalid IP address!")
  return (false)
}
```

Perform this check before adding IPs to the whitelist, and ensure you're not adding IPs with a leading zero.