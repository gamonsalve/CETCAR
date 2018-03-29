from django.db import models

# Create your models here.
class Servicio(models.Model):
	nombre=models.CharField(max_length=150)
	categoria=models.CharField(max_length=150)

class SensorData(models.Model):
	sensor_id=models.CharField(max_length=5)
	bus_id=models.CharField(max_length=7)
	counter=models.PositiveIntegerField()