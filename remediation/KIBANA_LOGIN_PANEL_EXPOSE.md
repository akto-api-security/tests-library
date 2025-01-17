

## Remediation Steps for Kibana Login Panel Exposure
Kibana Login Panel Exposure is a potential security risk that allows unauthorized users to gain access to Kibana dashboards. By properly securing the Kibana Login Panel, you can prevent unauthorized access to sensitive information.

### Step 1: Enable Kibana Security Features
Enable X-Pack Security on Elasticsearch and Kibana. For that, you have to set `xpack.security.enabled` to `true` in both elasticsearch.yml and kibana.yml configuration files. This step will enable authentication requirement to access Kibana interface.
```bash
echo 'xpack.security.enabled: true' >> /etc/elasticsearch/elasticsearch.yml
echo 'xpack.security.enabled: true' >> /usr/share/kibana/kibana.yml
```

### Step 2: Set Username and Password for Kibana
Create a password for Kibana user `kibana_system` using `elasticsearch-setup-passwords` command. This user is used for Kibana to connect to Elasticsearch.
```bash
bin/elasticsearch-setup-passwords interactive
```

### Step 3: Configure Kibana with the new user
Configure Kibana to use `kibana_system` user for its internal requests to Elasticsearch. Update `elasticsearch.username` and `elasticsearch.password` in kibana.yml with the `kibana_system` user.
```bash
echo 'elasticsearch.username: "kibana_system"' >> /usr/share/kibana/kibana.yml
echo 'elasticsearch.password: "your_password"' >> /usr/share/kibana/kibana.yml
```

### Step 4: Restart Kibana and Elasticsearch services
```bash
sudo systemctl restart elasticsearch.service
sudo systemctl restart kibana.service
```

After performing these steps, Kibana login panel will no longer be exposed and access to it will require authentication. Remember to replace `your_password` with the password you created for `kibana_system` user.