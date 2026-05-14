from django.db import models

class Portfolio(models.Model):   # Mantengo el nombre que usas
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(
        verbose_name="Imagen",
        upload_to="portfolio",   # Carpeta dentro de MEDIA_ROOT
        null=True,
        blank=True
    )
    enlace = models.URLField(verbose_name="Enlace", blank=True, null=True)
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de edición", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Portafolio"
        verbose_name_plural = "Portafolios"
        ordering = ["-created"]
        db_table = "portfolio"


class Tarea(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    archivo = models.FileField(upload_to="tareas/")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        db_table = "tareas"
