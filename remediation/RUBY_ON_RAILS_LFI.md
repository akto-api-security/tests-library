# Remediation for RUBY_ON_RAILS_LFI

## Remediation Steps for Ruby On Rails Local File Inclusion

Local File Inclusion (LFI) in Ruby on Rails can lead to serious security breaches, giving unauthorized users access to local files and data. It commonly occurs when user-supplied input is not properly sanitized or validated.

### Step 1: Avoid Using Untrusted Data for File Names
Avoid using user-supplied data to generate file names or paths. This reduces the risk of manipulated input leading to unexpected file access.

In the context of a Rails application, that might look somethinglike:

```ruby
# NOT secure
file_to_render = params[:file]
render file: file_to_render

# More secure alternative
file_to_render = params[:file]
if ['safe_file1', 'safe_file2', 'safe_file3'].include?(file_to_render)
  render file: file_to_render
else
  # Do something else if the requested file is not allowed
end
```

### Step 2: Sanitize User Inputs
Always sanitize user inputs. Untrusted user input should never be used for file names or paths without validation.

For example,

```ruby
file_to_access = Pathname.new("/app/data/#{params[:file]}").cleanpath.to_s 
if file_to_access.start_with?('/app/data/')
  # use the file
else
  # log attempt to break out of /app/data/
end
```

### Step 3: Update Dependencies
Regularly update all dependencies, including the Rails library itself, to benefit from the latest security patches.

```bash
bundle update
```

### Step 4: Error Handling
Ensure appropriate error handling is in place for failed file access attempts, and do not reveal sensitive system information in error messages.

For example:

```ruby
begin
  # attempt to access file
rescue
  # handle error, log if necessary, and return a generic error message
  render plain: "An error occurred."
end
```