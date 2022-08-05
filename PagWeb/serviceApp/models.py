from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models


class Service(models.Model):
    title = models.CharField(verbose_name='Título', max_length=50)
    content = models.CharField(verbose_name='Contenido', max_length=300)
    image = models.ImageField(verbose_name='Imagen', upload_to='serviceApp')
    created = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Actualizado', auto_now_add=True)
    
    # model meta options
    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    
    def __str__(self):
        return self.title