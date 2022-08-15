from django.shortcuts import render
from carroApp.carro import Cart


def home(req):
    carro = Cart(req)
    return render(req, 'webApp/index.html')

def faq(req):
    return render(req, 'webApp/faq.html')