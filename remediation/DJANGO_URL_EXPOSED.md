# Remediation for DJANGO_URL_EXPOSED

## Remediation Steps for Django URL Exposure Due to Debug Mode Enablement

Django URL exposure due to debug mode enablement is a serious security issue. Debug mode is intended for use in development and can expose sensitive information if enabled in a production environment.

### Step 1: Disable Debug Mode in Django

Firstly, open the `settings.py` file in your Django project, the debug field should be located towards the top of the file. 

Here's a Python snippet on how to disable debug mode:

```python
# in settings.py

DEBUG = False
```
This setting turns off the debug mode.

### Step 2: Use Separate Settings for Development and Production

It's also a good practice to separate your production settings and development settings. Make sure debug is False on your production setting.

Here is a simplified example on how to implement it:

```python
# in settings.py

DEBUG = False

try:
    # Try to load local_settings.py if it exists
    from .local_settings import *  
except ImportError:
    pass
```

In the `local_settings.py` file:

```python
DEBUG = True
```
This will allow you to maintain a production-safe settings file while easily keeping local settings that can differ between instances of the application.