from .base import *  # NOQA

REDIS_URL = os.environ.get("REDIS_URL", '127.0.0.1:6379:1')

DEBUG = False

ALLOWED_HOSTS = ["typeidea.com"]

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ["DB_NAME"],
        'HOST': os.environ["DB_HOST"],
        'PORT': os.environ["DB_PORT"],
        'USER': os.environ["DB_USER"],
        'PASSWORD': os.environ["DB_PASSWORD"],
        'CONN_MAX_AGE': 5 * 60,
        'OPTIONS': {
            'charset': 'utf8mb4'
        }
    },
}

CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "TIMEOUT": 300,
        "OPTIONS": {
            # 'PASSWORD': '<password>',
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
    }
}
