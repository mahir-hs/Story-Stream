from .base import *  # noqa
from .base import env
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY", default="chZIQt7UZG9osmynnqWFfsxC0_ZimzgrUToFHUwfVV8Q6U6zXW8",)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]


