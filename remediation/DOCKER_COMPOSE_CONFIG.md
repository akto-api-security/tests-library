# Remediation for DOCKER_COMPOSE_CONFIG

## Remediation Steps for Docker-Compose.yml Exposure 

Docker-Compose.yml exposure is a significant security risk. Insecure Docker Compose configurations can expose sensitive information and potentially grant unauthorized access to Docker services. Following these steps will help you secure your Docker environment.

### Step 1: Check Permissions and Ownership
Ensure the docker-compose.yml files are not world-readable or world-writable. Files should be owned by a specific user who is responsible for Docker deployment and who has appropriate permissions. The below commands change the ownership and permissions to the current user and removes all other permissions:

```bash
chown $USER:docker docker-compose.yml
chmod 0600 docker-compose.yml
```

### Step 2: Do Not Store Sensitive Data in Docker Compose Files
Avoid storing secrets or sensitive data in your docker-compose.yml files directly. Docker supports the use of secrets, which lets you store sensitive data out of the Compose file:

```bash
echo "This is a secret" | docker secret create my_secret_data -
```

Then refer to these secrets but not exposing them in the Docker Compose file:

```yaml
version: '3.1'
services:
  someservice:
    image: someservice
    secrets:
      - my_secret_data
secrets:
  my_secret_data:
    external: true
```

### Step 3: Use .env file for variables and add it to .gitignore
Store your environment variables in a separate .env file (Ensure that you include .env in your .gitignore, so it isn't added to version control):

```properties
DB_USER=user
DB_PASS=secret
```

Then refer to these variables in docker-compose file:

```yaml
version: '3.1'
services:
  db:
    image: db
    environment:
      - user=${DB_USER}
      - password=${DB_PASS}
```