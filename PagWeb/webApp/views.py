from django.shortcuts import render


def home(req):
    return render(req, 'webApp/index.html')

def faq(req):
    return render(req, 'webApp/faq.html')