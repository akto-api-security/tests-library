# Remediation for GRAPHQL_DEBUG_MODE_ENABLED

## Remediation Steps for Graphql Debug Mode Enabled

Having Graphql Debug Mode Enabled is a security vulnerability. It can leak vital application and environment details to attackers who can use this information to exploit the system. 

### Step 1: Determine the Developer Environment

Determine if your Graphql API is currently running in a production or development environment. Debug mode should only be used in the development environment. 

### Step 2: Disable Debug Mode

To fix this security issue, switch off the debug mode. You can achieve this by using the below code snippet. In this example, we are using Graphql with Javascript/Node.js. 

```javascript
const { graphqlHTTP } = require('express-graphql');
const { buildSchema } = require('graphql');

app.use('/graphql', graphqlHTTP({
  schema: MyGraphQLSchema,
  graphiql: false, // Set graphiql to false
}));
```
In this code, `graphiql` is set to `false`, which turns off the debug mode. 

### Step 3: Validate Changes

Validate that the debug mode has been turned off. 