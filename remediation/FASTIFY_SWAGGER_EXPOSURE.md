# Remediation for FASTIFY_SWAGGER_EXPOSURE

## Remediation Steps for Fastify Swagger UI Exposure
Fastify Swagger UI exposure is a serious security issue. Without properly securing Swagger UI, attackers may gain unauthorized access to your APIs structure and its sensitive data, potentially causing a significant compromise of your application.

### Step 1: Disable Swagger UI in Production

Depending on your environment, the first step in remediation might be simply to disable the Swagger UI in production environments.
```javascript
const fastify = require('fastify')()
const swagger = require('fastify-swagger')

// Only enable Swagger UI in non-production environments
if (process.env.NODE_ENV !== 'production') {
  fastify.register(swagger, { routePrefix: '/documentation', exposeRoute: true })
} 

fastify.get('/api', async (request, reply) => {
  // Your route logic here...
})

fastify.listen(3000, function (err) {
  if (err) {
    throw err
  }

  fastify.log.info('server listening on %s', fastify.server.address().port)
})
```

### Step 2: Implement Basic Auth

Another recommended option is to secure your API documentation with Basic Auth. This prevents unauthorized users from seeing your API structure in the Swagger UI. To implement basic authentication in Fastify, you can use `fastify-basic-auth`:

```javascript
// Enable Swagger only for authenticated users
fastify.register(require('fastify-basic-auth'), { validate })
fastify.after(() => {
  fastify.register(require('fastify-swagger'), swagger.options)
  fastify.addHook('preHandler', fastify.basicAuth)
})

async function validate (username, password, req, reply) {
  if (username !== 'foo' || password !== 'bar') {
    return new Error('Invalid credentials')
  }

  // You can also use the result of an async function here
  const customer = await Customers.findByUsername(username)
  if (!customer) {
    return new Error('Invalid credentials')
  }
}
```