from django.shortcuts import render
from .models import Product


def market(req):
    products = Product.objects.all()
    return render(req, 'tiendaApp/market.html', {'products': products})
