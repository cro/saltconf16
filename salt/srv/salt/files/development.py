# Django settings for development deploy of SSC project.
# -*- coding: utf-8 -*-
import os
from settings.common import *

DEBUG = True

SITE_ID = 3
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ pillar["django_database_name"]}}',
        'USER' : 'ssc',
        'PASSWORD' : '{{ pillar["django_database_password"]}}',
        'HOST': 'localhost',
        'PORT' : '',
    }
}

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
# ADMIN_MEDIA_PREFIX = '/admin/'


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
#STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
# ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
#STATICFILES_DIRS = (
#    # Put strings here, like "/home/html/static" or "C:/www/django/static".
#    # Always use forward slashes, even on Windows.
#    # Don't forget to use absolute paths, not relative paths.
#    PROJECT_PATH / 'static',
#)
