

## Remediation Steps for RabbitMQ Default Login

Security issues may arise from using the default login details in RabbitMQ. It can lead to unauthorized access, leading to information exposure and potential misuse of the system. To mitigate this, default credentials must be changed or disabled. 

Below are remediation steps for changing the default username and password. 

### Step 1: Connect to RabbitMQ 
First, establish a secure connection to your RabbitMQ server. 

### Step 2: Change Default Credentials

You can use RabbitMQ's management interface or `rabbitmqctl` utility to change default login credentials. Here are examples of how to do this:

#### Via RabbitMQ's Management Interface
```bash
curl -i -u guest:guest -H "content-type:application/json" -XPUT http://localhost:15672/api/users/newuser -d'{"password":"newpassword","tags":""}'
```

#### Via 'rabbitmqctl' utility
```bash
rabbitmqctl change_password guest newpassword
```

In both the above codes, replace `newuser` with your new username and replace `newpassword` with your new, strong password.