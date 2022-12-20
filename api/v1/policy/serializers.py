from rest_framework import serializers

from api.v1.customer.exceptions import CustomerDoesNotExistException
from api.v1.customer.models import Customer
from api.v1.customer.serializers import CustomerSerializer
from api.v1.policy.exceptions import InvalidPolicyStateError
from api.v1.policy.models import Policy


class PolicyCreateSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField(source="customer")

    def validate(self, data):
        if "customer" in data:
            customer_id = data.get("customer")
            # check if customer exist
            customer = Customer.objects.filter(id=customer_id).first()
            if not customer:
                raise serializers.ValidationError(
                    f"Customer with Id {customer_id} doesnot exist"
                )
        return data

    def create(self, validated_data):
        customer = Customer.objects.get(id=validated_data.get("customer"))
        type_ = validated_data.get("type")
        return Policy.objects.create(type=type_, customer=customer)

    class Meta:
        model = Policy
        fields = [
            "type",
            "customer_id",
        ]


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
    def validate(self, data):
        # very bad idea to manage state transition in if-else blocks
        if "state" not in data:
            return data
        policy = Policy.objects.filter(id=self.instance.id).first()
        current_state = policy.state

        target_state = data.get("state")

        if current_state == "active" and target_state == "accepted":
            raise serializers.ValidationError(
                f"Cannot transition policy state from {current_state} to {target_state}"
            )

        if target_state == "active":
            if current_state == "new":
                raise serializers.ValidationError(
                    f"Cannot transition policy state from {current_state} to {target_state}"
                )

        elif target_state == "new" and current_state in ["active", "accepted"]:
            raise serializers.ValidationError(
                f"Cannot transition policy state from {current_state} to {target_state}"
            )
        return data
