from django.urls import path
from applications.posiciones.api.posiciones_api import *


urlpatterns = [
    path('posiciones/',posiciones),
]