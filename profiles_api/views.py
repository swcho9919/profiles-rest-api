from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api.api import serializers


class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns a list of APIView features"""
        an_apiview = [
            'uses HTTp methods as function (get, post, patch, put, delete)'
            'is similar to a traditional Django view'
            'Gives you the mose control over your application logic'
            'is mapped manually to URLs'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':"PUT"})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PUT'})
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})