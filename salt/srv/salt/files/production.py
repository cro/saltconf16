# Django settings for hkcms project.
# -*- coding: utf-8 -*-
from settings.common import *

DEBUG = False
TEMPLATE_DEBUG = False
SESSION_COOKIE_SECURE = True

EMAIL_HOST='localhost'
EMAIL_PORT=25


SITE_ID = 2

ALLOWED_HOSTS = ['ssc.saltstack.com', '23.253.90.73']

# Databases clause moved to individual deployment settings files.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ssc',
        'USER': 'ssc',
        'PASSWORD': '{{ pillar["django_database_password"] }}',
        'HOST': 'localhost',
        'PORT': '',
    }
}
