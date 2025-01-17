

## Remediation Steps for Bypass Credit and Buy-Now-Pay-Later Limits in Transaction APIs
Bypassing credit and Buy-Now-Pay-Later limits in Transaction APIs poses significant security and business risks, and steps should be taken to address these vulnerabilities. The remediation strategy should focus on strengthening the server-side control, input validation, and ensuring that every transaction request is authenticated and authorized.

### Step 1: Ensure Server Side Control
Ensure that all the important validation checks are done at the server side. Assuming that validations carried out on the client-side are secure is unsafe as they can be manipulated before reaching the server.

```javascript
app.post('/api/transaction', (req, res) => {
  const userId = req.body.userId;
  const transactionAmount = req.body.transactionAmount;
  
  // Get user's credit limit and BNPL limit from the database
  getUserLimits(userId, (err, limits) => {
    if(err) {
      return res.status(500).send('Server error!');
    }
  
    /* If the transaction amount is more than the credit limit or BNPL limit, 
    the transaction should not be processed. */
    if(transactionAmount > limits.credit || transactionAmount > limits.bnpl) {
      return res.status(400).send('Transaction exceeds limits!');
    }
  
    // If checks pass, continue to process the transaction
    processTransaction(req, res);
  });
});
```

### Step 2: Input Validation
Approve only authorized and validated requests and check each entry for validation making sure it is in the correct format and within acceptable ranges.

```javascript
const Joi = require('joi');

const schema = Joi.object({
  userId: Joi.string().required(),
  transactionAmount: Joi.number().min(0).required()
});

app.post('/api/transaction', (req, res) => {
  const { error } = schema.validate(req.body);

  if(error) {
    return res.status(400).send(error.details[0].message);
  }

  processTransaction(req, res);
});
```

### Step 3: Implement User Authentication and Authorization
Information related to any transaction or user data should be accessible only to authenticated and authorized users.

```javascript
const jwt = require('jsonwebtoken');

app.post('/api/transaction', (req, res) => {
  const token = req.header('x-access-token');
  
  if (!token) {
    return res.status(401).send('Access denied. No token provided.');
  }

  try {
    const decodedPayload = jwt.verify(token, config.get('jwtPrivateKey'));
    req.user = decodedPayload;

    processTransaction(req, res);
  } catch (ex) {
    res.status(400).send('Invalid token.');
  }
});
```