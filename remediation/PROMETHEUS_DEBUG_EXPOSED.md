# Remediation for PROMETHEUS_DEBUG_EXPOSED

## Remediation Steps for Prometheus Debug Exposure
Prometheus debug exposure is a serious security issue that can allow unauthorized access to debug endpoints. Therefore, it's important to ensure these are not exposed in a production environment.

### Step 1: Disable Debug Flag
Debug endpoints are enabled by adding the `--web.enable-admin-api` flag to Prometheus' start-up command. This flag should not be used in production setups.
```bash
./prometheus --web.enable-admin-api
```
Remove the `--web.enable-admin-api` flag from your startup command or script to disable the debug API.

### Step 2: Network Firewall Configuration
Ensure that your network firewall rules do not allow access to the debug API. For example, service exposed on port 9090 should be blocked to all non-local access. Replace `x.x.x.x` with the correct Prometheus server's IP address.
```bash
sudo iptables -A INPUT -p tcp -s ! x.x.x.x --dport 9090 -j DROP
```

### Step 3: Regular Audit and Update
Monitor the Prometheus logs on a regular basis to check if there are unauthorized access attempts and remediate or report if any are found.
```bash
journalctl -u prometheus
```

Finally, ensure that the Prometheus server is regularly updated to benefit from the latest security patches.