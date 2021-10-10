from django.db import models

# Create your models here.

class Torneo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    nombre_torneo = models.TextField(verbose_name='Torneo')

    class Meta:
        managed = False
        db_table = 'torneo'

    def __str__(self):
        return f'{self.nombre_torneo}'