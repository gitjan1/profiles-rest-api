from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    """Test API View"""

    def get(self, request, format=None):
        """"Returns a list of APIView"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, put, patch, delete)',
            'IS similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
         ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
