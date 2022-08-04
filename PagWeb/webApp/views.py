from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    return render(req, 'webApp/index.html')

def service(req):
    return render(req, 'webApp/service.html')

def market(req):
    return render(req, 'webApp/market.html')

def blog(req):
    return render(req, 'webApp/blog.html')

def contact(req):
    return render(req, 'webApp/contact.html')