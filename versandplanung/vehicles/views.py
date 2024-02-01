from django.shortcuts import render
from .models import Vehicle


def view_vehicles(request):
    vehicles = Vehicle.objects.all().using('vehicles')
    return render(request, 'vehicle.html', {
        'vehicles': vehicles
    })
