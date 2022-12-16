from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


from api.v1.accounts.managers import UserManager
from api.v1.common.models import TimeTrackedModel


class CustomUser(AbstractUser, TimeTrackedModel):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
