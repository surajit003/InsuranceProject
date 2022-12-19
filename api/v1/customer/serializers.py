from rest_framework import serializers

from api.v1.customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "first_name",
            "last_name",
            "dob",
            "uuid",
        ]
