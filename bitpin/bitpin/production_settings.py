from .settings import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "bitpin_db",
        "USER": "bitpin_usr",
        "PASSWORD": "root",
        "HOST": "bitpin-db-service",
        "PORT": "5432",
        "TEST": {
            "NAME": "bitpin_test_db",
        },
    }
}
