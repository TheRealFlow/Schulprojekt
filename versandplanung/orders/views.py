from django.http import HttpRequest
from django.template.response import TemplateResponse

def view_orders(request: HttpRequest):
    context = {
        "someValue": "this is a value"
    }
    return TemplateResponse(request, 'orders.html', context = context)