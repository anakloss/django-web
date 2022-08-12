from django.shortcuts import render

def login(req):
    return render(req, 'authApp/login.html')

