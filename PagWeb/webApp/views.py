from django.shortcuts import render


def home(req):
    return render(req, 'webApp/index.html')

def market(req):
    return render(req, 'webApp/market.html')

def contact(req):
    return render(req, 'webApp/contact.html')

def faq(req):
    return render(req, 'webApp/faq.html')