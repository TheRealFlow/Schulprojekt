from django.shortcuts import render, get_object_or_404
from versandplanung.orders.models import Orders


def order_detail(request, order_id):
    order = get_object_or_404(Orders, id=order_id)

    articles = []
    for article in order.articles:
        for key, items in article.items():
            articles.append(list([key, items]))

    return render(request, 'order_detail.html', {'order': order, "articles": articles})

