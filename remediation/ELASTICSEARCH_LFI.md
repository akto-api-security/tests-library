# Remediation for ELASTICSEARCH_LFI

## Remediation Steps for Elasticsearch Local File Inclusion

Elasticsearch Local File Inclusion (LFI) can be a serious security threat. This vulnerability may allow an attacker to read files that are outside of the designated directories on the server. Therefore, we need to take appropriate actions to manage and secure Elasticsearch instances to prevent unauthorized local file inclusion.

### Step 1: Update to the Latest Version

First, ensure Elasticsearch is updated to its latest version. Elasticsearch has addressed several security issues in the latest updates. 

To check your current version:

```bash
curl 'http://localhost:9200'
```

To update Elasticsearch, it usually depends on your installation, but as an example, you can use:

```bash
sudo apt-get update && sudo apt-get install elasticsearch
```

### Step 2: Limit file:// Access

Add the following settings in your `elasticsearch.yml` to disallow any URIs that start with `file://`. This will prevent a large category of LFI attacks.

```yml
path:
  allow_unsafe_settings: false
```
You should restart Elasticsearch after modifying the configuration file.

```bash
sudo service elasticsearch restart
```
### Step 3: Configure Proper User Access Control

Make sure there are proper access control rules in place. This will minimize the risk of an attacker getting access to Elasticsearch console or API.

```bash
chown -R elasticsearch:elasticsearch /etc/elasticsearch
chmod 700 /etc/elasticsearch
```

### Step 4: Use Elasticsearch Security Features

Elasticsearch now comes with built-in security features, which includes built-in roles for common use cases, and the ability to create your own custom roles.

```bash
PUT /_security/role/my_admin_role
{
  "cluster": ["all"],
  "indices": [
    {
      "names": ["*"],
      "privileges": ["all"]
    }
  ]
}
```
