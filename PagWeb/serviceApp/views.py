from django.shortcuts import render
from .models import Service


def about(req):
    servicios = Service.objects.all()
    return render(req, 'serviceApp/about.html', {'servicios': servicios})
