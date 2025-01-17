

## Remediation Steps for Bypass Minimum Order Quantity Requirements to Exploit Free Add-Ons

Bypassing minimum order quantity requirements to exploit free add-ons is a critical e-commerce vulnerability. This loophole allows malicious users to exploit the system by placing orders without reaching the required minimum quantity, thereby securing free add-ons without fair exchange. 

### Step 1: Validate Orders on Server-Side
Always validate order at the back-end side. Do not rely just on the client-side validation. Server-side validation is more secure and must be used in addition to client-side validation.

Here is an example using PHP:

```php
<?php
  function validate_order($order) {
    $min_order_quantity = 5; // set your minimum order quantity
    
    if ($order->quantity < $min_order_quantity) {
        throw new Exception("Minimum order quantity is $min_order_quantity");
    }
  }
?>
```

### Step 2: Add Constraints to Database
If using a relational database like PostgreSQL or MySQL, add constraints to the orders table to enforce the minimum order quantity at the database level.

Here is an example using PostgreSQL:

```sql
ALTER TABLE orders ADD CONSTRAINT check_quantity CHECK (quantity >= 5);
```
This statement sets a constraint that ensures quantity cannot be less than 5.