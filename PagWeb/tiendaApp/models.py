from tkinter import image_names
from django.db import models
from matplotlib import image


class Category(models.Model):
    name = models.CharField(verbose_name='Título', max_length=50)
    created = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Actualizado', auto_now_add=True)
    
    # model meta options
    class Meta:
        verbose_name='categoría'
        verbose_name_plural='categorías'
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='Título', max_length=50)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categorias')
    image = models.ImageField(verbose_name='Imagen', upload_to='tiendaApp', null=True, blank=True)
    price = models.FloatField(verbose_name='Precio')
    availability = models.BooleanField(verbose_name='Disponibilidad', default=True)
    created = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Actualizado', auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.name