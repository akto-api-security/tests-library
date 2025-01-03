# Remediation for GRAPHQL_DOS_CIRCULAR_QUERY_DEFAULT_OBJECT

## Remediation Steps for Denial of Service Test on GraphQL API with Circular Query
A circular query presents recursive or endlessly repeating data structures and can be used in an attack to cause Denial of Service (DoS) by overloading the server's memory and CPU resources. The following steps will help you mitigate this issue by limiting the depth and complexity of GraphQL queries.
### Step 1: Limit Maximum Depth of GraphQL Queries
To stop processing deeply nested queries which may potentially lead to a Denial-of-Service attack, define a maximum query depth limit.
```javascript
const { createComplexityLimitRule } = require('graphql-validation-complexity');

const rules = [
  createComplexityLimitRule(maxDepth, {
    onCost: cost => console.log('query cost: ', cost),
  }),
];

app.use('/graphql', graphqlHTTP({
  schema,
  validationRules: rules,
}));
```
### Step 2: Limit Query Complexity
The complexity of a query essentially signifies the computational resources needed by the server to resolve a query, taking into consideration aspects like nesting level and number of queried elements.

```javascript
const { createComplexityLimitRule } = require('graphql-validation-complexity');
// define max complexity
const maxComplexity = 1000;

app.use('/graphql', graphqlHTTP({
  schema,
  validationRules: [createComplexityLimitRule(maxComplexity)],
}));
```
### Step 3: Persistent Queries
Using persistent queries can avoid potential Denial of Service attacks which could be triggered by sending large and complex queries to your GraphQL server. Instead of sending the full query string, the client sends a generated ID to represent the query.
```javascript
const { persistedQueries } = require('apollo-server');

const app = new ApolloServer({
  schema,
  persistedQueries,
});
```
### Step 4: Regular Audit and Update
Ensure that you apply regular updates to your server and any dependencies to have the latest security patches and improvements.