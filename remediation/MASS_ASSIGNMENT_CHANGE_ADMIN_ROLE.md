# Remediation for MASS_ASSIGNMENT_CHANGE_ADMIN_ROLE

## Remediation Steps for Mass Assignment Granting Low Privilege User Admin Role Access
Mass assignment is a common security issue where an attacker is able to assign values to unintended model attributes through mass assignment. This is especially critical when it comes to user roles, where a low privilege user could gain admin access.

### Step 1: Prevent Direct Assignment of Critical Attributes
In most modern web frameworks, you can prevent certain attributes from being updated through mass assignment. For Ruby on Rails, this may look like:
```ruby
class User < ApplicationRecord
  attr_accessible :name, :email, :password, :password_confirmation
end
```
In the above code, the `:role` attribute is not listed, so it cannot be updated through mass assignment.

### Step 2: Utilize Strong Parameters (Specifically in Rails)
Rails introduced Strong Parameters to deal with mass assignment vulnerabilities. With strong parameters, attributes must be explicitly permitted for mass assignment in the controller's method. Here's an example in Rails:

```ruby
class UsersController < ApplicationController
  def update
    @user = User.find(params[:id])
    if @user.update(user_params)
      redirect_to @user
    else
      render 'edit'
    end
  end

  private

    def user_params
      params.require(:user).permit(:name, :email, :password, :password_confirmation)
    end
end
```
In the `user_params` private method, only the permitted attributes can be updated via mass assignment.