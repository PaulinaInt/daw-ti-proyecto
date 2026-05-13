from django.db import models

class Portfolio(models.Model):   # Nombre de clase con mayúscula
    title = models.CharField(max_length=100)
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name='Imagen', upload_to='portfolio', null=True, blank=True)
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Fecha de edición', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Portafolio'
        verbose_name_plural = 'Portafolios'
        ordering = ['-created']
        db_table = 'portfolio'


class Tarea(models.Model):   # También con mayúscula inicial
    titulo = models.CharField(max_length=100, verbose_name='Título')
    archivo = models.FileField(upload_to='portfolio/')
