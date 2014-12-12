"""
Django settings for lucchetti project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""




# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import mysecrets

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
SECRETS = mysecrets.secrets

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETS['django_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID=1

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'cms',  # django CMS itself
    'mptt',  # utilities for implementing a modified pre-order traversal tree
    'menus',  # helper for model independent hierarchical website navigation
    'south',  # intelligent schema and data migrations
    'sekizai',  # for javascript and css management
    'djangocms_admin_style',  # for the admin skin. You **must** add 'djangocms_admin_style' in the list before 'django.contrib.admin'.
    'django.contrib.messages',  # to enable messages framework (see :ref:`Enable messages <enable-messages>`)
    'djangocms_link',
    'djangocms_video',
    'djangocms_text_ckeditor',
    'inline_ordering',
    'filer',
    'easy_thumbnails',
    'novita',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'slideshow',
    'adminsortable',
)

MIDDLEWARE_CLASSES = (
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
#    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.i18n',
        'django.core.context_processors.request',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'cms.context_processors.cms_settings',
        'sekizai.context_processors.sekizai',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
        # The docs say it should be absolute path: PROJECT_PATH is precisely
        # one.
        # Life is wonderful!
        os.path.join(PROJECT_PATH, "templates"),
)

CMS_TEMPLATES = (
        ('home_page_template.html', 'Template One'),
        ('news_template.html', 'News Template'),
        ('plain_page.html', 'Pagina Vuota'),
        ('timeline.html', 'Timeline'),
)

ROOT_URLCONF = 'lucchetti.urls'

WSGI_APPLICATION = 'lucchetti.wsgi.application'

#django-cms
LANGUAGES = [
    ('it', 'Italiano'),
    ('en', 'English'),
]


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'negozio',                      # Or path to database file if using sqlite3.
        'USER': SECRETS['postgresql_username'],                      # Not used with sqlite3.
        'PASSWORD': SECRETS['postgresql_password'],                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    },
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'django',
#         'USER': SECRETS['postgresql_username'],
#         'PASSWORD': SECRETS['postgresql_password'],
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'it'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, "static"),
)

STATIC_ROOT = "/var/www/static/"
STATIC_URL = "/static/"

MEDIA_ROOT = "/var/www/media/"
MEDIA_URL = "/media/"

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

CMSPLUGIN_FILER_IMAGE_STYLE_CHOICES = (
    ('default', 'Default'),
    ('promo-img', 'Promo Image'),
)
