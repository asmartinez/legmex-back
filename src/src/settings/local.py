from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'elasticSearch',
            'USER': 'dev',
            'PASSWORD': 'dev',
            'HOST': 'localhost',
            'PORT': 5434,
        }
}


STATIC_URL = '/static/'

AUTH_USER_MODEL = 'persona.User'
