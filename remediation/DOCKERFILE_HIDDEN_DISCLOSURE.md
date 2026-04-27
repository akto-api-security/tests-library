

## Remediation Steps for Dockerfile Hidden Disclosure
Dockerfile Hidden Disclosure can become a serious security issue as it could potentially expose sensitive data like passwords or API keys in the Dockerfile. The best practice is to use Docker secrets or environment variables to handle sensitive data. 

Here is how you can fix this vulnerability in a Dockerfile:

### Step 1: Remove Sensitive Data from Dockerfile

Firstly, ensure that no sensitive data is stored directly in the Dockerfile. This includes API keys, passwords, or any other sensitive data.

To check the Dockerfile, inspect the CMD, RUN and ARG entries for any such sensitive data.

For a Dockerfile looking something like this:

```Dockerfile
FROM python:3.7

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD python api.py
```

### Step 2: Use Docker Secrets or Environment Variables

Sensitive data such as passwords or API keys should not be hard-coded into the Dockerfile. They should instead be provided using Docker secrets (for Swarm mode) or environment variables:

Using Docker secrets:

```bash
printf <your sensitive data> | docker secret create my_secret -
```
Using Environment Variables:

```Dockerfile
FROM python:3.7

WORKDIR /app

COPY . .

# Do not write secrets directly in Dockerfile.
# ENV YOUR_SECRET_KEY=your-secret-key 

RUN pip install --no-cache-dir -r requirements.txt

CMD python api.py
```

To use the environment variable, you can reference it in the Dockerfile like so:

```bash
docker run -e "YOUR_SECRET_KEY=<your-secret-key>" <your-image>
```