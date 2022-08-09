from django.shortcuts import redirect, render
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
            return redirect('/contact/?successful')
    return render(req, 'contactApp/contact.html', {'form': contact_form})
