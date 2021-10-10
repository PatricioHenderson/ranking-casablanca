from django.db import models

# Local
from applications.jugadores.models import *
from applications.torneos.models import *

# Create your models here.


class Puntos(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)

    jugador_id = models.ForeignKey(Jugador,
                                verbose_name='Jugador',
                                on_delete=models.DO_NOTHING,
                                blank=True
                                )
    
    torneo_id = models.ForeignKey(Torneo,
                                verbose_name='Torneo',
                                on_delete=models.DO_NOTHING,
                                blank=True
                                )

    puntos = models.PositiveIntegerField(
        verbose_name='Puntos',
         default=0)
    

    class Meta:
        db_table = 'Puntos'

    def __str__(self):
        return f'{self.puntos}'