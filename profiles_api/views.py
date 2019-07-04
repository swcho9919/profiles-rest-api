from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """returns a list of APIView features"""
        an_apiview = [
            'uses HTTp methods as function (get, post, patch, put, delete)'
            'is similar to a traditional Django view'
            'Gives you the mose control over your application logic'
            'is mapped manually to URLs'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})