import email
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from .forms import contactForm


def contact(req):
    contact_form = contactForm()

    if req.method == 'POST':
        contact_form = contactForm(data=req.POST)
        if contact_form.is_valid():
            name = req.POST.get('name')
            email = req.POST.get('email')
            phone = req.POST.get('phone')
            msg = req.POST.get('message')

            email = EmailMessage(
                "Mensaje desde AKStart",
                "Usuario: {}\n Teléfono: {}\n Email: {}\n Mensaje:\n\n {}".format(name, phone, email, msg),
                "", ["edna.haley@ethereal.email"], reply_to=[email]
                )
            
            try:
                email.send()
                return redirect('/contact/?successful')
            except:
                return redirect('/contact/?error')
    return render(req, 'contactApp/contact.html', {'form': contact_form})
