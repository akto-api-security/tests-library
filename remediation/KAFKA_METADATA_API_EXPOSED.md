

## Remediation Steps for Kafka Metadata API Exposure
Kafka Metadata API exposure is a significant security threat. Proper securing of the Kafka Metadata API is crucial to prevent unauthorized access to Kafka metadata, which can cause significant harm to your data flow and indirectly your entire system.

### Step 1: Restricting Kafka Brokers to Known Clients

Use the `listeners` parameter in the `server.properties` file of each broker. This allows the broker to listen only to specific IPs of known instances.

```bash
listeners=PLAINTEXT://your.host.name:9092
```

### Step 2: Enable SASL authentication

Kafka supports client authentication via SASL. Multiple SASL mechanisms can be enabled on the broker and are offered in the order of preference during SASL handshake. 

Update your `server.properties`:

```bash
sasl.enabled.mechanisms=PLAIN
```

### Step 3: Setup ACLs (Access Control Lists)

ACLs allow you to define which users (Principals) have access to read or write to Topics. Use the following script to apply ACLs:

```bash
kafka-acls --authorizer-properties zookeeper.connect=localhost:2181 --add --allow-principal User:Bob --topic topicA
```