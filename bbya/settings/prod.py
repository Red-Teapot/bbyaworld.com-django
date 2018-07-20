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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'fileDjango': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'verbose',
        },
        'fileApp': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/app.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['fileDjango'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
        '': {
            'handlers': ['fileApp'],
            'level': os.getenv('APP_LOG_LEVEL', 'ERROR'),
        },
    },
}