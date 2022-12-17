from rest_framework import serializers

from api.v1.customer.exceptions import CustomerDoesNotExistException
from api.v1.customer.models import Customer
from api.v1.policy.models import Policy


class QuoteSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField(source="customer")

    class Meta:
        model = Policy
        fields = ["customer_id", "type"]

    def create(self, validated_data):
        customer_id = validated_data.get("customer")
        type_ = validated_data.get("type")
        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            raise CustomerDoesNotExistException
        return Policy.objects.create(type=type_, customer=customer)
