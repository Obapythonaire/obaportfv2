from pathlib import Path
import os
import environ, dj_database_url

# Load environment variables from .env
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY =env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['abdulahiogundare.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "portfoliov2.apps.Portfoliov2Config",

    "ckeditor",
    # 'ckeditor_uploader',

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "portfolio2.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR,'templates/')],
        # "DIRS":[],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "portfolio2.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASE_URL = env("DATABASE_URL")
# DATABASES = {
#     'default': dj_database_url.config(default=env('DATABASE_URL'))
#     }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

BASE_URL = 'http://abdulahiogundare.pythonanywhere.com/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = '/home/abdulahiogundare/obaportfv2/portfolio2/static'


# To serve media files
MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = '/home/abdulahiogundare/obaportfv2/portfolio2/media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# For sendmail/mail config
EMAIL_BACKEND = env('EMAIL_BACKEND')
# EMAIL_HOST = 'smtp-relay.brevo.com'
# EMAIL_HOST_USER = 'obatech518@gmail.com'
EMAIL_PORT = env('EMAIL_PORT')
# EMAIL_USE_SSL = True
EMAIL_USE_TLS = env('EMAIL_USE_TLS')  # TLS is required for Gmail
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = 'jgyqgalbkyfwradc'

# EMAIL_HOST_PASSWORD = 'xsmtpsib-57a13e96f00a3547c19a91f8698afb40d4798a10e145582ecaddebee2b94d99a-CJYGtA7qTF9cyXDv'
# EMAIL_HOST_PASSWORD = 'xsmtpsib-57a13e96f00a3547c19a91f8698afb40d4798a10e145582ecaddebee2b94d99a-XJPGHVfjz4O7n2QB'
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')  # Replace with your email address
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
# EMAIL_HOST_USER = 'obatech518@gmail.com'
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = 465    #587
# # EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True

# CKEditor configuration
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        # 'height': 300,
        'width': 'auto',
        'extraPlugins': ','.join([
            'codesnippet',
        ])
        # 'toolbar_Custom': [
        #     ['Bold', 'Italic', 'Underline'],
        #     ['NumberedList', 'BulletedList'],
        #     ['Link', 'Unlink'],
        #     ['RemoveFormat'],
        # ],
    },
}
