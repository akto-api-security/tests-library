

## Remediation Steps for Unauthenticated Mutation Query in GraphQL
Unauthenticated Mutation Query in GraphQL can be a serious security vulnerability. If not properly managed, malicious actors may perform unauthorized operations or mutate data, creating inconsistencies in the system.

### Step 1: Implement Authorization Middleware
First step is to add an authorization middleware that checks if a user is authenticated before any requests are processed. The following JavaScript code snippet implements an authentication middleware for a GraphQL server using express-graphql library and JWT for handling authentication.

```javascript
const { verify } = require('jsonwebtoken');
const { AuthenticationError } = require('apollo-server');

const authMiddleware = async (req, res, next) => {
  const authHeader = req.get('Authorization');
  if(!authHeader){
    req.isAuth = false;
    return next();
  }
  
  const token = authHeader.split(' ')[1];
  if(!token || token === ''){
    req.isAuth = false;
    return next();
  }
  
  try {
    const decodedToken = verify(token, 'YOUR_SECRET_KEY');
    if(!decodedToken){
      req.isAuth = false;
      return next();
    }
    req.isAuth = true;
    req.userId = decodedToken.userId;
    next();
  } 
  catch(err) {
    req.isAuth = false;
    return next();
  }
}

module.exports = authMiddleware;
```
You should replace 'YOUR_SECRET_KEY' with your actual secret key.

### Step 2: Apply Middleware to GraphQL Server
After creating the authentication middleware, apply it to your GraphQL server.

```javascript
const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const authMiddleware = require('./authMiddleware');
const schema = require('./schema');

const app = express();

app.use(authMiddleware);
app.use('/graphql', graphqlHTTP({
  schema: schema,
  graphiql: true,
}));

app.listen(4000);
```

### Step 3: Protect GraphQL Mutations
Finally, we need to ensure that our GraphQL mutations verify if the user is authenticated before performing any operation. 

```javascript
const { UserInputError, AuthenticationError } = require('apollo-server');

const Mutation = new GraphQLObjectType({
  name: 'Mutation',
  fields: {
    addPost: {
      type: PostType,
      args: { /*...args*/ },

      resolve(parentValue, args, request){
        if (!request.isAuth) {
          throw new AuthenticationError('Not authenticated');
        }

        // perform mutation operation
      }
    }
  }
});
```

In the `resolve` method, we check if `request.isAuth` is `true`. If not, an `AuthenticationError` is thrown.

By enforcing these steps, you can mitigate the risk of unauthenticated mutation queries in GraphQL.