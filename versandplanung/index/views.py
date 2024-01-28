from django.http import HttpRequest
from django.template.response import TemplateResponse

def index_site(request: HttpRequest):
    return TemplateResponse(request, 'index.html')