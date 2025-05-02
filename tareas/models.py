from django.db import models

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(
        max_length=200,
        verbose_name='Título',
        help_text='El título de la tarea'
    )
    descripcion = models.TextField(
        verbose_name='Descripción',
        help_text='Descripción detallada de la tarea'
    )
    estado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
    
