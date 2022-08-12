from django.urls import path
from . import views

app_name = 'carro'

urlpatterns = [
    path('add/<int:product_id>', views.add_product, name='agregar'),
    path('del/<int:product_id>', views.del_product, name='eliminar'),
    path('sub/<int:product_id>', views.sub_product, name='restar'),
    path('empty/', views.empty_cart, name='limpiar'),
]