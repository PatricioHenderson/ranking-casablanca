from django.urls import path



# Importamos las VIEWS:
from applications.posiciones.views import *

urlpatterns = [
    path('ranking', PosicionesView.as_view()),
    path('ranking2', PosicionesView2.as_view()),
]
