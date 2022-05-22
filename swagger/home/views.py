from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status

from . import models
from . import serializers

# Create your views here.


class HomeView(generics.ListAPIView):

    queryset = models.Home.objects.all()
    serializer_class = serializers.HomeSerializer

    def get(self, request):
        alumnos = self.get_serializer(self.get_queryset(), many=True)
        response = {
            'success': True,
            'message': 'Lista de alumnos',
            'data': alumnos.data
        }
        return Response(response, status=status.HTTP_200_OK)