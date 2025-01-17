

## Remediation Steps for Sensitive Data Exposure in Heroku

Sensitive data exposure is a significant security issue. In case of Heroku, it can occur due to improper configuration of Heroku's environment variables or exposure of source code repositories. It's crucial to protect your sensitive data from unauthorized access.

### Step 1: Use Environment Variables for Storing Sensitive Data

Heroku allows us to define configuration variables within the application. These variables should be utilized to store any sensitive data instead of hard coding within the application.

In Python, you can use the `os` module to access these variables.

```python
import os
secret_data = os.environ['SECRET_DATA']
```

To set these variables in Heroku, you can use the Heroku CLI with the following command:

```bash
heroku config:set SECRET_DATA=sensitiveInformationHere
```

### Step 2: Setup GitIgnore to Exclude Sensitive Files

Some files like `.env` where sensitive data might be stored should not be included in the git repository. To exclude these files, include them to your `.gitignore`.

```bash
echo '.env' >> .gitignore
```

### Step 3: Setup SSL for Data in Transit

All the data in transit should be encrypted. Heroku provides Automated Certificate Management (ACM), which can be enabled with the following command:

```bash
heroku certs:auto:enable
```


### Step 4: Protect Heroku Authentication

Use a strong password and two-factor authentication for your Heroku account. Use the following command to enable two-factor authentication:

```bash
heroku 2fa
```