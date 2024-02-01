from django.shortcuts import render
from .articles.models import Articles
from .customer.models import Customer
from .orders.models import Orders
from .vehicles.models import Vehicle


def index(request):
    articles = Articles.objects.all()
    customers = Customer.objects.all()
    orders = Orders.objects.all()
    vehicles = Vehicle.objects.all()

    return render(request, 'index.html', {
        'articles': articles,
        'customers': customers,
        'orders': orders,
        'vehicles': vehicles
    })
