"""
Django settings for webBase project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import string  # @UnusedImport
import random  # @UnusedImport

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_NAME = os.path.basename(BASE_DIR)
SITE_ROOT = os.path.dirname(BASE_DIR)

CONFIGURATION_DIRECTORY = os.path.normpath( os.path.join( SITE_ROOT, 'config' ) )

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'webBase.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                ],
            'builtins': [ 'webBase.templatetags.base_tags'
                ],
        },
    },
]

STATICFILES_DIRS = [ ("common", os.path.join( BASE_DIR, "webBase/static" ) ), ]

WSGI_APPLICATION = 'webBase.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'webBase.db3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


SITE_ID = 1

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

#    local configuration values
try:
    LOCAL_SETTINGS  # @UndefinedVariable
except NameError:
    try:
        from .settings_local import *
    except ImportError: #    pragma: no cover
        pass

# Try to load the SECRET_KEY from our SECRET_FILE. If that fails, then generate
# a random SECRET_KEY and save it into our SECRET_FILE for future loading. If
# everything fails, then just raise an exception.

SECRET_FILE = os.path.normpath(os.path.join( CONFIGURATION_DIRECTORY, 'SECRET'))
try:
    with open( SECRET_FILE ) as f:
        SECRET_KEY = f.read().strip()
except IOError: #    pragma: no cover
    try:
        base = string.digits + string.ascii_letters + string.punctuation
        chars = [random.SystemRandom().choice(base) for i in range(50)]
        with open( SECRET_FILE, 'w' ) as f:
            f.write("".join(chars))
        SECRET_KEY = chars
    except IOError:
        raise Exception('Cannot open file `%s` for writing.' % SECRET_FILE)

