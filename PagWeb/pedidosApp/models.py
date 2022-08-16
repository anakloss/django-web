from django.db import models
from django.contrib.auth import get_user_model
from tiendaApp.models import Product
from django.db.models import F, Sum, FloatField


_user = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(_user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        return self.linea_pedido_set.aggregate(
            total = Sum(F("price") * F("amount"), output_field=FloatField())
        )["total"]

    class Meta:
        db_table = 'pedido'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']


class OrderLine(models.Model):
    user = models.ForeignKey(_user, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} unid de {self.product.name}"
    
    class Meta:
        db_table = 'linea_pedido'
        verbose_name = 'Línea pedido'
        verbose_name_plural = 'Lineas pedidos'
        ordering = ['id']