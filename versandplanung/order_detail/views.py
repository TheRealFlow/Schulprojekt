import csv
from os import path
import random
from django.shortcuts import render, get_object_or_404
from versandplanung.orders.models import Orders
from versandplanung.settings import BASE_DIR
from versandplanung.vehicles.models import Vehicle


def order_detail(request, order_id):
    order = get_object_or_404(Orders, id=order_id)

    articles = []
    for article in order.articles:
        for key, items in article.items():
            articles.append(list([key, items]))
        
    customer_data = {}
    try:
        customer_file = 'datasources/customer_data.csv'
        path_to_redemption = path.join(BASE_DIR, customer_file)
        with open(path_to_redemption, 'r', encoding='UTF-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # \ufeffUserId is some random windows bullshit
                if int(row.get('\ufeffUserId', row.get('UserId', '0'))) == order.customerId:
                    customer_data = row
                    break
    except (FileExistsError, FileNotFoundError) as error:
        print(error)

    free_vehicles = None
    on_tour_vehicle = None
    random_vehicle = None

    if order.status == 'open':
        free_vehicles = Vehicle.objects.filter(status='free')
    elif order.status == 'in progress' or order.status == 'shipped':
        on_tour_vehicles = Vehicle.objects.filter(status='on tour')
        on_tour_vehicle = on_tour_vehicles.first() if on_tour_vehicles else None
    elif order.status == 'delivered':
        all_vehicles = Vehicle.objects.all()
        random_vehicle = random.choice(all_vehicles) if all_vehicles else None

    return render(request, 'order_detail.html', {'order': order, "articles": articles, "free_vehicles": free_vehicles, 'on_tour_vehicle': on_tour_vehicle, 'random_vehicle': random_vehicle, 'customer_data': customer_data})
