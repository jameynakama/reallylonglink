import logging
import os
import string

import envdir


logger = logging.getLogger(__name__)


SOMETHING = os.environ.get('FFUUU')
logger.warning(">>>>> {}".format(SOMETHING))
logger.warning(">>>>> {}".format(dir(envdir)))
logger.warning(">>>>> {}".format(os.environ))
if SOMETHING:
    envdir.open(SOMETHING)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = os.environ.get('DEBUG', 'False') == 'True'
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',

    'reallylonglink'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'reallylonglink.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'reallylonglink.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'reallylonglink',
        'USER': 'reallylonglink',
        'PASSWORD': os.environ.get('DB_PASSWORD', 'password'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get('STATIC_ROOT')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(levelname)s] [%(asctime)s] [%(name)s]: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'syslog': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'logging.handlers.SysLogHandler',
            'address': '/dev/log',
            'facility': 'user',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'syslog'],
            'level': 'DEBUG' if DEBUG else 'INFO'
        },
        'django.db': {
            'handlers': ['syslog', 'console'],
            'level': 'INFO',
            'propagate': False
        },
        'django.request': {
            'handlers': ['syslog', 'console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': False
        },
    }
}

if not os.path.exists('/dev/log'):
    LOGGING['handlers']['syslog'] = {'class': 'logging.NullHandler'}


#
# App settings
#
DOMAIN = 'http://www.reallylong.link/'
BASE_REDIRECT_URL = 'rll'
MAX_URL_LENGTH = 1999  # Leave room for optional trailing slash
LINK_CHARS = string.ascii_letters + string.digits + '_/'
REALLY_LONG_LINK_LENGTH = MAX_URL_LENGTH - len(DOMAIN) - len(BASE_REDIRECT_URL) - len('//')  # /{{ rll }}/
