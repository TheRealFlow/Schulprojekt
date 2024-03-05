from django.shortcuts import render

from versandplanung.orders.models import Orders


def view_orders(request):
    orders = []
    orders = Orders.objects.all()

    return render(request, 'orders.html', {
        'orders': orders
    })
