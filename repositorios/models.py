from django.db import models
from django.contrib.auth.hashers import make_password

# Create your modelmodels.Model.

class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=32)

class Repositorio(models.Model):
    titulo=models.CharField(max_length=500, null=True)
    descripcion=models.CharField(max_length=500, null=True)
    #watch=models.CharField(max_length=20, null=True)
    star=models.IntegerField(null=True)
    fork=models.IntegerField(null=True)
    fecha_creacion = models.DateField(max_length=100, null=True)
    fecha_actualizacion = models.CharField(max_length=100, null=True)
    url_commits = models.CharField(max_length=500, null=True)
    url_colaboradores=models.CharField(max_length=500, null=True)
    url_lenguajes = models.CharField(max_length=500, null=True)
    url_repositorio=models.CharField(max_length=500, null=True)



