"""
WSGI config for takeaway project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'takeaway.settings')

# There is no error in your wsgi.py file.
# The error is in your URL or template configuration.
# Make sure you are visiting /products/menu/ (not /products/menu.html/)
# and that your template is named menu.html and is in the correct templates directory.
