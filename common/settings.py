"""
Django settings for willmoggridge project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
import sys

from common import env_vars
from libs.environment import EnvironmentVariables

env = EnvironmentVariables(prefix='WILLMOGGRIDGE_')
env.load(env_vars.ENV_VARS)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Append the apps folder so apps can be called as "APPNAME",
# rather than "apps.APPNAME"
sys.path.append(os.path.join(BASE_DIR, 'apps'))


# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = ''

DATABASES = {}
# DATABASES = {
#     "default": {
#         # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3"
#         # or "oracle".
#         "ENGINE": "django.db.backends.sqlite3",
#         # Or path to database file if using sqlite3. 
#         "NAME": "../test_db.sqlite3",
#         # Not used with sqlite3.
#         "USER": "",
#         # Not used with sqlite3.
#         "PASSWORD": "",
#         # Set to empty string for localhost. Not used with sqlite3.
#         "HOST": "",
#         # Set to empty string for default. Not used with sqlite3.
#         "PORT": "",
#     }
# }

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
