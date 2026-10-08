from django.db import models

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_documento = models.CharField(max_length=20, blank=True, default='')
    numero_documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, default='')
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, default='')
    fecha = models.DateField(blank=True, null=True)
    asistencia = models.BooleanField(default=False)
