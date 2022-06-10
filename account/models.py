from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    # email = models.EmailField(
    #     max_length=255,
    #     unique=True
    # )
    # avatar = models.ImageField(
    #     upload_to="",
    #     null=True,
    #     default='default/avatar.svg'
    # )
    #
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
