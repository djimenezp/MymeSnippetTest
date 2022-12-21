import os

from .settings import *

assert BASE_DIR
SECRET_KEY = os.environ.get("SECRET_KEY", "foo")
DEBUG = int(os.environ.get("DEBUG", default=1))
ALLOWED_HOSTS = ['*']

STATIC_ROOT = BASE_DIR / 'static'
