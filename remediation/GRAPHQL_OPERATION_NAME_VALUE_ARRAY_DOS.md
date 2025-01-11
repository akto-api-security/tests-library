# Remediation for GRAPHQL_OPERATION_NAME_VALUE_ARRAY_DOS

## Remediation Steps for Denial of Service Test on GraphQL API with Operation Name Value Array Test

DoS (Denial of Service) attacks on GraphQL APIs can effectively make a server unresponsive by overloading it with requests. A common method would be through operation name value array tests. Without proper checks and safeguards, this vulnerability could allow attackers to cause significant disruption.

### Step 1: Limit Query Complexity

You can impose a limit on the complexity of the queries that your GraphQL server will accept. This can be achieved by using GraphQL's `createComplexityLimitRule` function. A maximal depth can be set to prevent deep nesting queries that could be expensive for the server to process.

```javascript
const depthLimit = require('graphql-depth-limit')
const schema = makeExecutableSchema({ typeDefs, resolvers })

app.use(
  '/graphql',
  expressGraphql(req => ({
    schema,
    validationRules: [depthLimit(4)]
  }))
)
```

### Step 2: Query Whitelisting

Consider only allowing known operation names. An array of operation names may be provided and only these specific operations will be allowed.

```javascript
const whitelist = ['knownOperation1', 'knownOperation2'];
// validate incoming queries
// Assuming apollo server is used
app.use(server.graphqlPath, (req, res, next) => {
  const operationName = req.body.operationName;
  if (!whitelist.includes(operationName)) {
    return res.status(400).send('Invalid operation name');
  }
  next();
});
```

### Step 3: Rate Limiting

Consider enforcing rate limiting on your API. Rate limiting provides a mechanism to control user's request to the server in a time slot. There are several ways to add rate limiting, here's an example using 'express-rate-limit'.

```javascript
const rateLimit = require('express-rate-limit');
// Enable if you're behind a reverse proxy (Heroku, Bluemix, AWS ELB, Nginx, etc)
app.enable('trust proxy');
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
// only apply to requests that begin with /api/
app.use('/graphql', apiLimiter);
```