from .base import *  # noqa: F403

DEBUG = False

ALLOWED_HOSTS = ["scvready.online"]
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
# CORS_ORIGIN_ALLOW_ALL = True
