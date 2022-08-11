from django.shortcuts import render, redirect
from .carro import Cart
from tiendaApp.models import Product


def add_product(req, product_id):
    carro = Cart(req)
    product = Product.objects.get(id=product_id)
    carro.addProduct(product=product)
    return redirect('market')

def del_product(req, product_id):
    carro = Cart(req)
    product = Product.objects.get(id=product_id)
    carro.delProduct(product=product)
    return redirect('market')

def sub_product(req, product_id):
    carro = Cart(req)
    product = Product.objects.get(id=product_id)
    carro.subProduct(product=product)
    return redirect('market')

def empty_cart(req, product_id):
    carro = Cart(req)
    carro.emptyCart()
    return redirect('market')