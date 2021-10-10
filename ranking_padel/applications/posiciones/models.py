# from django.db import models

# # Local
# from applications.jugadores.models import *
# from applications.torneos.models import *
# from applications.puntos.models import *
# # Create your models here.


# class Posiciones(models.Model):
#     id = models.BigAutoField(db_column='ID', primary_key=True)

#     jugador_id = models.ForeignKey(Jugador,
#                                 verbose_name='Jugador',
#                                 on_delete=models.DO_NOTHING,
#                                 blank=True
#                                 )

#     torneo_id = models.ForeignKey(Torneo,
#                                 verbose_name= Torneo.nombre_torneo,
#                                 on_delete=models.DO_NOTHING,
#                                 blank=True
#                                 )
    
#     puntos = models.ForeignKey(Puntos,
#                                 verbose_name='Puntos' ,
#                                 on_delete=models.DO_NOTHING,
#                                 blank=True
#                                 )

#     class Meta:
#         db_table = 'torneo'

#     def __str__(self):
#         return f'{self.nombre_torneo}'