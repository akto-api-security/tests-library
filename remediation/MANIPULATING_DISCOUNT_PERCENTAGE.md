# Remediation for MANIPULATING_DISCOUNT_PERCENTAGE

## Remediation Steps for Manipulating Discount Percentage
Manipulating discount percentage is a substantive security issue. Without proper validation on the server-side, attackers are able to manipulate client-side JavaScript and modify the discount percentage on products. This can result in revenue loss. 

Below are a few steps that can be taken to remedy this issue:

### Step 1: Validate and Sanitize Input Data
Ensure that all input data are validated and sanitized on the server side. Never trust client-side input validation as it can be easily bypassed.

For example in a Python Flask application, such could be done as follows:
```python
from flask import Flask, request 
app = Flask(__name__)

@app.route('/apply_discount', methods=['POST'])
def apply_discount():
    try:
        discount_percentage = float(request.form.get('discount_percentage')

        if not 0 <= discount_percentage <= 100:
            return "Invalid discount percentage", 400
        else:
            # Apply the discount
            pass

    except ValueError:
        return "Invalid discount percentage", 400
```

### Step 2: Use Parameterized Queries or Prepared Statements
This restriction will assist in the prevention of SQL Injections. Here is an example using PHP with MySQLi:

```php
$stmt = $conn->prepare("UPDATE Products SET Price=Price*(1-?) WHERE ProductID=?");
$stmt->bind_param("di", $discountPercentage, $productID);
$stmt->execute();
```

### Step 3: Implement Strict Access Controls
Access to features and functions that could potentially be exploited, like modifying discounts, should have strict access controls that limit who and what can modify these entities.

### Step 4: Regular Audit and Update
Frequently update and audit your systems and applications for any vulnerabilities or system glitches. Automated testing can be a useful tool in this regard.