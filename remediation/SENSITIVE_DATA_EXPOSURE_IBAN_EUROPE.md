# Remediation for SENSITIVE_DATA_EXPOSURE_IBAN_EUROPE

## Remediation Steps for Sensitive Data Exposure of IBAN EUROPE
Sensitive data exposures happen when an application does not adequately protect sensitive information. For IBAN in Europe, this is typically in the form of improper encryption or protection of financial or personal user data.
### Step 1: Use Strong Cryptography for Data at Rest
IBAN and any personal data should be stored with strong encryption.
```java
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

String initVector = "randomKey12345678"; // for example
String key = "SecureKey12345678";
IvParameterSpec ivspec = new IvParameterSpec(initVector.getBytes());
SecretKeySpec keyspec = new SecretKeySpec(key.getBytes(), "AES");
Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
cipher.init(Cipher.ENCRYPT_MODE, keyspec, ivspec);
byte[] encrypted = cipher.doFinal(iban.getBytes());
```
### Step 2: Secure Transmissions with HTTPS
All communication channels sending sensitive data including IBANs should be protected with HTTPS.
```java
URL url = new URL("https://secure-site.com/");
HttpURLConnection conn = (HttpURLConnection)url.openConnection();
// always verify the host - dont check for certificate
conn.setHostnameVerifier((hostname, session) -> hostname.equals("secure-site.com"));
```
### Step 3: Use Masked Inputs for Sensitive Data in UI
In the user interface, sensitive data inputs like IBAN should be masked to protect from shoulder surfing.
```html
<!-- in html -->
<input type="password" id="iban" name="iban">
```
