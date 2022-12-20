from django.db.models.signals import post_save, pre_save
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


@receiver(post_save, sender=Policy)
def policy_calculation(sender, instance, created, **kwargs):
    if created:
        # just a dummy policy criteria based on age
        age = instance.customer.age
        cover = 2000000
        premium = cover / 24 if age > 18 else 0
        instance.cover = cover
        instance.premium = premium
        instance.save()
