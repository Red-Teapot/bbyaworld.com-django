import os
import json

from pathlib import Path


BASE_DIR = str(Path(__file__).resolve().parent.parent.parent)

SECRETS_FILE = os.path.join(BASE_DIR, 'secrets.json')

SECRETS = {
    'secret_key': 'so secret',
    'db': {
        'default': {
            'name': 'db',
            'user': 'django',
            'password': 'django',
        },
    },
    'allowed_hosts': [],
}

try:
    with open(SECRETS_FILE) as f:
        secrets_json = json.loads(f.read())
        SECRETS.update(secrets_json)
except:
    pass

SECRET_KEY = SECRETS['secret_key']

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]'] + SECRETS['allowed_hosts']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pipeline',
    'django_cron',
    'common.apps.CommonConfig',
    'server_status.apps.ServerStatusConfig',
    'website.apps.WebsiteConfig',
    'player_online_stats.apps.PlayerOnlineStatsConfig',
    'clans_cells.apps.ClansCellsConfig',
    'player_regions.apps.PlayerRegionsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bbya.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'templates/jinja2')],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'bbya.jinja2.environment',
            'extensions': ['pipeline.jinja2.PipelineExtension'],
        }, 
    },
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

WSGI_APPLICATION = 'bbya.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'bower_components'),
)

PIPELINE = {
    'PIPELINE_ENABLED': False,
    'CSS_COMPRESSOR': 'pipeline.compressors.yuglify.YuglifyCompressor',
    'JS_COMPRESSOR': 'pipeline.compressors.yuglify.YuglifyCompressor',
    'YUGLIFY_BINARY': os.path.join(BASE_DIR, 'node_modules/yuglify/bin/yuglify'),
    'COMPILERS': (
        'pipeline.compilers.stylus.StylusCompiler',
    ),
    'STYLUS_BINARY': os.path.join(BASE_DIR, 'node_modules/stylus/bin/stylus'),
    'STYLESHEETS': {
        'website_main': {
            'source_filenames': (
                'website/stylus/main.styl',
            ),
            'output_filename': 'css/website_main.css',
        },
        'bower': {
            'source_filenames': (
                'bootstrap/dist/css/bootstrap.min.css',
            ),
            'output_filename': 'css/bower.css',
        },
    },
    'JAVASCRIPT': {
        'website_main': {
            'source_filenames': (
                'website/js/*.js',
            ),
            'output_filename': 'js/website_main.js',
        },
        'bower': {
            'source_filenames': (
                'jquery/dist/jquery.min.js',
                'bootstrap/dist/js/bootstrap.min.js',
            ),
            'output_filename': 'js/bower.js',
        },
    },
}

CRON_CLASSES = [
    'player_online_stats.update_job.UpdateJob',
    'clans_cells.update_job.UpdateJob',
    'player_regions.update_job.UpdateJob',
]