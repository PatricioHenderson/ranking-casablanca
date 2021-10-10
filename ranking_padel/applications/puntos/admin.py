from django.contrib import admin

# Local
from applications.puntos.models import *
# Register your models here.


@admin.register(Puntos)
class jugador_listAdmin(admin.ModelAdmin):
    search_fields = ['nombre_jugador']
    list_display = ['jugador_id' , 'torneo_id' , 'puntos']
    