# Remediation for SENSITIVE_DATA_EXPOSURE_AZURE_SEARCH_QUERY_KEY_URL

## Remediation Steps for Azure Search Query Key URL Sensitive Data Exposure

Sensitive data exposure via Azure Search query key URL could result in unauthorized access and data breaches. Therefore, it's essential to lock down this vulnerability.

### Step 1: Remove the Query Key from URL

First, sensitive data such as the query key should never be exposed in the URL. Modify the existing source code to remove the key from the URL.

In Python, the modified code to call the Azure Search service without exposing the key in the URL may look like:

```python
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

endpoint = "https://your-service-name.search.windows.net"
credential = AzureKeyCredential("<your-query-key>")

search_client = SearchClient(endpoint=endpoint, index_name="your-index-name", credential=credential)

results = search_client.search("your-search-term")
```

### Step 2: Secure the Key

Use environment variables to store sensitive data such as keys, passwords and connection strings. Always secure them and avoid hard coding in your source files.

```python
import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

endpoint = "https://your-service-name.search.windows.net"
key = os.getenv("AZURE_SEARCH_QUERY_KEY")

credential = AzureKeyCredential(key)

search_client = SearchClient(endpoint=endpoint, index_name="your-index-name", credential=credential)

results = search_client.search("your-search-term")
```

### Step 3: Use HTTPS 

Make sure you're using secure HTTP (HTTPS) for all communications between your app and Azure Search.