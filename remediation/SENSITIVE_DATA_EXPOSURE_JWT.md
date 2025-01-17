

## Remediation Steps for Sensitive Data Exposure for JWT (JSON Web Tokens)
Sensitive data exposure for JWT means an attacker can potentially access or manipulate the information encoded in the token. Loss of confidentiality, integrity and availability can be the result of such exposure.

### Step 1: Token Signature
Always validate the token signature to ensure that it has not been tampered with.
```javascript 
var jwt = require('jsonwebtoken');
var secret = 'SECRET_KEY';  //Replace this with your secret key

var token = 'your token here'; //The JWT token that needs to be validated 

jwt.verify(token, secret, function(err, decoded) {
  if(err){
    console.log('Token has been tampered with');
  } else {
    console.log('Token is valid');
  }
});
```

### Step 2: Encrypt Sensitive Data
If the JWT contains sensitive data, it should be encrypted using the JWE standard to prevent data exposure even if an attacker can decode a token.

```javascript
const jose = require('jose')
const secret = Buffer.from('fe1a1915a379f3be645e6e3257bb3', 'hex')

const jweToken = jose.JWE.createEncrypt(secret).update('sensitive data').finalize()
console.log('JWE token: ', jweToken)
```

### Step 3: Set Expiry for Tokens
Do not set a very long validity for the tokens. It reduces the probability of an attacker gaining access to a valid token.

```javascript
var jwt = require('jsonwebtoken');
var payload = {
  data: 'foobar',
  exp: Math.floor(Date.now() / 1000) + (60 * 60) // expires in 1 hour
};
console.log(jwt.sign(payload, 'SECRET_KEY'));
```

### Step 4: Use HTTPS for transmission
Always use a secure channel (HTTPS) to send the token to the client to prevent man in the middle attacks.

No code needed as this is a server setup instruction not a code fix issue.

### Step 5: Store JWTs securely in Web Apps
If JWTs are stored insecurely in web apps they can be stolen leading to token-based attacks. Cookies with 'httpOnly' and 'secure' options should be used for storage.

```javascript
// Node.js Express example
const express = require('express');
const jwt = require('jsonwebtoken');
const cookieParser = require('cookie-parser');

let app = express();
app.use(cookieParser());

app.get('/secure', (req, res) => {
  const token = jwt.sign({ user: 'username' }, 'secret_key');
  
  res.cookie('token', token, {
    httpOnly: true,
    secure: true,
    maxAge: 60 * 60 * 1000 // 1 hour
  });

  res.send('Secure cookie has been set with JWT!');
});

app.listen(3000, () => console.log('Listening on port 3000!')); 
```