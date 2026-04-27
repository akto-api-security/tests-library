

## Remediation Steps for BOLA JSON Parameter Vulnerability

BOLA, or Broken Object Level Authorization, is a type of application security issue where an attacker manipulates object references to gain unauthorized access to data. In this case, the JSON parameter is turned into an array for unauthorized access via DELETE method APIs. 

Here is how you can mitigate this issue:

### Step 1: Validate User Inputs
Always validate user inputs. When dealing with IDs or parameters in API calls, ensure they adhere to the expected format and type. Furthermore, use arrays instead of strings for multiple parameters to avoid unauthorized access.

The following JavaScript example shows a proper validation:

```javascript
const Joi = require('joi');

const schema = Joi.array().items(Joi.number().integer());
const { error } = schema.validate(req.body.ids);

if (error) {
    res.status(400).send("Invalid 'ids' parameter.");
}
```

### Step 2: Implement Proper Access Controls 
Implement a robust system for Access Control Lists (ACLs). You can use middleware to check if the current user is authorized to access the objects before performing any operation.

Here's an example in Express.js:

```javascript
app.use('/api/resource/:id', function(req, res, next){
  if(!req.user.hasAccess(req.params.id)){
    return res.status(403).json({error: 'Unauthorized access'});
  }
  next();
});
```

### Step 3: Patch/Delete API Endpoints Protection 
On API endpoints that perform an operation such as delete, ensure to verify object ownership before carrying out any action.

For example, you can do something like this with a mongoose model in Express.js:

```javascript
app.delete('/api/resource/:id', function(req, res, next){
  Resource.findOne({ _id: req.params.id }, function (err, resource){
    if (err) { return next(err); }

    if (resource.owner.toString() !== req.user._id.toString()){
      return res.status(403).json({error: 'Unauthorized access'});
    }

    resource.remove(function (err) {
      if (err) { return next(err); }

      res.json({ message: 'Resource deleted successfully' });
    });
  });
});
```

Follow these steps and ensure your nominated resources are correctly protected against BOLA attacks. Always check for roles, authorization, and access controls when accessing critical resources.
