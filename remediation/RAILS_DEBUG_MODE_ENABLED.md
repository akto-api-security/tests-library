# Remediation for RAILS_DEBUG_MODE_ENABLED

## Remediation Steps for Rails Debug Mode Enabled

The Debug Mode in Rails is meant to be used in a development environment. However, when left enabled in a production environment, it can expose sensitive information about the application and the underlying system that can be used by attackers to aid them in exploiting the system.

### Step 1: Disable Debug Mode in Production

In Rails, debug mode is typically enabled in the `development.rb` configuration file. You need to ensure it's disabled in the `production.rb` configuration file. If the `debug` value is set to `true` in `production.rb`, change it to `false`.

```ruby
# config/environments/production.rb
Rails.application.configure do
  ...
  config.consider_all_requests_local = false
  ...
end
```

### Step 2: Configure Production Environment

In the `config` folder, check `environments/production.rb` for the following line and make sure it's set to true.

```ruby
# config/environments/production.rb
Rails.application.configure do
  ...
  config.cache_classes = true
  ...
end
```

### Step 3: Restart the server

Finally, in order to ensure that the changes take effect, restart your server:

```bash
pkill -f puma
RAILS_ENV=production bundle exec puma -C config/puma.rb
```

By ensuring that Debug Mode is not enabled in your production environment, you can help keep your Rails application secure.