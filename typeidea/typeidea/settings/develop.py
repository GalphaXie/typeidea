import dotenv
from .base import *  # NOQA


dotenv.read_dotenv("/home/user/venvs/typeidea-env/conf/.env")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ["DB_NAME"],
        'HOST': os.environ.get("DB_HOST", "127.0.0.1"),
        'PORT': int(os.environ.get("DB_PORT", 3306)),
        'USER': os.environ["DB_USER"],
        'PASSWORD': os.environ["DB_PASSWORD"],
        # 'CONN_MAX_AGE': 5 * 60,  # <= wait_time # None
        # 'OPTIONS': {'charset': 'utf8mb4'}
    }
}

INSTALLED_APPS += [
    'debug_toolbar',
    # 'pympler'
    # 'debug_toolbar_line_profiler',
    # 'silk'
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'silk.middleware.SilkyMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']
STATIC_ROOT = os.path.join("/home/user/venvs/typeidea-env", 'static_files')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(module)s:'
                      '%(funcName)s:%(lineno)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'typeidea.log',
            'formatter': 'default',
            'maxBytes': 1024 * 1024,  # 1M
            'backupCount': 5,
        },

    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
