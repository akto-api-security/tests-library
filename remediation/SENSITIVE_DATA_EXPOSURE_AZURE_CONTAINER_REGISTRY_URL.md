

## Remediation Steps for Azure Container Registry Sensitive Data Exposure

Sensitive data exposure for Azure Container Registry URL is a serious security risk. This vulnerability can cause unauthorized access, data leaks, and may end up compromising your entire cloud environment. Follow the steps mentioned below to secure your Azure Container Registry.

### Step 1: Use Private Link for Azure Container Registry

By default, when you push or pull images to/from Azure Container Registry, these requests can be made over the public network. By enabling Private Link, you reduce your exposure to threats on the public Internet.

```bash
az network private-endpoint create --name myPrivateEndpoint \
                                   --resource-group myResourceGroup \
                                   --vnet-name myVNet \
                                   --subnet mySubnet \
                                   --private-connection-resource-id $(az acr show --name myContainerRegistry --query id --output tsv) \
                                   --group-id registry
```

### Step 2: Enable Content Trust in Docker

By enabling Docker content trust, you validate the integrity of the images that you are pulling and pushing which will prevent unauthorized or compromised images from being used.

```bash
export DOCKER_CONTENT_TRUST=1
```

### Step 3: Use Role-Based Access Control (RBAC) for Azure Container Registry

Applying RBAC permissions ensures that only authorized users can access your Azure Container Registry. Use Azure CLI to grant access to a user.

```bash
# Assign the role to a user
az role assignment create --assignee userAssignedIdentityId --role Reader --scope $(az acr show --name myAcr --query "id" --output tsv)
```


### Step 4: Create Immutable Tags

Creating immutable tags ensure that an image tag cannot be overwritten with a new and possibly harmful image. By enforcing this at the registry level, you assist in preventing malicious activity.

```bash
az acr config content-trust update --status Enabled --registry myacr
```