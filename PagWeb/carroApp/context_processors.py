
def total_cart(request):
    total = cant = 0
    if request.user.is_authenticated:
        for key, value in request.session['carro'].items():
            total += value['product_price']
            cant += 1
    return {'total_cart': total, 'total_cant': cant}