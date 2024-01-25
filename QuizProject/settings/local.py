from decouple import config

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '../db.sqlite3',  # This is where you put the name of the db file.
        # If one doesn't exist, it will be created at migration time.
    }
    # "default": {
    #     "ENGINE": config("SQL_ENGINE"),
    #     "NAME": config("SQL_DATABASE"),
    #     "USER": config("SQL_USER"),
    #     "PASSWORD": config("SQL_PASSWORD"),
    #     "HOST": config("SQL_HOST"),
    #     "PORT": config("SQL_PORT"),
    # }
}
