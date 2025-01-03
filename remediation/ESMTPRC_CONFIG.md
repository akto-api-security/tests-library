# Remediation for ESMTPRC_CONFIG

## Remediation Steps for eSMTP - Config Discovery

eSMTP Config Discovery vulnerability can lead to the attacker discovering sensitive information that can be exploited. Remediation steps can include limiting the information that your SMTP server reveals during session initialization.

### Step 1: Update SMTP Server Configurations

Linux postfix command can be used to limit certain features of SMTPD banner. This can be executed in bash language:

```bash
sudo postconf -e 'smtpd_banner = $myhostname ESMTP Ready'
```
This will limit the information given out by the ESMTP server.

### Step 2: Disabling VRFY Command

VRFY command can disclose whether a user exists or not. Disable VRFY command in postfix:

```bash
sudo postconf -e 'disable_vrfy_command = yes'
```

### Step 3: Limit Debugging Information

Limit debugging information. This can help prevent information leakage.

```bash
sudo postconf -e 'debug_peer_level = 2'
```

### Step 4: Service Restart

After making the configuration changes, ensure to restart your postfix service to apply the new settings.

```bash
service postfix restart
```

These steps help secure eSMTP from configuration discovery by reducing the information given out during session initialization and disabling commands that may lead to user discovery.

Please note that these steps and commands may vary depending on the specific server software in use. Always consult your server software documentation for best practices relating to security and configuration.