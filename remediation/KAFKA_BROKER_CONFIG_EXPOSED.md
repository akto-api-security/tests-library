# Remediation for KAFKA_BROKER_CONFIG_EXPOSED

## Remediation Steps for Exposed Kafka Broker Config
Exposed Kafka Broker Config represents a serious security concern. If not properly secured, the Kafka Broker can be compromised and unauthorized activities may take place.
### Step 1: Secure Broker Configuration Files
Ensure all your broker configuration files are secured and not accessible for unauthorized users.

```bash
chown kafka:kafka /etc/kafka/server.properties
chmod 600 /etc/kafka/server.properties
```
### Step 2: Enable Firewall for Kafka Ports
Kafka uses port 9092 by default. Block inbound connections to this port unless they're necessary for your use case.
```bash
sudo ufw deny from any to any port 9092
```
### Step 3: Use Security Protocols (SSL, SASL)
Update Kafka configuration file to use SSL or SASL, this would encrypt interaction with Kafka Broker and helps ensure secure communication.
```bash
# An example for SSL:
echo 'listeners=PLAINTEXT://:9092,SSL://:9093' >> /etc/kafka/server.properties
echo 'ssl.keystore.location=/var/private/ssl/kafka.server.keystore.jks' >> /etc/kafka/server.properties
echo 'ssl.keystore.password=test1234' >> /etc/kafka/server.properties
echo 'ssl.key.password=test1234' >> /etc/kafka/server.properties
echo 'ssl.truststore.location=/var/private/ssl/kafka.server.truststore.jks' >> /etc/kafka/server.properties
echo 'ssl.truststore.password=test1234' >> /etc/kafka/server.properties
```
### Step 4: Regular Audit and Update 
Perform a regular audit and update of Kafka Broker configurations.
```bash
# example to start the Kafka broker and let it load the updated config
sudo service kafka start
```

Note: Replace `'test1234'` with your secure passwords and `/var/private/ssl/kafka.server.keystore.jks, /var/private/ssl/kafka.server.truststore.jks` with your own generated key/truststore files in the commands provided above.