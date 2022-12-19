from django.db.models.signals import post_save
from django.dispatch import receiver

from api.v1.policy.models import Policy


@receiver(post_save, sender=Policy)
def trigger_payment(sender, instance, **kwargs):
    policy = Policy.objects.filter(id=instance.id).first()
    if policy.state == Policy.STATUS_ACCEPTED:
        print("Payment has been triggered...")
        print("Simulating customer has made the payment....")
        policy.state = Policy.STATUS_ACTIVE
        policy.save()
