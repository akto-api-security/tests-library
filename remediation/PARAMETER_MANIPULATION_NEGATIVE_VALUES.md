# Remediation for PARAMETER_MANIPULATION_NEGATIVE_VALUES

## Remediation Steps for Parameter Manipulation Using Negative Values in Transactions
Parameter manipulation using negative values in transactions is a frequent security issue, and it can lead to unwanted behavior or effect on your software. This can happen, for instance, when a user inputs a negative value in a transaction where only positive values are expected.

### Step 1: Ensure Adequate Validation
Ensure that your system is validating the input parameter correctly. If you are expecting only positive values, make sure your system is rejecting negative and decimal number inputs. Below is an example in Python:

```python
def validate_input(param):
    if param < 0:
        raise ValueError("Invalid input: Please enter a positive integer.")
    else:
        return param
```

### Step 2: Limit Input Range
You also want to ensure that the input is within the allowable range. An example of this in Java is:

```java
public int validateInput(int param) {
    if(param < 0) {
        throw new IllegalArgumentException("Invalid input: Input must be a positive integer.");
    } else {
        return param;
    }
}
```

### Step 3: Regular Database Checks
Regular database checks can help ensure that parameters are within the expected range. Remember to scrub any data that is outside that range.

```sql
DELETE FROM Transactions WHERE param < 0;
```