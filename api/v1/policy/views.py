from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.customer.exceptions import CustomerDoesNotExistException
from api.v1.policy.serializers import QuoteSerializer


class QuoteAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = QuoteSerializer(data=data)
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
