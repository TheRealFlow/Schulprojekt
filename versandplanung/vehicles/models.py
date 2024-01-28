from django.db import models

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    brandName = models.CharField(max_length=50)
    modelName = models.CharField(max_length=50)
    modelYear = models.IntegerField()
    initalRegistration = models.DateField()
    licensePlate = models.CharField(max_length=10)
    