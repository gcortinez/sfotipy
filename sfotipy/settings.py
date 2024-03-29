"""
Django settings for sfotipy project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$xavdo(iv0$!ydz72^f&@qkec#n%%ynj&6%)2fr$hi64ty5qy_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

GRAPPELLI_ADMIN_TITLE = 'erwilli'

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'sfotipy.context_processors.basico',

)

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'tracks',
    'albums',
    'artists',
    'userprofiles',
    'autofixture',
    'django_extensions',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    #'sfotipy.middleware.PaisMiddleware',
)

CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

ROOT_URLCONF = 'sfotipy.urls'

WSGI_APPLICATION = 'sfotipy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

SOUTH_TESTS_MIGRATE = False
SKIP_SOUTH_TESTS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sfotipy',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

CACHES = {
    'default': {
        'BACKEND' : 'redis_cache.RedisCache',
        'LOCATION' : 'localhost:6379',
        'OPTIONS' : {
            'DB' : 1
            #'PASSWORD' : 'ALGO',
            #'PARSER_CLASS' : 'redis.connection.HiredisParser'
        }
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'content')
#MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:2] + ['media'])
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

#backends

#AUTHENTICATION_BACKENDS = (
   # 'userprofiles.backends.EmailBackend',
#)
