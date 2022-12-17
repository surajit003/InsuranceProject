from rest_framework import serializers

from api.v1.customer.exceptions import CustomerDoesNotExistException
from api.v1.customer.models import Customer
from api.v1.policy.models import Policy


class QuoteSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField(source="customer")

    class Meta:
        model = Policy
        fields = [
            "customer_id",
            "type",
            "cover",
            "premium",
        ]

    def _generate_policy_criteria(self, customer):
        age = customer.age
        cover = 0
        premium = 0
        if age > 18:
            # some random data
            cover = 200000
            total_duration = 24
            premium = cover / total_duration  # premium per month
        return cover, premium

    def create(self, validated_data):
        customer_id = validated_data.get("customer")
        type_ = validated_data.get("type")
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            raise CustomerDoesNotExistException
        premium, cover = self._generate_policy_criteria(customer)
        return Policy.objects.create(
            type=type_, customer=customer, premium=premium, cover=cover
        )
