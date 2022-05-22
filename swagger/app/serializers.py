from rest_framework import serializers
from . import models


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alumno
        fields = '__all__'


class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clase
        fields = '__all__'