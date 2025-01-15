# Remediation for DOCKER_EXPOSED

## Remediation Steps for Docker API Exposure
Unprotected Docker APIs can result in severe security vulnerabilities if not addressed promptly. The following steps provide assistance in mitigating the exposure of Docker APIs.

### Step 1: Disable Docker Remote API
Firstly, stop the Docker service and disable the remote API by performing following commands:

```bash
sudo systemctl stop docker.service
sudo systemctl disable docker.service
```

### Step 2: Configure Docker to Use TLS
Then, enable TLS in Docker daemon. Follow these steps:

```bash
# Create a directory for Docker configurations
mkdir -pv ~/.docker

# Generate a certificate authority (CA) private and public key
openssl genrsa -out ~/.docker/ca-key.pem 4096
openssl req -new -x509 -days 365 -key ~/.docker/ca-key.pem -sha256 -out ~/.docker/ca.pem

# Start Docker daemon with TLS
dockerd --tlsverify --tlscacert=~/.docker/ca.pem --tlscert=~/.docker/cert.pem --tlskey=~/.docker/key.pem -H=0.0.0.0:2376
```

### Step 3: Configure the Firewall 
To further secure your Docker, configure your firewall:

```bash
# Block connections to Docker’s default port
sudo ufw deny from any to any port 2375
sudo ufw deny from any to any port 2376
```