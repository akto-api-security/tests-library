

## Remediation Steps for Hash Disclosure

Hash disclosure refers to when a system unintentionally discloses sensitive hashed data which could potentially be brute-forced, leading to confidentiality breach. The following steps provide a guide to remedy a hash disclosure vulnerability.

### Step 1: Identify the exposure point
The primary step is to identify where hashing occurs in the system and where these hashes are being incorrectly stored or disclosed.

```bash
grep -r 'hash(' .
grep -r 'md5(' .
grep -r 'sha1(' .
```

### Step 2: Use safer hash functions
Switch to more secure hash functions such as `bcrypt`, `scrypt`,  or `Argon2` instead of weaker hashing functions like `md5`.

#### Example in PHP:
```php
$hashedPassword = password_hash($password, PASSWORD_BCRYPT);
```

### Step 3: Use hash with Salt
Add unique random salt value to each password before hashing. Salting makes it extremely difficult for an attacker to use pre-computed tables to crack the password.

#### PHP example:

```php
$options = [
    'cost' => 12,
];
$hashedPassword = password_hash($password, PASSWORD_BCRYPT, $options);
```

### Step 4: Do not expose hashes
Prevent any form of hash disclosure, for instance, from error messages or URL parameters.

#### PHP example:

```php
try {
    // hashing and storing password
} catch (Exception $e) {
    echo 'An error occurred. Please try again.';
}
```