"""
Django settings for agrosite project.
"""

from django.utils.translation import gettext_lazy as _
from pathlib import Path
import os
import sys

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-a4pl9x_640)f)p44&h%edo=+j!aqwslo1&1)y6s)x3c+q*l*$j'

DEBUG = False  # 🚨 turn off in production

print(">>> STARTUP using settings file:", __file__, file=sys.stderr)

ALLOWED_HOSTS = [
    "agrosite-1.onrender.com",  # Render
    "127.0.0.1",
    "localhost",
    ".vercel.app",
]

print(">>> STARTUP ALLOWED_HOSTS:", ALLOWED_HOSTS, file=sys.stderr)

# CSRF (important for Render/Ngrok/Vercel preview domains)
CSRF_TRUSTED_ORIGINS = [
    "https://agrosite-1.onrender.com",
    "https://lashell-unleavenable-brycen.ngrok-free.dev",
    "https://*.vercel.app",
]

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
]

MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # must be right after SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'agrosite.urls'

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

WSGI_APPLICATION = 'agrosite.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGES = [
    ('fr', 'French'),
    ('ar', 'Arabic'),
]

LANGUAGE_CODE = 'fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
USE_L10N = True

CURRENCY = 'DZD'

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

JAZZMIN_SETTINGS = {
    "site_title": "Slim Agri Admin",
    "site_header": "Slim Agri",
    "welcome_sign": "Bienvenue sur le panneau d'administration",
    "site_brand": "Slim Agri Admin",
    "copyright": "© 2025 SLIM AGRI. Tous droits réservés.",
    "user_avatar": None,
    "topmenu_links": [
        {"name": "Accueil", "url": "admin:index", "permissions": ["auth.view_user"]},
    ],
    "order_with_respect_to": ["products.Product", "orders.Order"],
    "show_sidebar": True,
    "navigation_expanded": True,
}

print(">>> USING SETTINGS FILE:", __file__, file=sys.stderr)
print(">>> ALLOWED_HOSTS =", ALLOWED_HOSTS, file=sys.stderr)
