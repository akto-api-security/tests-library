# Remediation for MASS_ASSIGNMENT_CREATE_ADMIN_ROLE

## Remediation Steps for Mass Assignment Leading to Creation of Admin Role
Mass Assignment is a vulnerability that is found in applications where an attacker can update all the fields of a data object for which it has no permissions. This vulnerability can lead to the creation of a user with an admin role if not handled properly.

### Step 1: Limiting Accessible Attributes at the Model Level (Rails Example)
```ruby
class User < ActiveRecord::Base
  attr_accessible :name, :email # Only these fields can be mass-assigned
end
```
In this example, only the "name" and "email" attributes can be mass-assigned, preventing access to sensitive attributes such as an admin flag.

### Step 2: Strong Parameters (Rails Example)
Strong parameters allow you to control which attributes should be whitelisted for mass updating and thus prevent accidentally exposing that allows to assign to reserved attributes.
```ruby
class UsersController < ApplicationController
  def create
    User.create!(user_params)
  end

  private

  def user_params
    params.require(:user).permit(:name, :email)
  end
end
```
In this example, the "user_params" function defines a whitelist of parameters that can be mass-assigned for User.

### Step 3: Use Role-Based Access Control (RBAC)
In role-based systems, roles are created for various job functions and permissions are assigned to the roles. Users are not granted permissions directly, but only acquire them through their role (or roles). Simply not provide roles that allow mass assignment of administrative privileges.

### Step 4: Regularly Audit your Codebase
Ensure to verify that access controls are correctly put in place and that mass assignment vulnerabilities are not present.

Please note that this is a Ruby on Rails sample remediation, and your language or framework may have different methods for preventing mass assignment vulnerabilities.