import os

from .settings import *

assert BASE_DIR
SECRET_KEY = os.environ.get("SECRET_KEY", "foo")
DEBUG = int(os.environ.get("DEBUG", default=1))
ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}
STATIC_ROOT = BASE_DIR / 'static'
