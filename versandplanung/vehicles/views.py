from django.shortcuts import render


def view_vehicles(request):
    vehicles = [
        {
            'id': '1',
            'brandName': 'Mercedes-Benz',
            'modelName': 'Actros',
            'licensePlate': 'HRO-JL 1234',
            'status': 'free'
        },
        {
            'id': '2',
            'brandName': 'MAN',
            'modelName': 'TGE',
            'licensePlate': 'HRO-JL 4321',
            'status': 'on tour'
        },
        {
            'id': '3',
            'brandName': 'Volvo',
            'modelName': 'FMX',
            'licensePlate': 'HRO-JL 1001',
            'status': 'garage'
        }
    ]

    return render(request, 'vehicles.html', {
        'vehicles': vehicles
    })
