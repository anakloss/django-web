from tabnanny import verbose
from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    # model meta options
    class Meta:
        verbose_name='service'
        verbose_name_plural='services'
    
    def __str__(self):
        return self.title