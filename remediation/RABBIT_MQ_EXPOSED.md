

## Remediation Steps for RabbitMQ Exposure
RabbitMQ exposure is a significant security concern. If not properly secured, RabbitMQ could be exploited by hackers leading to unauthorized access and potential data breaches.

### Step 1: Disable Unnecessary Access
Mostly, RabbitMQ is exposed because of the unnecessary wide access possibility. Make sure you limit the access to the desired end points only. RabbitMQ configures the applicable policies on their respective vhosts.

```bash
rabbitmqctl set_permissions [-p vhost] user configure_regex write_regex read_regex
```

### Step 2: Enable TLS/SSL
It is essential to encrypt the data in transfer by enabling the SSL/TLS in RabbitMQ.

```bash
# Add these lines to rabbitmq.config file
[
  {rabbit, [
    {ssl_listeners, [5671]},
    {ssl_options, [{cacertfile,"/path/to/ca_certificate.pem"},
                   {certfile,"/path/to/server_certificate.pem"},
                   {keyfile,"/path/to/server_key.pem"},
                   {verify,verify_peer},
                   {ssl_cert_login_from,distinguished_name}]
    }
  ]}
].
```

### Step 3: Firewall Configuration
Configure the firewall to restrict access to your RabbitMQ ports to only trusted IP addresses.

```bash
# ufw (Uncomplicated Firewall) is used for managing firewall on ubuntu
# deny access to all by default
sudo ufw deny from any to any port 5672

# allow access only from trusted_IP_address
sudo ufw allow from trusted_IP_address to any port 5672
```
Please replace the 'trusted_IP_address' with the IP address of the trusted entity.


### Step 4: User Credential Management
Never use default credentials, create a strong password and change them regularly. Reverse proxy could be used to enable more restrictive authentication and permissions checks.

```bash
# To add user
rabbitmqctl add_user username strong_password

# To set user tags
rabbitmqctl set_user_tags username administrator

# To set permissions
rabbitmqctl set_permissions -p / username ".*" ".*" ".*"
```