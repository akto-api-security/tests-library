# Remediation for GRAPHQL_DOS_QUERY_DEPTH_CHECK

## Remediation Steps for Denial of Service Attack on GraphQL API with Deeply Nested Query

A Denial of Service (DoS) attack on a GraphQL API with deeply nested queries potentially causes significant server load and performance issues. To mitigate this security risk, limit the query depth and complexity.

### Step 1: Limit GraphQL Query Depth

Try implementing a simple depth limit for your GraphQL queries. This can be done using various GraphQL libraries like graphql-depth-limit for JavaScript.

Here's an example using NodeJS:

```javascript
const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const { createComplexityLimitRule } = require('graphql-validation-complexity');
const depthLimit = require('graphql-depth-limit');

const app = express();

app.use('/graphql', graphqlHTTP({
  schema: MyGraphQLSchema,
  validationRules: [
    depthLimit(5) // maximum query depth 
  ]
}));

app.listen(3000);
```

### Step 2: Limit Query Complexity

To limit the impact of complex queries on your server, you can put a limit on the complexity. This can be done using the `graphql-validation-complexity` library. 

```javascript
const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const { createComplexityLimitRule } = require('graphql-validation-complexity');

const app = express();

app.use('/graphql', graphqlHTTP({
  schema: MyGraphQLSchema,
  validationRules: [
    createComplexityLimitRule(1000) // maximum query complexity 
  ]
}));

app.listen(3000);
```

### Step 3: Regular Monitoring and Update

Regularly monitor your server logs for unusual or abnormally sized queries. Add updates accordingly to your GraphQL API to prevent further exploitation of this vulnerability.

```bash
sudo service graphqlapi restart
```
Remember, it's important to strike a balance between protective measures and providing a useful, flexible API for your users.