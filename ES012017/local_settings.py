import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'es012017',
        'USER': 'es012017',
        'PASSWORD': 'senhatop',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = True