from django.utils.translation import gettext_lazy as _
from django.db import models

from api.v1.common.models import TimeTrackedModel, UUIDModel


class Customer(TimeTrackedModel, UUIDModel):
    first_name = models.CharField(_("FirstName"), max_length=120)
    last_name = models.CharField(_("LastName"), max_length=120)
    dob = models.DateField(_("DateofBirth"))

    # use to mark a customer as inactive in case the customer doesnot pay the premium to prevent access to the
    # insurance portal
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"
