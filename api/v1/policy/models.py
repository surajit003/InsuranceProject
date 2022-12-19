from simple_history.models import HistoricalRecords

from django.db import models
from django.utils.translation import gettext_lazy as _

from api.v1.common.models import UUIDModel, TimeTrackedModel
from api.v1.customer.models import Customer


class Policy(TimeTrackedModel, UUIDModel):
    STATUS_NEW = "new"
    STATUS_ACCEPTED = "accepted"
    STATUS_ACTIVE = "active"

    POLICY_STATUS_CHOICES = (
        (STATUS_NEW, "New"),
        (STATUS_ACCEPTED, "Accepted"),
        (STATUS_ACTIVE, "Active"),
    )

    type = models.CharField(_("Policy Type"), max_length=120)
    premium = models.IntegerField(_("Premium Amount"), null=True, blank=True)
    cover = models.IntegerField(_("Cover"), null=True, blank=True)
    state = models.CharField(
        choices=POLICY_STATUS_CHOICES, default=STATUS_NEW, db_index=True, max_length=20
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_index=True)

    history = HistoricalRecords()

    def __str__(self):
        return f"Policy for {self.customer} for cover {self.cover}"

    class Meta:
        verbose_name_plural = "Policies"
