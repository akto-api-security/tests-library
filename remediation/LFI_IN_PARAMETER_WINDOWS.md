# Remediation for LFI_IN_PARAMETER_WINDOWS

## Remediation Steps for Local File Inclusion (LFI) in Parameter for Windows
Local File Inclusion (LFI) exploits are a serious security issue that can potentially allow an attacker unauthorized access to files. These attacks can be avoided through the proper evaluation of file references within your application code before they're used. 

The following steps show you how to remediate this security issue:

### Step 1: Input Validation
First, validate all user inputs before processing them. This step ensures that the users are only able to interact with the application within the boundaries set by the developer.
The code snippet below demonstrates input validation in C#:

```csharp
if (Path.IsPathRooted(input) || input.Contains(".."))
{
    throw new ArgumentException();
}
string safeFileName = Path.GetFileName(input);
string fullPath = Path.Combine(knownDirectory, safeFileName);
```

### Step 2: Limit File Permissions
Ensure that your application's scripts don't run with too many permissions, especially write permissions, and avoid running them as an admin user.

### Step 3: Update File Access Function
Deprecate the use of functions like `include()`, `include_once()`, `require()` and `require_once()`, which use file names or URLs that can be manipulated by the user. 

### Step 4: Use White-Listing Approach
Limit the files that can be included in the execution scope of your application. If there is a finite list of resources that should be accessible, use a white list approach.