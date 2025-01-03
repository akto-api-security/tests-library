# Remediation for KIBANA_LFI

## Remediation Steps for Kibana Local File Inclusion (LFI)
Kibana local file inclusion (LFI) is a serious security issue that can lead to exposure of sensitive information. An attacker can use LFI to read local files on the server that Kibana is hosted on.

### Step 1: Update Kibana 
The first step to remediate Kibana LFI vulnerability is to upgrade your Kibana to a newer version that has patches for these security issues.
```bash
# Replace x.y.z with the desired version
wget https://artifacts.elastic.co/downloads/kibana/kibana-x.y.z-linux-x86_64.tar.gz
tar xzvf kibana-x.y.z-linux-x86_64.tar.gz
cd kibana-x.y.z-linux-x86_64/
```
### Step 2: Limit Access to File Paths
In your Kibana instance, restrict access to file paths that contain sensitive information. This is to prevent an attacker from reading arbitrary files from the host.
```bash
# Add this in your kibana.yml file
server.rewriteBasePath: true
#Specify false to prevent the basePath from being appended to the proxied paths.
server.basePath: "/your_base_path"
```
### Step 3: Network-level Security Measures
Implement network-level security measures such as VPN, IP whitelisting or SSH tunneling to ensure that Kibana is not directly exposed to the internet.
```bash
# Example of securing SSH as a network-level security measure
# Step 1: backup your SSH configuration file
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.factory-defaults
sudo chown root:root /etc/ssh/sshd_config.factory-defaults
sudo chmod 600 /etc/ssh/sshd_config.factory-defaults
# Step 2: Deny root logins
# In your SSH configuration file, find the PermitRootLogin line and edit it as follows:
PermitRootLogin no
# Save and exit the file
# Step 3: Restart your SSH service
sudo service ssh restart
```
### Step 4: Regular Audit and Update

Perform regular audit of your network and update Kibana as well as your operating system to the latest security patches.
```bash
# Update your Ubuntu system
sudo apt-get update -y 
sudo apt-get upgrade -y
```