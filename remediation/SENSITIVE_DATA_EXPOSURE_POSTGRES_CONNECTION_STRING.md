

## Remediation Steps for Postgres Connection String Exposure

Exposing the Postgres Connection String reveals sensitive data like username, password, and host information which can be misused by attackers to gain unauthorized access to the database. Therefore, it is vital to ensure that the Connection String isn't publicly exposed.

### Step 1: Don't Hardcode Connection Strings

Sensitive data like Connection Strings should not be hardcoded into the application's source code.

Here is an example in Python using psycopg2:

```python
import psycopg2
import os

def connect():
    connection = psycopg2.connect(
        dbname = os.getenv('DB_NAME'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASS'),
        host = os.getenv('DB_HOST')
    )
    return connection
```

In the example above, the Postgres connection string's parameters are fetched from environment variables instead of being hardcoded. 

### Step 2: Use Environment Variables

Environment variables can be used to store sensitive data such as the Connection String.

If you're using a .env file to store these variables, ensure that it's added to your .gitignore file so it doesn't end up in source control.

### Step 3: Use a Secrets Manager

For an additional act of security, consider using a Secrets Manager like AWS Secrets Manager, Azure Key Vault, or HashiCorp Vault. These tools provide a secure way to store, manage, and retrieve sensitive data.

Here is an example in Python of how to access secrets from AWS Secrets Manager:

```python
import boto3
import base64
from botocore.exceptions import BotoCoreError, ClientError

def get_secret():
    secret_name = "MySecretName"
    region_name = "us-west-2"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise Exception("Couldn't retrieve the secret.")
    
    else:
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            secret = base64.b64decode(get_secret_value_response['SecretBinary'])

    return secret
```