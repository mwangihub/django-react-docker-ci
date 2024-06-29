from .base import *  # noqa: F403
from .base import INSTALLED_APPS
from .base import MIDDLEWARE
from .base import env

env.read_env(str(BASE_DIR / ".env"))

DEBUG = True

SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]  # noqa: S104

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    },
}

EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend",
)

INSTALLED_APPS = ["whitenoise.runserver_nostatic", *INSTALLED_APPS]

CELERY_TASK_EAGER_PROPAGATES = True
