from django.db import models

# Create your models here.
class Servicio(models.Model):
	nombre=models.CharField(max_length=150)
	categoria=models.CharField(max_length=150)