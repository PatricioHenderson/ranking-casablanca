from django.contrib import admin

# Locals

from applications.torneos.models import *

# Register your models here.

@admin.register(Torneo)
class torneo_listAdmin(admin.ModelAdmin):
    search_fields = ['nombre_torneo']
    list_display = ['nombre_torneo']
    