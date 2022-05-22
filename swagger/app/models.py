from django.db import models

# Create your models here.


class Alumno(models.Model):
    alumno_id = models.AutoField(primary_key=True)
    alumno_nombre = models.CharField(max_length=50, verbose_name="Nombre alumno")
    alumno_apellido = models.CharField(max_length=50, verbose_name="Apellido alumno")

    def __str__(self):
        return self.alumno_nombre;


class Clase(models.Model):
    clase_id = models.AutoField(primary_key=True)
    clase_nombre = models.CharField(max_length=50, verbose_name="Nombre clase")

    def __str__(self):
        return self.clase_nombre;