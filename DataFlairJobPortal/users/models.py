from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=150, verbose_name='First Name')
    surname = models.CharField(max_length=150, verbose_name='surname')
    user_type=models.CharField(max_length=20,null=False)
    location=models.CharField(max_length=200,null=True)
    is_active = models.BooleanField(default=True)
    date_of_birth = models.DateTimeField(null=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","surname"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
