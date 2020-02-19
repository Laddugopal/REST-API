from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from laddu_rest_api import serializers

# Create your views here.


class HelloApiView(APIView):
    '''
        Create Api View
        
    '''
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """
        Return API View features
        """
        
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        
        return Response({'message':'Hare Krishna','an_apiview':an_apiview})
    
    def post(self, request):
        '''
            function to create a hello message with our name        
        '''
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return  Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    ''' test hello view set'''
    def list(self, request):
        ''' Thi will return a sample view message'''
        a_viewset = [
            "Sample view set for user action (list create restrict update destroy )",
            "Hare Krishna Hare Krishna",
            
        ]
        return Response({'message': 'Hare Krishna Hare Ram',"a_viewset":a_viewset})