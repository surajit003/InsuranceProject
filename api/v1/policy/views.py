from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from django_filters import rest_framework as filters

from .exceptions import InvalidPolicyStateError
from .filters import PolicyFilterSet
from .models import Policy
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.customer.exceptions import CustomerDoesNotExistException
from api.v1.policy.serializers import (
    PolicyCreateSerializer,
    PolicyWithCustomerDetailSerializer,
    PolicyPutOrPatchSerializer,
)


class PolicyAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = PolicyCreateSerializer(data=data)
        if serializer.is_valid():
            validated_data = dict(serializer.validated_data)
            try:
                serializer.create(validated_data)
            except CustomerDoesNotExistException:
                return Response(
                    {"detail": "CustomerNotFound"}, status=status.HTTP_400_BAD_REQUEST
                )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PolicyListAPIView(ListAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicyWithCustomerDetailSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PolicyFilterSet


class PolicyRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Policy.objects.all()
    serializer_class = PolicyWithCustomerDetailSerializer
    lookup_field = "uuid"
    action = "retrieve"

    def patch(self, request, *args, **kwargs):
        policy = Policy.objects.filter(uuid=str(kwargs.get("uuid"))).first()
        serializer = PolicyPutOrPatchSerializer(
            instance=policy, data=request.data, partial=True
        )
        if serializer.is_valid():
            validated_data = dict(serializer.validated_data)
            try:
                policy = serializer.update(policy, validated_data)
            except InvalidPolicyStateError:
                return Response(data={"detail": "Invalid state change requested"})
            policy_dict = PolicyPutOrPatchSerializer(policy)
            return Response(data=policy_dict.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
