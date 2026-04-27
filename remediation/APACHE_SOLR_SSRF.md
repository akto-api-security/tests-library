

## Remediation Steps for Apache Solr Server-Side Request Forgery

Server-Side Request Forgery (SSRF) in Apache Solr is a security issue that could allow an attacker to make HTTP requests to any internal resources accessible by the server hosting the Solr instance.

### Step 1: Upgrade to a Non-vulnerable Version of Apache Solr

The first step is to check the version of Apache Solr that is currently in use. The versions vulnerable to SSRF are 5.0.0 to 8.1.1. Hence, it is highly advisable to upgrade Solr to a more recent version where this issue has been fixed.

```bash
wget https://downloads.apache.org/lucene/solr/{latest-version}/solr-{latest-version}.tgz
tar xzf solr-{latest-version}.tgz solr-{latest-version}/bin/install_solr_service.sh --strip-components=2
sudo bash ./install_solr_service.sh solr-{latest-version}.tgz
```

Please replace `{latest-version}` with the actual latest version.

### Step 2: Limit Network Access

It is always a good practice to limit the access to your Apache Solr instance to only trustworthy domains or local networks using firewall rules.

```bash
sudo ufw enable
sudo ufw allow from <trusted_network> to any port <solr_port>
```

Replace `<trusted_network>` with your trusted network and `<solr_port>` with the Apache Solr port.

### Step 3: Limit URL Parameter Configurations

It's likewise recommended to set up URL parameter configurations to limit what can be parsed through the URL.

Example in java:

```java
UpdateRequest updateRequest = new UpdateRequest("/update");
...
updateRequest.setParam("stream.url", "http://trusted-domain.com/resource");
...
updateRequest.process(solrClient);
```