from django.http import HttpRequest
from django.template.response import TemplateResponse

def view_vehicles(request: HttpRequest):
    context = {
        "someValue": "this is a value"
    }
    return TemplateResponse(request, 'vehicle.html', context = context)