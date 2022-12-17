from rest_framework import serializers

from api.v1.policy.models import Policy


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ["customer_id", "type"]
