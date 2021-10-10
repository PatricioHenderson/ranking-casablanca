from django.db.models.query import QuerySet
from django.shortcuts import render


# Locals
from applications.torneos.models import *
from applications.jugadores.models import *
from applications.puntos.models import *

# Importamos vistas genericas:
from django.views.generic import TemplateView , ListView




 
# Probamos la vista generica:
class PosicionesView(TemplateView):
    template_name = 'posiciones/00-posiciones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nombre_torneo = [Torneo.nombre_torneo ]
        context['nombre_torneo'] = nombre_torneo
        return context



class PosicionesView2(TemplateView):
    # jugadores = Jugador.objects.all()
    # return render (request,'posiciones/01-posiciones.html', {"Jugador":jugadores} )
    # model = Puntos


    template_name = 'posiciones/01-posiciones.html'
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        queryset_jugadores = Jugador.objects.all()
        context['jugador_list'] = queryset_jugadores

        queryset_torneos = Torneo.objects.all()
        context['torneo_list'] = queryset_torneos

        queryset_puntos = Puntos.objects.all()
        context['punto_list'] = queryset_puntos

        return context
