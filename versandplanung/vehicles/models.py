from collections.abc import Iterable
from django.db import models


class VehicleManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using('vehicles')


class Vehicle(models.Model):
    STATUS_CHOICES = (
        ('free', 'Frei'),
        ('on tour', 'Auf Tour'),
        ('garage', 'Werkstatt'),
    )

    id = models.AutoField(primary_key=True)
    brandName = models.CharField(max_length=50)
    modelName = models.CharField(max_length=50)
    modelYear = models.IntegerField()
    initalRegistration = models.DateField()
    licensePlate = models.CharField(max_length=10)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='free')

    # doing this allows to call Vehicle.objects.all() instead of Vehicle.objects.using('vehicles').all()
    objects = VehicleManger()

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        return super().save(force_insert, force_update, using, update_fields).using('vehicles')
