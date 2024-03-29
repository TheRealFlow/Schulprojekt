"""
URL configuration for versandplanung project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from versandplanung.articles.views import view_articles
from versandplanung.customer.views import view_customers
from versandplanung.vehicles.views import view_vehicles
from versandplanung.orders.views import view_orders
from versandplanung.order_detail.views import order_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_orders, name='index'),
    path('articles/', view_articles, name='index'),
    path('customers/', view_customers, name='index'),
    path('vehicles/', view_vehicles, name='index'),
    path('orders/', view_orders, name='index'),
    path('order/<int:order_id>/', order_detail, name='index')
]
