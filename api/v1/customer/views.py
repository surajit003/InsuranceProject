from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters import rest_framework as filters

from api.v1.customer.filters import CustomerFilterSet
from api.v1.customer.models import Customer
from api.v1.customer.serializers import CustomerSerializer


class CustomerCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            validated_data = dict(serializer.validated_data)
            serializer.create(validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerListAPIView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CustomerFilterSet


class CustomerRetrieveAPIView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = "uuid"
    action = "retrieve"
