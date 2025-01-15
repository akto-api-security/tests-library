# Remediation for HTTP_RESPONSE_SPLITTING

## Remediation Steps for HTTP Response Splitting using CRLF

HTTP Response Splitting vulnerability allows an attacker to inject malicious headers or contents into the HTTP response by splitting the response into two parts using CRLF characters. Here are remediation steps using input-validation approach to prevent this vulnerability using Python's String replace function.
        
### Step 1: Identify where user input is included in HTTP responses

Audit your code to find any location where you are including user input in HTTP headers or where you're building HTTP responses manually. 

```python 
response = HttpResponse()
response['Custom-Header'] = user_input
return response
```

### Step 2: Sanitize user input

Sanitize the user input to remove or replace any CRLF characters. 

```python 
def sanitize_input(input_string):
    return input_string.replace('\n', '').replace('\r', '')

    sanitized_user_input = sanitize_input(user_input)

response = HttpResponse()
response['Custom-Header'] = sanitized_user_input
return response
```

### Step 3: Audit and test

Auditing and testing is an important aspect of mitigating such security vulnerability. It's good practice to test for security holes before code is pushed live.

```python
#This is a testing step/unit test to ensure the code is working as expected.

def test_sanitize_input():
    assert sanitize_input("test\ninput") == "testinput"
    assert sanitize_input("test\r\ninput") == "testinput"
    assert sanitize_input("test\rinput") == "testinput"
```