from django.shortcuts import render
from .models import Service, Staff


def about(req):
    servicios = Service.objects.all()
    personal = Staff.objects.all()
    return render(req, 'serviceApp/about.html', {'servicios': servicios, 'staff': personal})
