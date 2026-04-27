

## Remediation Steps for Mass Assignment Test for GraphQL APIs

Mass Assignment can allow a malicious user to attempt to update all attributes of an object, which can cause serious security issues. GraphQL APIs are very susceptible to this. Here are the steps to remediate the same.

### Step 1: Update Your GraphQL Schema

You must explicitly define which fields are available for mass assignment in your GraphQL API. To attain this, you need to update your GraphQL schema by mentioning the fields that can be mutable in the API.

```bash
const typeDefs = `
  type Mutation {
    updateNoSensitiveInfoUser(id: ID!, name: String, email: String): User
  }
  type User {
    id: ID!
    name: String!
    email: String!
  }
`;
```
In this example, only the 'name' and 'email' fields of the 'User' are allowed to be updated, effectively preventing any unauthorized mass assignment.

### Step 2: Data Validation

Ensure you have proper input validation in place to prevent mass assignment vulnerability. In the resolvers, you can add logic to validate the fields before updating the data.

```bash
const resolvers = {
 Mutation: {
   updateNoSensitiveInfoUser: (parent, args, context, info) => {
     //Validate args here
     return context.db.updateUser(args);
   },
 },
};
```
In the above example, 'args' are validated before being passed to the 'updateUser' function.

### Step 3: Regular Audit and Update of your GraphQL API

You should regularly audit and update your API to ensure that no fields that shouldn’t be open to mass assignment are being unintentionally exposed.

```bash
const typeDefs = /* GraphQL */ `
      type AggregatePost {
        count: Int!
      }
  `;
```
With this Aggregate type you can perform audits of your posts easily.