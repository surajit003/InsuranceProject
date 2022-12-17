from simple_history.models import HistoricalRecords

from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from api.v1.common.models import UUIDModel, TimeTrackedModel
from api.v1.customer.models import Customer


class Policy(TimeTrackedModel, UUIDModel):
    STATUS_NEW = 0
    STATUS_ACCEPTED = 1
    STATUS_ACTIVE = 2

    POLICY_STATUS_CHOICES = (
        (STATUS_NEW, "New"),
        (STATUS_ACCEPTED, "Accepted"),
        (STATUS_ACTIVE, "Active"),
    )

    type = models.CharField(_("Policy Type"), max_length=120)
    premium = models.IntegerField(_("Premium Amount"))
    cover = models.IntegerField(_("Cover"))
    state = models.PositiveSmallIntegerField(
        choices=POLICY_STATUS_CHOICES, default=STATUS_NEW, db_index=True
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_index=True)

    history = HistoricalRecords()

    def __str__(self):
        return f"Policy for {self.customer} for cover {self.cover}"
