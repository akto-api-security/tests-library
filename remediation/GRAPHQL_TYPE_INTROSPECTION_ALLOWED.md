

## Remediation Steps for Graphql Type Introspection Allowed

The ability to perform type introspection in GraphQL may leak important API information. Squashing this vulnerability involves specifically disabling the introspection feature to eliminate the risk of potential information exposure.

### Step 1: Disable Introspection In Apollo Server
If you're using Apollo Server, you can disable introspection in the production environment as follows:
```javascript
const server = new ApolloServer({ 
    typeDefs, 
    resolvers,
    introspection: process.env.NODE_ENV === 'development',
});
```
In the above configuration, introspection is allowed only during development. 

### Step 2: Apply Introspection Middleware
For Express-GraphQL Server, apply a middleware to check for the introspection query, disabling it when in a production environment.
```javascript
app.use('/graphql', (req, res, next) => {
    if (req.body.hasOwnProperty('operationName') && 
        req.body.operationName === "IntrospectionQuery") {
        if(process.env.NODE_ENV == 'production'){
            console.log('Blocked introspection in production');
            res.status(403).end('Graphql introspection not allowed');
        }else{
            next();
        }
    } else {
        next();
    }
}, graphqlHTTP({schema: MyGraphQLSchema}));
```
