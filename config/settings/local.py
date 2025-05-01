
from os import getenv, path

from dotenv import load_dotenv

from .base import * #noqa

from .base import BASE_DIR

local_env_file = path.join(BASE_DIR, ".envs", ".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)
    
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-_%=)$g=0s^-u3z(^9$ofhf7))pha)&0d19)c9wmpg7de72v2th'
SECRET_KEY = getenv("DJNAGO_SECRET_KEY","NSdeDnb1QeYD2aMEaURpC2JJgg5wOPX6SQdVoNX55O_Vekn6x7s")


ALLOWED_HOSTS = ["localhost","127.0.0.1","0.0.0.0"]

ADMIN_URL = getenv("DJANGO_ADMIN_URL")


#Logg config

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(name)-12s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}