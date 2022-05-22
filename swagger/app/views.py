from rest_framework.response import Response
from rest_framework import generics, status

from . import models
from . import serializers

# Create your views here.


class AlumnoView(generics.CreateAPIView):

    queryset = models.Alumno.objects.all()
    serializer_class = serializers.AlumnoSerializer

    def get(self, request):
        alumnos = self.get_serializer(self.get_queryset(), many=True)
        response = {
            'success': True,
            'message': 'Lista de alumnos',
            'data': alumnos.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        nuevoAlumno = self.get_serializer(data=request.data)
        if nuevoAlumno.is_valid():
            nuevoAlumno.save()
            response ={
                'success': True,
                'message': 'Alumno creado',
                'data': nuevoAlumno.data
            }
            return Response(response)
        return Response(nuevoAlumno.errors)
    
class ClaseView(generics.ListAPIView):

    queryset = models.Clase.objects.all()
    serializer_class = serializers.ClaseSerializer

    def get(self, request):
        clases = self.get_serializer(self.get_queryset(), many=True)
        response = {
            'success': True,
            'message': 'Lista de clases',
            'data': clases.data
        }
        return Response(response)