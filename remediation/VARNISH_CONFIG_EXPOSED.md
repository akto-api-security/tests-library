# Remediation for VARNISH_CONFIG_EXPOSED

## Remediation Steps for Varnish Config Exposure
Varnish Config exposure is a severe security issue. It can allow attackers to access sensitive user information and possibly execute arbitrary commands. It's crucial to secure Varnish Config to prevent unnecessary exposure.

### Step 1: Protect Varnish Status
Firstly, configuration rules should be put into place to limit access to the Varnish status.

```bash
acl purger {
    "localhost";
    "192.168.55.0"/24;
}

sub vcl_recv {
    if (req.url ~ "^/status$" && !client.ip ~ purger) {
        return(synth(405,"Not allowed."));
    }
}
```

### Step 2: Setup System-Level Firewalls
Implement system-level firewalls to block unauthorized IP addresses.

```bash
sudo ufw deny from any to any port 6082
```

### Step 3: Varnish Secret File
Use a secret file with Varnish, so that only applications which know that can purge cache. It is also recommended to change the default Varnish secret.

```bash
sudo nano /etc/varnish/secret
```
Generate a new secret, save it and restart Varnish.

```bash
sudo service varnish restart
```