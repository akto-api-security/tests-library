# Remediation for MASS_ASSIGNMENT_CHANGE_ACCOUNT

## Remediation Steps for Mass Assignment Leading to Modification of Account

Mass assignment can lead to serious security issues, where attackers can modify or escalate permissions of user accounts. To prevent this, we can use a method known as 'whitelisting' to define which parameters are permitted in mass assignments.

### Step 1: Understand and Identify Model Attributes

The first thing is to identify all the attributes of your model that you don't want to be mass assignable.

```ruby
class User < ApplicationRecord
  # attr_accessible :name, :password, :password_confirmation
  attr_protected :is_admin
end
```
In the above Ruby on Rails example, `:is_admin` is an attribute we wouldn't want mass assignable.

### Step 2: Implement Whitelisting in Controllers

The second step would be to setup strong parameters in your controllers to prevent mass assignment.

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
      params.require(:user).permit(:name, :password, :password_confirmation)
    end
end
```
In the above Ruby on Rails example, only `:name`, `:password`, and `:password_confirmation` are permitted to be updated.

### Step 3: Regular Code Review and Update

Regularly review and update your code to ensure new attributes are properly whitelisted and not prone to mass assignment vulnerabilities. Ensuring updated and secure dependencies can also aid in prevention.

### Note

_This example is in the context of a Ruby on Rails application. Depending on your application's language and framework, the specific approach to mitigating mass assignment vulnerabilities may vary._

## Conclusion

Mass assignment is a serious issue that can lead to unauthorized modification of user accounts. Always ensure to whitelist attributes that can be changed in mass assignments to avoid such vulnerabilities.