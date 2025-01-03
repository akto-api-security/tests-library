# Remediation for APACHE_PULSAR_EXPOSED

## Remediation Steps for Exposed Apache Pulsar 

Exposed Apache Pulsar is a serious security issue that can give unauthorized users the ability to read and alter your messages. Applying Authentication, Auhorization, and Encryption are ways to secure Apache Pulsar.

### Step 1: Enable Authentication
Below process will enable token based authentication in Apache Puslar.

```bash
# Create a secret key
bin/pulsar tokens create-secret-key --output my-secret.key

# Use the key to create a token for a client
bin/pulsar tokens create --secret-key file:///path/to/my-secret.key --subject client-1
```
In your `broker.conf` or `standalone.conf`, configure Pulsar to authenticate clients:

```properties
authenticationEnabled=true
authenticationProviders=org.apache.pulsar.broker.authentication.AuthenticationProviderToken

tokenSecretKey=file:///path/to/my-secret.key
```

```bash
# Restart the service
bin/pulsar-daemon stop broker
bin/pulsar-daemon start broker
```

### Step 2: Enable Authorization
```properties
# In your broker.conf or standalone.conf
authorizationEnabled=true
authorizationProvider=org.apache.pulsar.broker.authorization.PulsarAuthorizationProvider
```

### Step 3: Enable Encryption
In Pulsar, encryption is performed in the producers and consumers. Configure your client to use encryption:

```java
//Java Code:
Producer<T> producer = client.newProducer(Schema.STRING)
                     .topic("persistent://sample/standalone/ns1/my-topic")
                     .addEncryptionKey("my-app-key")
                     .cryptoKeyReader(new RawFileKeyReader("path/pub_key_file", "path/priv_key_file"))
                     .create();

Consumer<T> consumer = client.newConsumer(Schema.STRING)
                      .topic("persistent://sample/standalone/ns1/my-topic")
                       .subscriptionName("sub1")
                       .cryptoKeyReader(new RawFileKeyReader("path/pub_key_file", "path/priv_key_file")
                       .subscribe();
```

### Step 4: Regular Update and Audit
Regularly update your Apache Pulsar software to ensure you're using a version with the latest security patches. Also, conduct regular audits of logs for any unusual activity. 

```bash
# Check your version
pulsar-admin brokers version
# Update your software
sudo apt-get install --only-upgrade pulsar
```

Remember, it's best to use multi-layered security, like using both authentication and encryption, to provide the most robust protection for your Pulsar setup.