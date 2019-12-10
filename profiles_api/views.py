from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    serializer_class=serializers.HelloSerializer
    
    def get(self, request, format=None):
        return Response({'message':'Hello'})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            return Response({'message': name})