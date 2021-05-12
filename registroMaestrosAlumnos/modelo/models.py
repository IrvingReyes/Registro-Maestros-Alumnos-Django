from django.db import models

# Create your models here.

class Maestro(models.Model):
	nombre = models.CharField(max_length=51)
	direccion = models.CharField(max_length=50)
	telefono = models.BigIntegerField()

class Alumno(models.Model):
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50)
	maestro = models.ForeignKey(Maestro, on_delete=models.CASCADE)
	salon = models.CharField(max_length=50)
