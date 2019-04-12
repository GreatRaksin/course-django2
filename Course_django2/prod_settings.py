import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '#nzz6!b4tnqyow@2i^-i4ry9dgfd#@%#%dggh@%#YH463r02!=(0-%^'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'course',
       'USER': 'userdb',
       'PASSWORD': '123456',
       'HOST': 'localhost',
       'PORT': '5432',
        'TEST': {
            'NAME': 'test_db',
        },
   }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'