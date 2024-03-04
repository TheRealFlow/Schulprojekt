from django.shortcuts import render
from versandplanung.vehicles.models import Vehicle


def view_vehicles(request):
    vehicles = Vehicle.objects.all()

    return render(request, 'vehicles.html', {
        'vehicles': vehicles
    })
