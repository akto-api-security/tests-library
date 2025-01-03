# Remediation for LARAVEL_TELESCOPE_ENABLED

## Remediation Steps for Laravel Telescope Enabled

Laravel Telescope making your application's details public is a severe security problem. If Laravel Telescope is enabled in production, it can expose sensitive data. Here are the steps to disable it.

### Step 1: Check the Telescope Configuration
First, verify that Telescope isn't enabled in production. Open the configuration file located at `config/telescope.php`. 

The `enabled` option in this file determines if Telescope is enabled for your application. 

For most applications, you should disable Telescope in your production environment, as it can expose private application information like requests handled by the application, exceptions & logs.

```php
'environments' => env('TELESCOPE_ENABLED', false),
```
This will set the `TELESCOPE_ENABLED` value to 'false' by default. This means telescope will be disabled unless explicitly told to be enabled.

### Step 2: Set Environment Specific Value
In your `.env` file, you can define whether to enable or disable the Telescope for a specific environment. 

```
TELESCOPE_ENABLED=false
```
This will override the default value set in the `telescope.php` configuration file.

### Step 3: Applying Access Control
To restrict who can access your Telescope, define a `gate` configuration within the `boot` method of your `TelescopeServiceProvider`:

```php
protected function gate()
{
    Gate::define('viewTelescope', function ($user) {
        return in_array($user->email, [
            'taylor@laravel.com',
            // Other developers e-mail addresses
        ]);
    });
}
```
Above code will allow access only for users with specified emails.

### Step 4: Clear Compiled Files

Once changes are made, clear and re-compile:

```bash
php artisan config:clear
php artisan config:cache
php artisan route:clear
php artisan route:cache
php artisan view:clear
php artisan view:cache
```
This will make sure your updated configuration changes have taken effect across the application. 

Remember to keep Laravel Telescope disabled in your production environment and limit access to Telescope in your local environment to authorized users only.