import os

from .settings import *

assert BASE_DIR

# SECURE_HSTS_SECONDS = 60
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# CSRF_TRUSTED_ORIGINS = ['https://*.127.0.0.1', 'https://*.localhost']
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECRET_KEY = os.environ.get("SECRET_KEY", "foo")
DEBUG = int(os.environ.get("DEBUG", default=0))
ALLOWED_HOSTS = ['*']

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}
