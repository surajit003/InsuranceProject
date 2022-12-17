from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.policy.serializers import PolicySerializer


class PolicyAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = PolicySerializer(data=data)
        if serializer.is_valid():
            validated_data = dict(serializer.validated_data)
            serializer.create(validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
