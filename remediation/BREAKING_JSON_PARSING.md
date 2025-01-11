# Remediation for BREAKING_JSON_PARSING

## Remediation Steps for Breaking JSON Parsing
Breaking JSON Parsing is a security vulnerability where an attacker might manipulate the data structure of the JSON objects, and if not properly validated, can compromise the application's data flow.

### Step 1: Use JSON.parse
The `JSON.parse` method is a safe way to handle JSON strings. It converts a JSON string into a JavaScript object. If the input is not a valid JSON string, it will throw an error.

```javascript
try {
    var data = JSON.parse(input);
} catch (error) {
    console.error("Invalid JSON input: ", error);
}
```
### Step 2: Validate JSON Schema
Always validate JSON schema before further processing of the parsed object.
Use libraries like `ajv` to define and validate JSON schema.

```javascript
const Ajv = require('ajv');
const ajv = new Ajv();

const schema = {
    type: 'object',
    properties: {
        name: {type: 'string'},
        age: {type: 'number'}
    },
    required: ['name', 'age'],
    additionalProperties: false
};

function validate(data) {
    const valid = ajv.validate(schema, data);
    if (!valid) console.error(ajv.errors);
};

validate(data);
```
### Step 3: Use Parameterized Queries
To protect against Injection attacks, use parameterized queries while interacting with databases.

```javascript
const text = 'INSERT INTO users(name, age) VALUES($1, $2)';
const values = ['John', 30];

client.query(text, values, (error, result) => {
    if (error) {
        console.error('Failed to execute query', error.stack);
    } else {
        console.log(result.rows);
    }
})
```