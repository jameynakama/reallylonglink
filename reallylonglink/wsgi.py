"""
WSGI config for reallylonglink project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

import envdir

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reallylonglink.settings")

envdir.open('/home/jameydeorio/webapps/reallylonglink/envdir')

application = get_wsgi_application()
