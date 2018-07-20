#  pylint: disable=all

from .common import *


DEBUG = False

ALLOWED_HOSTS += ['bbyaworld.com']

DEFAULT_DB_SECRETS = SECRETS['db']['default']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DEFAULT_DB_SECRETS['name'],
        'USER': DEFAULT_DB_SECRETS['user'],
        'PASSWORD': DEFAULT_DB_SECRETS['password'],
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
}

PIPELINE['PIPELINE_ENABLED'] = True