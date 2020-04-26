from .base import *  # NOQA


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
        'CONN_MAX_AGE': os.environ.get("CONN_MAX_AGE", 60),
        'OPTIONS': {
            'charset': 'utf8mb4'
        }
    },
}

CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get("REDIS_URL", '127.0.0.1:6379:1'),
        "TIMEOUT": 300,
        "OPTIONS": {
            'PASSWORD': os.environ.get("REDIS_PASSWORD", ""),
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
    }
}

ADMINS = MANAGERS = (
    ("姓名", "<邮件地址>"),
)

# EMAIL_HOST = '<邮件smtp服务地址>'
# EMAIL_HOST_USER = '<邮箱登录名>'
# EMAIL_HOST_PASSWORD = '<邮箱登录密码>'
# EMAIL_SUBJECT_PREFIX = '<邮件标题前缀>'
# DEFAULT_FROM_EMAIL = '<邮件展示发件人的地址>'
# SERVER_EMAIL = '<邮件服务器>'

STATIC_ROOT = '/tmp/static'


REDIS_URL = '127.0.0.1:6379:1'

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
            'filename': '/tmp/logs/typeidea.log',
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