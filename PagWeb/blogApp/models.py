from django.db import models
from django.contrib.auth.models import User


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


class Post(models.Model):
    title = models.CharField(verbose_name='Título', max_length=50)
    content = models.CharField(verbose_name='Contenido', max_length=300)
    image = models.ImageField(verbose_name='Imagen', upload_to='serviceApp', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    created = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Actualizado', auto_now_add=True)
    
    # model meta options
    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
    
    def __str__(self):
        return self.title