# Remediation for SENSITIVE_DATA_EXPOSURE_SSN

## Remediation Steps for Sensitive Data Exposure - SSN

Exposing sensitive personal data like Social Security Numbers (SSNs) is a crucial security issue that could cause significant harm, including identity theft and financial loss. To prevent sensitive data exposure, we should encrypt our sensitive data at rest and in transit.

### Step 1: Encryption at Rest

Ensure SSNs are encrypted in your database. Possibly using AES-256 encryption which provides a high level of security.

If you are using a language like Python, you can use PyCryptodome, a library that provides cryptographic recipes and primitives.

Here's an example using Python:

```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b"This is your SSN"      
key = get_random_bytes(32)

cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

# Store ciphertext, tag, nonce, key securely
```

### Step 2: Encrypt Data in Transit

Use SSL/TLS encryption when data is transmitted over networks. In web applications, you can enforce HTTPS.

### Step 3: Implement Proper Access Control

Ensure that only authorized users have access to SSNs. Define proper user roles and permissions.

### Step 4: Use Masking Techniques

Mask SSNs when displaying it to the user. In general, only the last four digits of SSN are displayed (for example, XXX-XX-6789).

```python
def mask_ssn(ssn):
   masked = "XXX-XX-" + ssn.split('-')[2]
   return masked

ssn = "123-45-6789"
masked_ssn = mask_ssn(ssn)
```