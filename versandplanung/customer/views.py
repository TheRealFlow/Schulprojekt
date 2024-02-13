from django.shortcuts import render


def view_customers(request):
    customers = [
        {
            'id': '1',
            'first_name': 'Max',
            'last_name': 'Mustermann',
            'city': 'Musterstraße 1, 12345 Musterstadt',
            'email': 'max.mustermann@test.com'
        },
        {
            'id': '2',
            'first_name': 'Erika',
            'last_name': 'Mustermann',
            'city': 'Musterstraße 2, 12345 Musterstadt',
            'email': 'erika.mustermann@test.com'
        },
        {
            'id': '3',
            'first_name': 'Hans',
            'last_name': 'Mustermann',
            'city': 'Musterstraße 3, 12345 Musterstadt',
            'email': 'hans.mustermann@test.com'
        }
    ]

    return render(request, 'customers.html', {
        'customers': customers
    })
