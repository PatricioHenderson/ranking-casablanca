from django.contrib import admin

# Locals
from applications.jugadores.models import *

# Register your models here.

@admin.register(Jugador)
class jugador_listAdmin(admin.ModelAdmin):
    search_fields = ['nombre_jugador']
    list_display = ['nombre_jugador' , 'apellido_jugador' , 'sobre_nombre_jugador' , 'foto_jugador']
    
