# Remediation for DRUPAL_SQLI

## Remediation Steps for Drupal SQL Injection

SQL injection is a serious security vulnerability that can allow an attacker to manipulate your database records or even leak sensitive secrets from them. Without properly validating and sanitizing user inputs or without using SQL statements that are parameterized, applications may expose themselves to these types of attacks.

### Step 1: Update Drupal Version

Update your Drupal version to the latest one. Drupal released a security patch in version 7.32 to address the SQL Injection vulnerability. Use the commands below to update your Drupal application:

```bash
drush pm-update drupal
```

or

```bash
composer update drupal/core --with-dependencies
```

### Step 2: Use Prepared Statements

Use Drupal's abstraction layer functions such as `db_query()` or `db_select()`, these functions automatically use prepared statements which make them safe against SQL Injections. Avoid concatenating strings to form SQL queries.

Here's an example:

```php
$query = db_select('mytable', 'm');
$query->fields('m')
  ->condition('m.myfield', $some_value, '=')
  ->execute();
```
### Step 3: Use Parameterized Queries

If you must write SQL, use parameterized queries to prevent injection of rogue SQL.

Here's an example:

```php
db_query('SELECT n.nid, n.title, n.created
  FROM {node} n WHERE n.uid = :uid', array(':uid' => $user->uid));
```

In the above method, `:uid` is a placeholder for a value to be interpolated by `db_query()`.
Note the use of curly braces `{}` around table names, this is a Drupal convention that allows the system to replace it with the actual table names.

### Step 4: Regular Audit and Update 

Perform regular checks on your website for any possible SQL injection vulnerabilities. It is also essential that you keep your Drupal installation up to date with the latest security patches.

```bash
drush pm-updatestatus
```

**References:**

[Drupal SQL Injection](https://www.drupal.org/docs/7/security/writing-secure-code/sql-injection)