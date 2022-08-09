from django.shortcuts import render


def market(req):
    return render(req, 'tiendaApp/market.html')
