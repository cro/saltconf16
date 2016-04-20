# Django settings for ssc project.
# -*- coding: utf-8 -*-
import os
import warnings

warnings.simplefilter("ignore")

import path

gettext = lambda s: s
PROJECT_DIR = path.path(__file__).abspath().dirname().dirname()

DEBUG = False
DEFAULT_FROM_EMAIL = 'SaltStack Certification <ssc@saltstack.com>'
SERVER_EMAIL = 'ssc@saltstack.com'
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/profile/'
SECURE_PROXY_SSL_HEADER = ('X_SCHEME', 'https')
# Django-debug-toolbar
INTERNAL_IPS = ('127.0.0.1',)

# PIL Sucks!!!
# import sys
# import PIL.Image
# sys.modules['Image'] = PIL.Image

# Shut South up

import logging

south_logger = logging.getLogger('south')
south_logger.setLevel(logging.INFO)

ADMINS = (
    ('C. R. Oldham', 'cr@saltstack.com'),
    # ('Your Name', 'your_email@example.com'),
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Denver'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# This is set in development.py / production.py
# SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

STATICFILES_DIRS = (os.path.join(PROJECT_DIR, 'static_dev'), )

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
# ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ pillar["django_secret_key"] }}'


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
            os.path.join(PROJECT_DIR, "templates"),
        ],
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.core.context_processors.request',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    # 'south',
    'sekizai',
    'reversion',
    # 'autocomplete_light',
    # 'debug_toolbar',
    # 'debug_toolbar_user_panel',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'django_extensions',
    # 'django_nose',
    'ssc',
    'django.contrib.humanize',
    'crispy_forms',
    'bootstrap3',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'
AUTH_PROFILE_MODULE = 'reg.Person'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
# AllAuth settings
ACCOUNT_ADAPTER = 'ssc.accountadapter.SaltstackAccountAdapter'
SOCIALACCOUNT_ADAPTER = 'ssc.accountadapter.SaltstackSocialAccountAdapter'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[SaltStack Certification]'
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_HMAC = True
# Not needed for current version?
# SOCIALACCOUNT_ENABLED = False
SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_EMAIL_VERIFICATION = ACCOUNT_EMAIL_VERIFICATION

# SaltstackAccountAdapter checks to see if the login
# email ends in this string
ALLAUTH_REQUIRE_DOMAIN = '@saltstack.com'

# ACCOUNT_SIGNUP_FORM_CLASS = 'accounts.forms.SSCSignupForm'
SOCIALACCOUNT_PROVIDERS = \
    {'google':
         {'SCOPE': ['profile',
                    'email'],
          'AUTH_PARAMS': {'access_type': 'online'},
         },
     'github':
         {'SCOPES': ['user:email']},
    }

LANGUAGES = [
    ('en', 'English'),
]

CMS_LANGUAGES = {
    1: [
        {
            'code': 'en',
            'name': gettext('English'),
            'fallbacks': ['de', 'fr'],
            'public': True,
            'hide_untranslated': True,
            'redirect_on_fallback': False,
        },
    ],
    'default': {
        'fallbacks': ['en', ],
        'redirect_on_fallback': True,
        'public': False,
        'hide_untranslated': False,
    }
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'debug-false-only': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['debug-false-only'],
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# django-debug-toolbar configuration
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar_user_panel.panels.UserPanel',
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    # 'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    # 'debug_toolbar.panels.logger.LoggingPanel',
)


def custom_show_toolbar(request):
    return DEBUG or (request.user.is_authenticated() and
                     request.user.username == 'cro')


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    'HIDE_DJANGO_SQL': False,
    'TAG': 'div',
    'ENABLE_STACKTRACES': True,
}

#    'EXTRA_SIGNALS': ['myproject.signals.MySignal'],
