from .settings import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "bitpin_db",
        "USER": "bitpin_usr",
        "PASSWORD": "root",
        "HOST": "bitpin_db",
        "PORT": "",
        "TEST": {
            "NAME": "bitpin_test_db",
        },
    }
}
