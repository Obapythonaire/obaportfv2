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

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['abdulahiogundare.pythonanywhere.com']


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

DATABASE_URL = env("DATABASE_URL")
DATABASES = {
    'default': dj_database_url.config(default=env('DATABASE_URL'))
    }

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


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

BASE_URL = '127.0.0.1:8000'
# BASE_URL = 'http://abdulahiogundare.pythonanywhere.com/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = '/home/abdulahiogundare/obaportfv2/portfolio2/static'


# To serve media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_ROOT = '/home/abdulahiogundare/obaportfv2/portfolio2/media'

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
    'limited_config': {
        'toolbar': [
            ['Bold', 'Italic', 'Underline', 'Strike'],  # Basic formatting
            ['NumberedList', 'BulletedList', 'Outdent', 'Indent'],  # Lists
            ['Link', 'Unlink'],  # Hyperlinks
            # ['Image', 'Table'],  # Images and tables
            ['Image', 'Table'],  # Images and tables
            ['Maximize'],  # Maximize button
        ],
        # Other CKEditor configuration options...
    },
}

# JAZZMIN SETTINGS STARTS
JAZZMIN_SETTINGS = {
    "site_title": "Abdulahi Ogundare - SE",
    "site_header": "Abdulahi Ogundare",
    "site_brand": "Software Engineering",
    "site_icon": "portfoliov2/images/OBA_PASSPORT-imresizer.jpeg",
    # Add your own branding here
    "site_logo": "portfoliov2/images/OBA_PASSPORT-imresizer.jpeg",
    "welcome_sign": "Welcome to my Portfolio Site",
    # Copyright on the footer
    "copyright": "AbdulahiOgundare",
    "user_avatar": "portfoliov2/images/OBA_PASSPORT-imresizer.jpeg",
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Abdulahi Ogundare", "url": "home", "permissions": ["auth.view_user"]},
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "users.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "admin.LogEntry": "fas fa-file",
    },
    # # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-arrow-circle-right",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    # Uncomment this line once you create the bootstrap-dark.css file
    "custom_css": "portfoliov2/css/jazzminbootstrap-dark.css",
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
    ###############
    # Change view #
    ###############
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-success",
    "accent": "accent-teal",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-info",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "cyborg",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}
# JAZZMIN SETTINGS ENDS
