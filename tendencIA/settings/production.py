from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['wrossi.pythonanywhere.com/']


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.sqlite3',
 'NAME':
os.path.join(os.path.dirname(BASE_DIR),'db_sqlite3'),
 }
}