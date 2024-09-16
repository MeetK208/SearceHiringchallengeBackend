"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
import os
print(os.getcwd())  # Check the current working directory
# DEBUG = True

load_dotenv(".env")
print("DB Url is",os.environ.get('DATABASE_URL'))
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e)21&&p2&ck1_k)r(8mu^8+-%3y%yw)(csmn5(p1j*)yzh_6#)'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = ["searcehiringchallenge.onrender.com", "*", "127.0.0.1", "0.0.0.0"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'rest_framework',
    'corsheaders',
    'register',
    'projectcard',
    'usercard',
]

if os.environ.get("DEBUG") == "True":
    SESSION_COOKIE_SAMESITE = 'Lax'  # No cross-origin cookie sharing for local
    CSRF_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

else:
    SESSION_COOKIE_SAMESITE = 'None'  # Allow cross-origin cookie sharing for deployment
    CSRF_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_SECURE = True  # Secure cookie for HTTPS
    CSRF_COOKIE_SECURE = True  # Secure CSRF cookie for HTTPS

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS"
]
CORS_ALLOW_HEADERS = [
    'cookies',
    'content-type',
    'authorization',
    'x-csrftoken',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",   # Frontend running locally
    "http://127.0.0.1:3000",   # Frontend with localhost IP
    "http://0.0.0.0:3000",     # Dockerized app running on local network
    "https://yourfrontenddomain.com",  # Deployed frontend
    "https://searcehiringchallenge.onrender.com",  # Deployed backend
    "http://localhost:4200",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'register.middleware.AuthenticationMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

print(os.environ.get("DEBUG"))
if os.environ.get("DEBUG") == "True":
    print("Local Server Running.......")
    DEBUG = True
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins for local development
    CSRF_TRUSTED_ORIGINS = [
        "http://localhost:4200", 
        "http://127.0.0.1:8000", 
        "https://searcehiringchallenge.onrender.com"
    ]
else:
    print("Deployment Server Running.......")
    DEBUG = False
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_ALL_ORIGINS = False
    CSRF_TRUSTED_ORIGINS = [
        "http://localhost:4200",
        "http://127.0.0.1:8000",
        "https://searcehiringchallenge.onrender.com",
    ]

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

APPEND_SLASH = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = 'static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



# 1N 2H 3MK 4MD