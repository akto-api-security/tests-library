

## Remediation Steps for BOLA by HTTP Parameter Pollution
Also known as Blind Object Locator Attacks, BOLA, combined with HTTP Parameter Pollution (HPP), could pave way for dangerous information leaks or manipulation of sensitive content. Let's look at ways to secure your system.

### Step 1: Sanitize Inputs
All application inputs should be sanitized and validated. Neglect could result in undesired behavior via HPP being passed to the BOLA (i.e., object identifiers).

```java
public String sanitizeInput(String input) {
  return StringEscapeUtils.escapeJava(input);
}
```

### Step 2: Enforce Parameter Integrity
The integrity of parameters should be enforced to ensure that no unwanted parameters are admitted.

```php
$allowedParams = ['param1', 'param2', 'param3'];
$actualParams = array_keys($_GET);

if (array_diff($actualParams, $allowedParams)) {
  throw new Exception('Unwanted parameter admitted!');
}
```

### Step 3: Use HTTP POST instead of GET
Use the HTTP POST method over GET where possible, as POST parameters aren't exposed in URLs, making HPP much harder.

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
  data = request.form
  # process the data
```

### Step 4: Aviation of Direct Object References
The best defense against BOLA is to avoid Actual Reference. Indirect reference maps can be used to provide access controls that do not allow direct object reference.

```javascript
var accountAccessMap = {
  'user1': ['account1', 'account2'],
  'user2': ['account3']
}

var requestedAccount = request.getParameter('account');
var currentUser = getCurrentUser();

if(accountAccessMap[currentUser].includes(requestedAccount)){
  // proceed with account access
}
```