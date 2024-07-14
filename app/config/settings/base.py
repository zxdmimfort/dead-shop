from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = ["127.0.0.1"]

INTERNAL_IPS = ["127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.products",
    "apps.users",
    "apps.categories",
    "apps.cart",
    "apps.order",
    "debug_toolbar",
    "mptt",
    "django_elasticsearch_dsl",
    "storages",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "postgres"),
        "USER": os.getenv("POSTGRES_USER", "postgres"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "postgres"),
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "PORT": os.getenv("POSTGRES_PORT", 5432),
    }
}


USE_S3 = os.getenv("USE_S3") == "TRUE"

if USE_S3:
    AWS_ACCESS_KEY_ID = os.getenv("MINIO_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("MINIO_SECRET_KEY")
    AWS_DEFAULT_ACL = None
    AWS_STORAGE_BUCKET_NAME = os.getenv("MINIO_BUCKET_NAME")
    AWS_S3_CUSTOM_DOMAIN = os.getenv("MINIO_S3_CUSTOM_DOMAIN")
    AWS_S3_ENDPOINT_URL = os.getenv("MINIO_ENDPOINT")
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
    # s3 static settings
    STATIC_LOCATION = "static"
    STATIC_URL = f"http://{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/{STATIC_LOCATION}/"
    STATICFILES_STORAGE = "config.storage_backends.StaticStorage"
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = "media"
    MEDIA_URL = f"http://{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/{PUBLIC_MEDIA_LOCATION}/"
    DEFAULT_FILE_STORAGE = "config.storage_backends.PublicMediaStorage"
else:
    STATIC_DIR = BASE_DIR.parent
    STATIC_URL = "/static/"
    STATIC_ROOT = STATIC_DIR / "static/"
    MEDIA_URL = "/media/"
    MEDIA_ROOT = STATIC_DIR / "media/"

STATICFILES_DIRS = [
    BASE_DIR / "static/",
]

    # STORAGES = {
    #     "default": {
    #         "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    #         "OPTIONS": {
    #             "bucket_name": AWS_STORAGE_BUCKET_NAME,
    #             "access_key": os.getenv("MINIO_ACCESS_KEY_ID"),
    #             "secret_key": os.getenv("MINIO_SECRET_KEY"),
    #             "endpoint_url": os.getenv("MINIO_ENDPOINT"),
    #             "location": "media/",
    #             "querystring_auth": False,
    #             "use_ssl": False,
    #             },
    #     },
    #     "staticfiles": {
    #         # "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    #         "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    #         "OPTIONS": {
    #             "bucket_name": AWS_STORAGE_BUCKET_NAME,
    #             "access_key": os.getenv("MINIO_ACCESS_KEY_ID"),
    #             "secret_key": os.getenv("MINIO_SECRET_KEY"),
    #             "endpoint_url": os.getenv("MINIO_ENDPOINT"),
    #             # "location": "static/",
    #         },
    #     },
    # }

ELASTICSEARCH_DSL = {
    "default": {
        "hosts": f"http://{os.getenv('ELASTIC_HOST')}:{os.getenv('ELASTIC_PORT')}",  # Use https if TLS is enabled on Elasticsearch
        "http_auth": (os.getenv("ELASTIC_USER"), os.getenv("ELASTIC_PASSWORD")),
    },
}
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.mail.ru"
EMAIL_PORT = 2525
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


LOGIN_REDIRECT_URL = "products:index"
LOGIN_URL = "users:sign_in"
LOGOUT_REDIRECT_URL = "products:index"

AUTH_USER_MODEL = "users.Client"
USER_SESSION_ID = "proxy_user"
