from uuid import uuid4

from django.db import models
from django.utils import timezone


class TimeTrackedModel(models.Model):
    created = models.DateTimeField(default=timezone.now, editable=False, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    """
    Abstract model with uuid field.
    """

    uuid = models.UUIDField(default=uuid4, unique=True)

    class Meta:
        abstract = True
