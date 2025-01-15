# Remediation for LIGHTHTTPD_CONFIG_EXPOSED

## Remediation Steps for Lighttpd Config Exposed

The exposure of Lighttpd configuration settings can lead to serious security issues as it may provide potential attackers with sensitive information, allowing them to exploit vulnerabilities in your system. Following are the remediation steps:

### Step 1: Safeguard config file permissions

The first step towards remediation is to change the configurations files' permissions so they are not readable by unauthorized users.

```bash
sudo chmod 640 /etc/lighttpd/lighttpd.conf
sudo chown root:www-data /etc/lighttpd/lighttpd.conf
```

The above commands changes the permissions of the lighttpd.conf file in such a way that only users in the www-data group can read it.

### Step 2: Restrict Direct Access To Configuration Files

The location of the configuration files must not be under the web root. If they are under the web root, add the following block to the lighttpd config (40-deny-direct-access.conf) to prevent direct access:

```bash
$HTTP["url"] =~ "^/config/" {
   url.access-deny = ("")
}
```

The above configuration will block direct HTTP access to any files or directories with ‘config’ in the URL, per lighttpd’s url.access-deny directive.
