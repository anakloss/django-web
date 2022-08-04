from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    return render(req, 'webApp/index.html')

def service(req):
    return HttpResponse("Service")

def market(req):
    return HttpResponse("Market")

def blog(req):
    return HttpResponse("Blog")

def contact(req):
    return HttpResponse("Contact")
