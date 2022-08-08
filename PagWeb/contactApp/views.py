from django.shortcuts import render


def contact(req):
    return render(req, 'contactApp/contact.html')
