from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from carroApp.carro import Cart
from django.conf import settings
from .models import Order, OrderLine


@login_required(login_url="auth/login")
def procesar_pedido(request):
    pedido = Order.objects.create(user=request.user)
    carro = Cart(request)
    lineas_pedido = list()
    for producto in carro.carro:
        lineas_pedido.append(OrderLine(
            user=request.user,
            product_id=carro.carro[producto]['product_id'],
            amount=carro.carro[producto]['product_cant'],
            order_id=pedido.id
        ))
    # Guarda en la tabla de la BD
    OrderLine.objects.bulk_create(lineas_pedido)

    try:
        enviar_mail(pedido=pedido, lineas_pedido=lineas_pedido, username=request.user.username, email=request.user.email)
        messages.success(request, "El pedido se ha creado correctamente")
    except:
        messages.error(request, "Hubo un error al enviar pedido")
    return redirect('Market')


def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "username": kwargs.get("username"),
        "email": kwargs.get("email")
    })
    mensaje_txt=strip_tags(mensaje)
    # from_email="edna.haley@ethereal.email"
    from_email = settings.EMAIL_HOST_USER
    to=kwargs.get("email")
    send_mail(asunto, mensaje_txt, from_email, [to], html_message=mensaje)