# Remediation for BOLA_ACCESS_SYS_RESOURCE_DELETE

## Remediation Steps for File System Resource Retrieval: Exploiting BOLA through Direct Parameter Value Manipulation for DELETE based APIs

The File System Resource Retrieval issue related to parameter manipulation is a major security risk. If unchecked, an intruder may exploit this vulnerability to manipulate or delete data in a manner unintended by the API.

The remediation steps are language agnostic and mostly pertain to API design and the supporting logic but we can outline an example using Node.js and Express.js.

### Step 1: Parameter Verification
Ensure parameters are verified on the server before being used to handle file resources. This can be applied for all CRUD operations (Create, Read, Update, Delete) APIs.

For an example Delete endpoint in Node.js with Express:

```javascript
// This is a way to manipulate direct parameters value in DELETE method.
router.delete('/:id', (req, res) => {
   const id = req.params.id;
   if (!isValidID(id)) {
     return res.status(400).send('Invalid ID');
   }
   // Deletion logic...
})
```

Essentially, you check whether the 'id' parameter is valid before proceeding through the delete procedure.

### Step 2: Verify User Permissions
Ensure that each operation is tied to permissions that the user has been granted.

```javascript
router.delete('/:id', (req, res) => {
  const id = req.params.id;
  if (!isValidID(id)) {
    return res.status(400).send('Invalid ID');
  }
  if (!userHasPermission(req.user, 'delete')) {
    return res.status(403).send('User does not have required permissions');
  }
  // Deletion logic...
});
```

### Step 3: Database Transaction
On DELETE API endpoints, ensure the deletion is done in the context of a transaction. Any error in database operations should lead to transaction rollback, preventing any partial changes.

```javascript
router.delete('/:id', async (req, res) => {
  const id = req.params.id;
  if (!isValidID(id)) {
    return res.status(400).send('Invalid ID');
  }
  if (!userHasPermission(req.user, 'delete')) {
    return res.status(403).send('User does not have required permissions');
  }

  let transaction;
  try {
    transaction = await sequelize.transaction();
    // Deletion logic...
    await Model.destroy({ where: { id } }, { transaction });
    await transaction.commit();
    res.send('Item deleted');
  } catch (error) {
    if (transaction) await transaction.rollback();
    res.status(500).send('Error deleting item');
  }
});
```
These steps can mitigate the risk associated with exploiting BOLA (Broken Object Level Authorization) through Direct Parameter Value Manipulation for DELETE based APIs.