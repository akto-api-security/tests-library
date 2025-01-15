# Remediation for DJANGO_SQLI

## Remediation Steps for Django SQL Injection

SQL Injection is a common and serious security vulnerability. If not properly secured, attackers may use injection vulnerabilities to execute arbitrary SQL code on your database, potentially compromising your entire system. Django uses SQL databases, so it could be open to these types of attacks. 

However, Django has built-in protection against most types of SQL injection. It uses query parameterization, which means that all variables are sent to the database separately from the query, leaving no room for injection. However, there are still cases where you may inadvertently open yourself up to SQL injection if you're not careful.

### Step 1: Use Django's ORM

Django provides a full-featured Object-Relational Mapper (ORM) which you can use to interact with your database in a safe, Pythonic way, instead of crafting SQL queries by hand.

Here's an example of how to use it:

```python
from myapp.models import MyModel

items = MyModel.objects.filter(name='MyName')
```

### Step 2: Avoid Raw SQL queries

While Django's ORM is incredibly powerful and suits most needs, sometimes you may need to write raw SQL queries. If you do, never ever include user input directly into your SQL queries. Always use parameterization provided by Django ORM:

```python
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM my_table WHERE name = %s", [user_input])
```

In this example, `user_input` is automatically escaped by Django.

### Step 3: Avoid `extra()`

Django's ORM has a method called `extra()` that you can use to add arbitrary SQL to your query. However, `extra()` is deprecated and also potentially dangerous because it doesn't automatically escape its inputs:

```python
MyModel.objects.extra(where=["name = 'MyName'"])
```

This code is vulnerable to SQL injection if 'MyName' included user input. Avoid `extra()` whenever possible.