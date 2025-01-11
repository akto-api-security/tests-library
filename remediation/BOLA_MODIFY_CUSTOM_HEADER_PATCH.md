# Remediation for BOLA_MODIFY_CUSTOM_HEADER_PATCH

## Remediation Steps for BOLA Exploitation by Fuzzing Custom Header 

BOLA (Broken Object Level Authorization) issue occurs when users manipulate references to identifiers related to other external objects exposed by the system. On exploitation, it might lead to unauthorized access of data. Below mentioned are the steps to prevent the exploitation:

### Step 1: Strengthen Server-Side Access Control
Implement robust server-side access control checks for all PATCH/PUT requests. The code snippet below is an example in NodeJS.

```javascript
app.patch('/api/resource/:id', (req, res) => {
  var user = getUserFromToken(req.headers.authorization);
  var id = req.params.id;

  Resource.findById(id, (err, resource) => {
    if (err) {
      res.status(500).send(err);
    } else {
      if (resource.userId !== user.id) {
        res.status(403).send('Not allowed to access this resource');
      } else {
        // update the resource
      }
    }
  });
});
```

### Step 2: Input Validation
Validate custom headers and request parameters to ensure that unauthorized inputs cannot be processed. The code snippet below is an example in Python.

```python
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/api/resource', methods=['PUT', 'PATCH'])
def update_resource():
    if 'Custom-Header' in request.headers:
        custom_header = request.headers.get('Custom-Header')
        if not validate_custom_header(custom_header):
            abort(400, description="Invalid request")
        else:
            # proceed with updating the resource
            pass
    else:
        abort(400, description="Custom-Header missing in request")
        
def validate_custom_header(custom_header):
    # replace with actual validation logic
    return True
```