# Remediation for ZOOKEEPER_EXPOSED

## Remediation Steps for Zookeeper APIs Exposure
Zookeeper APIs exposure can lead to serious security issues. Without proper security measures, attackers can gain unauthorized access to vital system components, leading to service disruption or confidential data theft. 

### Step 1: Disable Unnecessary Zookeeper Client Ports

Unnecessary open ports can pose a security risk. You should close all ports that are not relevant to mission requirements and also add firewall rules to block unwanted traffic.

```bash
  #!/bin/bash
  sudo iptables -A INPUT -p tcp --dport zookeeper_port -j DROP
  # replace zookeeper_port with the actual port number
```

### Step 2: Enable Zookeeper ACL (Access Control List)

Make sure to configure ACL to Zookeeper, which control access to znodes by clients.

In Java:
```java
import org.apache.zookeeper.ZooDefs.Ids;
import org.apache.zookeeper.CreateMode;
import org.apache.zookeeper.ZooKeeper;
import org.apache.zookeeper.data.ACL;

...

ArrayList<ACL> acls = new ArrayList<ACL>(Ids.CREATOR_ALL_ACL);
zooKeeper.create("/path", "data".getBytes(), acls, CreateMode.PERSISTENT);
```

In Python:
```python
from kazoo.security import make_digest_acl

acl = make_digest_acl('guest', 'password', read=True)
client.default_acl = acl
```

### Step 3: Plus Use Firewall To Limit and Monitor Access

Use a firewall to monitor and limit traffic to the Zookeeper, allowing only the necessary cluster nodes and application servers to interact.

```bash
sudo ufw allow from trusted_ip to any port zookeeper_port
sudo ufw deny from any to any port zookeeper_port
```
Note: trusted_ip should be replaced with the actual IP address of a host you trust, and zookeeper_port should be replaced with the actual port number.