

## Remediation Steps for Grafana Unauthenticated Snapshot Creation

Grafana Unauthenticated Snapshot Creation is a serious security issue. If the snapshot creation is not properly authenticated, attackers could create a snapshot of your dashboard without authorization, which could compromise the data being visualized.

### Step 1: Upgrade Grafana to a patched version

The best way to protect your system from this vulnerability is to always use the latest version of Grafana. The vulnerability was patched since version 2.6.0.

If you're using Linux, you can use these commands to stop the Grafana service, upgrade it and then start the service again:

```bash
sudo service grafana-server stop
sudo yum update grafana
sudo service grafana-server start
```

### Step 2: Disable anonymous access

By default, Grafana allows anyone to create dashboards and snapshots. To protect your system, you should disable anonymous access.

For this, you should provide explicit `users` and `admins` in the Grafana configuration file:

```ini
[auth.anonymous]
# disable anonymous access
enabled = false
```

### Step 3: Require authentication for snapshot creation

On the Grafana server, locate the configuration file (`grafana.ini`) and identify the `[snapshots]` section. Set the `public_mode` flag to `false` to enforce authentication for snapshot creation:

```ini
[snapshots]
# disable public snapshots
public_mode = false
```
After making the above changes, ensure to restart the Grafana server for the changes to take effect:

```bash
sudo service grafana-server restart
```

By applying these changes, you help to protect your Grafana data from unauthenticated snapshot creation.