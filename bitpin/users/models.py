
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.utils.translation import gettext_lazy as _

# from .managers import CustomUserManager


class CustomUser(AbstractUser):
    ...

    # objects = CustomUserManager()
