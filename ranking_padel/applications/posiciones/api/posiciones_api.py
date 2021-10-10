# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view,  permission_classes

# NOTE: Ejemplo de hello world con método GET
@api_view(['GET'])
def posiciones(request):
    template = '<h1>Hello world Django APIs!</h1>' 
    return HttpResponse(template)