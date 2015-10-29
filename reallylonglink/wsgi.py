"""
WSGI config for reallylonglink project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

import django
from django.core.handlers.wsgi import WSGIHandler


class WSGIEnvironment(WSGIHandler):
    def __call__(self, environ, start_response):
        os.environ['FFUUU'] = environ['ENV_LOCATION']
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reallylonglink.settings")
        django.setup()
        return super(WSGIEnvironment, self).__call__(environ, start_response)

application = WSGIEnvironment()
