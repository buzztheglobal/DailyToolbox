"""
Django settings for DailyToolboxBackend project.

Generated by 'django-admin startproject' using Django 5.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""
import os # Make sure this is at the top
from pathlib import Path
import firebase_admin
from firebase_admin import credentials

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Add your Firebase path AFTER BASE_DIR is defined
FIREBASE_SERVICE_ACCOUNT_KEY_PATH = os.path.join(BASE_DIR, 'firebase-adminsdk.json')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#f9d_zfay5tmpilaczr$iz&gfgszqhl+_k6zn!=x-op&vqkps!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',        # Add this
    'corsheaders',           # Add this
    'menu', # <--- Add your 'menu' app here
    'core',                  # Add your new 'core' app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
     'corsheaders.middleware.CorsMiddleware', # Add this
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DailyToolboxBackend.urls'

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

WSGI_APPLICATION = 'DailyToolboxBackend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
# Database - PostgreSQL configuration
# superuser: admin123, password: admin123

# Replace the existing DATABASES setting with this one

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dailytoolbox_db',
        'USER': 'dailytoolbox_user',
        'PASSWORD': 'dailytoolbox_user', # Use the password you create
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

"""
Server [localhost]:
Database [postgres]:
Port [5432]:
Username [postgres]:
Password for user postgres: admin123 [superuser password]
https://gemini.google.com/app/e58cff66245cab52
"""

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000", # Adjust to your frontend port
    "http://127.0.0.1:3000",
]
# Or for simplicity during initial development (BE CAREFUL IN PROD):
# CORS_ALLOW_ALL_ORIGINS = True

# Initialize Firebase Admin SDK
try:
    cred = credentials.Certificate(FIREBASE_SERVICE_ACCOUNT_KEY_PATH)
    firebase_admin.initialize_app(cred)
    print("Firebase Admin SDK initialized successfully!")
except Exception as e:
    print(f"Error initializing Firebase Admin SDK: {e}")
    print("Ensure 'firebase-adminsdk.json' is in the backend directory and is valid.")

# Authentication Backends for Firebase
AUTHENTICATION_BACKENDS = [
    'core.backends.FirebaseAuthenticationBackend', # Add this line (will create in 0.4)
    'django.contrib.auth.backends.ModelBackend', # Keep default Django auth
]