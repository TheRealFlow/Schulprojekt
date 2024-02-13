from django.shortcuts import render


def view_orders(request):
    orders = [
        {
            'orderNumber': '123',
            'customerId': 1,
            'articles': [
                {
                    'id': '1',
                    'name': 'Article 1',
                    'count': 5
                },
                {
                    'id': '2',
                    'name': 'Article 2',
                    'count': 10
                }
            ],
            'address': 'Musterstraße 1, 12345 Musterstadt',
            'status': 'open',
            'total': 105.50
        },
        {
            'orderNumber': '124',
            'customerId': 2,
            'articles': [
                {
                    'id': '1',
                    'name': 'Article 1',
                    'count': 3
                },
                {
                    'id': '2',
                    'name': 'Article 2',
                    'count': 8
                }
            ],
            'address': 'Musterstraße 2, 12345 Musterstadt',
            'status': 'in progress',
            'total': 62.75
        },
        {
            'orderNumber': '125',
            'customerId': 3,
            'articles': [
                {
                    'id': '1',
                    'name': 'Article 1',
                    'count': 7
                },
                {
                    'id': '2',
                    'name': 'Article 2',
                    'count': 12
                }
            ],
            'address': 'Musterstraße 3, 12345 Musterstadt',
            'status': 'shipped',
            'total': 100.00
        },
        {
            'orderNumber': '126',
            'customerId': 4,
            'articles': [
                {
                    'id': '1',
                    'name': 'Article 1',
                    'count': 4
                },
                {
                    'id': '2',
                    'name': 'Article 2',
                    'count': 9
                }
            ],
            'address': 'Musterstraße 4, 12345 Musterstadt',
            'status': 'delivered',
            'total': 25.99
        }
    ]

    return render(request, 'orders.html', {
        'orders': orders,
    })
