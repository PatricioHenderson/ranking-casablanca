from django.db import models

# Create your models here.

class Jugador(models.Model):
    id = models.BigAutoField(
        db_column='ID',
        primary_key=True)

    nombre_jugador = models.CharField(
        verbose_name='Nombre',
        max_length=20,
        blank=True)

    apellido_jugador = models.CharField(
        verbose_name='Apellido',
        max_length=20,
        blank=True)

    sobre_nombre_jugador = models.CharField(
        verbose_name='Sobrenombre',
        max_length=20,
        blank=True)

    foto_jugador = models.URLField(
        verbose_name='Link de la foto del jugador',
        max_length=5000,
        blank=True)

    class Meta:
        db_table = 'jugador'

    def __str__(self):
        return f'{self.nombre_jugador + self.apellido_jugador}'