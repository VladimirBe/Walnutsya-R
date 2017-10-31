"""
Django settings for blogproject project.
Generated by 'django-admin startproject' using Django 1.10.1.
For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'site_secret_key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']
SITE_ID = 1
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'bejanvadim@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
FILE_UPLOAD_MAX_MEMORY_SIZE = 35000000

DISQUS_API_KEY = '5SAJOVv5ZIWmaeU3JOg8waxOiHFFBDLvVdjtyRjpKeyfaOwHXLMAsjJKnWmLDYgh'
DISQUS_WEBSITE_SHORTNAME = 'https://http-vladimirb-pythonanywhere-com.disqus.com/admin/'

# No Recaptha SITE_KEY and SECRET KEY
# https://www.google.com/recaptcha
NORECAPTCHA_SITE_KEY = "6LcsVxYUAAAAAKbRS4CneuGuJZb2Pn5O7CnpKjGk"
NORECAPTCHA_SECRET_KEY = "6LcsVxYUAAAAAIteMV6o3PBDLus1ooqkSbiZtTH_"

# Application definition
INSTALLED_APPS = [
    # Adding Django admin suit
    'suit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sitemaps',
    'django.contrib.sites',
    'markdown',
    'disqus',
    'redactor',
    'nocaptcha_recaptcha',
    'import_export',

    'blog',
]

# Django Suit configuration
SUIT_CONFIG = {
    'ADMIN_NAME': 'Python Learning',
    'SEARCH_URL': '/admin/blog/post/',
    'MENU': (
        {'app': 'blog', 'label': 'Blog', 'models': ('post', 'tag', 'page', 'author', 'gallery', 'visitor'),
            'icon': 'icon-align-left'},
        '-',
        {'app': 'auth', 'label': 'Authentication',
            'icon': 'icon-lock', 'models': ('user', 'group')},
        {'app': 'sites', 'label': 'Site Config', 'icon': 'icon-leaf'},
    ),
    'LIST_PER_PAGE': 15
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogproject.urls'

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

WSGI_APPLICATION = 'blogproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Config with postgresql - psql (9.5.4, server 9.3.14)
# $ sudo su - postgres
# $ psql
# postgres=# CREATE DATABASE database_nme;
# postgres=# CREATE USER database_user WITH PASSWORD 'password_user';
# postgres=# GRANT ALL PRIVILEGES ON DATABASE database_nme TO database_user;
# See this docs for more; https://goo.gl/9ONJKX

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database_nme',
        'USER': 'database_user',
        'PASSWORD': 'password_user',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
"""

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Bucharest'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static')

# Editor Redactor
import time
REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_UPLOAD = 'uploads/' + time.strftime("%Y/%m/%d/")
REDACTOR_AUTH_DECORATOR = 'django.contrib.auth.decorators.login_required'