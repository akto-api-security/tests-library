const { ApolloClient, InMemoryCache, HttpLink } = require('@apollo/client');
const { gql } = require('graphql-tag');

const testConfig = require('./test-config.yml');

const { api_endpoint, test_data } = testConfig.common_config;
const { object_name, keys_to_add } = testConfig.test_data;

const client = new ApolloClient({
  link: new HttpLink({ uri: api_endpoint }),
  cache: new InMemoryCache(),
});

describe('GraphQL API Tests', () => {
  it('should create an object, add keys, and verify', async () => {
    const createObjectMutation = gql`
      mutation CreateObject($input: ObjectInput!) {
        createObject(input: $input) {
          id
          name
        }
      }
    `;

    const createObjectVariables = {
      input: {
        name: object_name,
      },
    };

    const createObjectResponse = await client.mutate({
      mutation: createObjectMutation,
      variables: createObjectVariables,
    });

    expect(createObjectResponse.data.createObject.id).toBeDefined();

    const addObjectKeysMutation = gql`
      mutation AddKeysToObject($objectId: ID!, $keys: [String!]!) {
        addKeysToObject(objectId: $objectId, keys: $keys) {
          success
        }
      }
    `;

    const objectId = createObjectResponse.data.createObject.id;

    const addObjectKeysVariables = {
      objectId,
      keys: keys_to_add,
    };

    const addObjectKeysResponse = await client.mutate({
      mutation: addObjectKeysMutation,
      variables: addObjectKeysVariables,
    });

    expect(addObjectKeysResponse.data.addKeysToObject.success).toBe(true);

    const queryObjectWithKeys = gql`
      query GetObjectWithKeys($objectId: ID!) {
        getObject(id: $objectId) {
          id
          name
          keys
        }
      }
    `;

    const queryObjectWithKeysVariables = {
      objectId,
    };

    const getObjectWithKeysResponse = await client.query({
      query: queryObjectWithKeys,
      variables: queryObjectWithKeysVariables,
    });

    const objectWithKeys = getObjectWithKeysResponse.data.getObject;
    expect(objectWithKeys.keys).toEqual(expect.arrayContaining(keys_to_add));
  });
});
