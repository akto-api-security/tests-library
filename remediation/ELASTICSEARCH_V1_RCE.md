# Remediation for ELASTICSEARCH_V1_RCE

## Remediation Steps for ElasticSearch v1.1.1/1.2 Remote Code Execution
Elasticsearch versions 1.1.1 and 1.2 RCE is a serious security vulnerability. Attackers can exploit this weakness to carry out remote code execution attacks, thereby affecting the security of data and resources.

### Step 1: Update Elasticsearch
The very first step to remediate this vulnerability is to update your Elasticsearch installation to a latest stable version. Here is a command to do it via command line using curl and dpkg.
```bash
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.15.2-amd64.deb
sudo dpkg -i elasticsearch-7.15.2-amd64.deb
```
Remember to replace "7.15.2" with the version number you are upgrading to. Check the latest version at the official Elasticsearch [downloads page](https://www.elastic.co/downloads/elasticsearch).

### Step 2: Secure Elasticsearch Configuration
After the installation is complete, disable dynamic scripts by setting `script.inline` and `script.stored` to false in the `elasticsearch.yml` configuration file. Here is how to do it:
```yaml
script.inline: false
script.stored: false
```
Location of the Elasticsearch configuration file (`elasticsearch.yml`) depends on the method of installation but typically it’s located at `/etc/elasticsearch/elasticsearch.yml`.

### Step 3: Restart Elasticsearch Service
After applying configuration changes, don’t forget to restart Elasticsearch service for changes to take effect.
```bash
sudo systemctl restart elasticsearch
```
If the service restart command raises any error then consult Elasticsearch log files for troubleshooting.

These steps will help to fix the Elasticsearch RCE vulnerability. For heightened security, enforce access control, enable secure HTTPS communications in Elasticsearch, and carry out regular audits and updates. 

Remember to always keep backup before updating any software or making changes to configuration files.