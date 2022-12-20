from rest_framework import serializers

from api.v1.customer.exceptions import CustomerDoesNotExistException
from api.v1.customer.models import Customer
from api.v1.customer.serializers import CustomerSerializer
from api.v1.policy.exceptions import InvalidPolicyStateError
from api.v1.policy.models import Policy

STATUS_MAP = {
    "0": "New",
    "1": "Accepted",
    "2": "Paid",
}


class PolicyCreateSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField(source="customer")

    class Meta:
        model = Policy
        fields = [
            "type",
            "customer_id",
        ]

    @staticmethod
    def _generate_policy_criteria(customer):
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


class PolicyBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = [
            "cover",
            "premium",
            "state",
            "type",
            "uuid",
        ]


class PolicyWithCustomerDetailSerializer(PolicyBaseSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Policy
        fields = PolicyBaseSerializer.Meta.fields + [
            "customer",
        ]


class PolicyPutOrPatchSerializer(PolicyBaseSerializer):
    def update(self, instance, validated_data):
        if self.partial:
            # This is a bad idea to manage state transition like this. django-fsm is a good library
            # to use in this scenario
            if "state" in validated_data:
                self._check_policy_state(validated_data, instance)
            policy = Policy.objects.get(id=instance.id)
            # as of now it only makes sense to update the state as this is based on the user feedback if they accept
            # or not
            policy.state = validated_data.get("state", instance.state)
            policy.save()
            return policy

    @staticmethod
    def _check_policy_state(validated_data, instance):

        policy = Policy.objects.filter(id=instance.id).first()
        current_state = policy.state

        target_state = validated_data.get("state")

        if current_state == "active" and target_state == "accepted":
            raise InvalidPolicyStateError

        if target_state == "active":
            if current_state == "new":
                raise InvalidPolicyStateError

        elif target_state == "new" and current_state in ["active", "accepted"]:
            raise InvalidPolicyStateError
        return True
