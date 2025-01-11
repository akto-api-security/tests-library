# Remediation for CONFIG_RUBY

## Remediation Steps for Config Ruby File Disclosure
Config Ruby File Disclosure is a serious security issue that can lead to a disclosure of sensitive information, which an attacker can use to get unauthorized access to your system.

### Step 1: Restricting access to configuration files
Restrict access to your application's configuration files. Do not expose them in your application's public directory or through a publicly accessible URL. Here is a sample .htaccess file to restrict access.

```bash
<Files ~ "^.*\.config.rb">
    Order allow,deny
    Deny from all
</Files>
```

### Step 2: Securing sensitive data in configuration files
Encrypt sensitive data in your configuration files. The attr_encrypted gem can be used to encrypt and decrypt data in Ruby.

```ruby
gem 'attr_encrypted'
```
After adding 'attr_encrypted' to your Gemfile, define the attributes that need to be encrypted and specify a key.

```ruby
class User < ActiveRecord::Base
  attr_encrypted :ssn, key: 'This is a key that is 256 bits!!'
end
```
### Step 3: Environment Separation
Split the configuration files by environments (development, production, etc.) to minimize the impact if one environment is compromised.

```ruby
# config/initializers/secret_token.rb
YourApp::Application.config.secret_key_base = if Rails.env.development? or Rails.env.test? # generate simple key for test and development environments
  ('a' * 30) # should be at least 30 chars long
else
  ENV['SECRET_TOKEN']
end
```
In production environment, store sensitive data in environment variables:

```bash
export SECRET_TOKEN=your_secret_token
```