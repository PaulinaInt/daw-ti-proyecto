from django.db import models

# Create your models here.
class Portfolio (models.Model):
    pass

class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    titulo_academico = models.CharField(max_length=100)
    biografia = models.TextField()
    correo_electronico = models.EmailField()
    dedicacion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
