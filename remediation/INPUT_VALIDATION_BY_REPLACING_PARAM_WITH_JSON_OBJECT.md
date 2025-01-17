

## Remediation Steps for Input Validation by Replacing Param with JSON Object

Input validation issues arise when an application does not correctly check input data before it is processed. This can result in serious security vulnerabilities, like SQL injection or remote code execution.

Here are the remediation steps to solve this problem in a general application, let's consider a Node.js application using Express.js as framework and Joi as a validation library.

### Step 1: Install Joi
First, you need to install Joi in your application. You can do this by running the following command:

```bash
npm install @hapi/joi
```

### Step 2: Validate Input Data
Now that you have Joi installed, you need to create your validation schema and use this to validate your input data:

```javascript
const Joi = require('@hapi/joi')

const schema = Joi.object({
    name: Joi.string().min(3).required(),
    age: Joi.number().integer().min(0).required(),
});

app.post('/api/users', (req, res, next) => {
    const {error} = schema.validate(req.body);
    if(error){
        res.status(400);
        return next(new Error('Invalid data', 400));
    }
    
    // Further processing...
 });
```

In the example above, we have a JSON object that must have a `name` and `age` property, if the parameters do not meet the requirements an error response is returned.