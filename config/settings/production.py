from os import getenv, path

from dotenv import load_dotenv

from .base import * #noqa

from .base import BASE_DIR

local_env_file = path.join(BASE_DIR, ".envs", ".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  getenv("DJNAGO_SECRET_KEY",)

DEBUG = True

ALLOWED_HOSTS = []

DOMAIN = getenv("DOMAIN")
