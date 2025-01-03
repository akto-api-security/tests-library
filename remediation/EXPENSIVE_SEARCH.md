# Remediation for EXPENSIVE_SEARCH

## Remediation Steps for Denial of Service Attacks on Endpoint Search Fields
Denial of Service attacks by entering long strings in the search field of an endpoint is a common security issue. Attackers use this method to overwhelm the system with extensive data requests, rendering it unavailable for use.
Follow the below steps to mitigate this issue.

### Step 1: Input Validation
Invalidate or sanitize any unexpected input before processing. This can be done through `express-validator` for Node.js:

```javascript
const { check, validationResult } = require('express-validator');

app.post('/search', [
  // Validate length of the input field
  check('searchInput', 'Search input is too long.').isLength({ max: 500 })
], (req, res) => {
  // Finds the validation errors in this request and wraps them in an object with handy functions
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }
  // Continue with your function here
});
```
### Step 2: Limit Rate of Requests
Implement rate limiting to control the number of search requests an IP, session or user can make during a specific period

For Node.js, we can use the `express-rate-limit`:

```javascript
const rateLimit = require("express-rate-limit");

const limiter = rateLimit({
 max: 100, // limit each IP request per windowMs
 windowMs: 60 * 60 * 1000, // 1 Hour
 message: 'Too many request from this IP, please try again after an hour'
});

app.use('/search', limiter); // Apply to 'search' endpoint
```
### Step 3: Add Timeout to Requests
Limits on the amount of time a request can spend in your system will help you control resource usage:

```javascript
const timeout = require('connect-timeout'); 

app.use('/search', timeout('5s'), (req, res, next) => {
 // will end request if it hangs for longer than 5 seconds
});
```

These strategies should help safeguard your system's search functionality against potential Denial of Service attacks.