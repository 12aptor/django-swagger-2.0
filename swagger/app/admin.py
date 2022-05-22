from django.contrib import admin

from .models import Clase, Alumno

# Register your models here.


# Añadimos estas dos líneas para que podamos usarlo desde el admin
admin.site.register(Alumno)
admin.site.register(Clase)