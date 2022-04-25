from django.contrib.auth.models import AbstractBaseUser, AbstractUser

# from .managers import CustomUserManager


class CustomUser(AbstractUser):
    ...

    # objects = CustomUserManager()
