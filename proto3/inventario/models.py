from django.db import models

# Create your models here.
class Moto(models.Model):
    marca = models.CharField(max_length=120) # Define un campo de texto para almacenar la marca de la moto, con una longitud máxima de 120 caracteres 
    cantidad = models.IntegerField() # Define un campo entero para almacenar la cantidad de motos
    barrio = models.CharField(max_length=120)
    mes = models.CharField(max_length=120)