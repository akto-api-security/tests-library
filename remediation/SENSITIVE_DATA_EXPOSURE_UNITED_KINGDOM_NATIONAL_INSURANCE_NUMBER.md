# Remediation for SENSITIVE_DATA_EXPOSURE_UNITED_KINGDOM_NATIONAL_INSURANCE_NUMBER

## Remediation Steps for Sensitive Data Exposure - UK National Insurance Number

Sensitive data exposure of UK National Insurance Numbers would have huge legal consequences because this data is highly sensitive purpose-specific identification. Encrypting the NI numbers would be an essential remediation step to avoid any malicious activity.

Here is a simplified solution coded in Python that uses AES (Advanced Encryption Standard) for encrypting NI numbers.

### Step 1: Install required packages
Python comes with built-in support for many cryptographic algorithms. However, `pycryptodome` is a powerful library that we will use to demonstrate AES encryption.

```bash
pip install pycryptodome
```

### Step 2: Encrypt the NI Numbers
Use AES for encryption, store keys securely.

```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_NI(ni_number, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(ni_number.encode('utf-8'))
    return (nonce, ciphertext, tag)

key = get_random_bytes(AES.block_size)
```

Encrypt a NI number with the function `encrypt_NI()` and the key.

```python
ni_number = 'AB123456C'  # Replace with actual NI number
nonce, ciphertext, tag = encrypt_NI(ni_number, key)
```

### Step 3: Decrypt the NI Numbers

Create a separate function to decrypt the NI numbers when you need them.

```python
def decrypt_NI(nonce, ciphertext, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('utf-8')
    except ValueError:
        return "Key incorrect or message corrupted"

# Decrypt a NI number with the function `decrypt_NI()` and the key.
decrypted_ni_number = decrypt_NI(nonce, ciphertext, tag, key)
```
