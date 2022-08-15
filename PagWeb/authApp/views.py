from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


class registerView(View):
    def get(self, req):
        form = UserCreationForm()
        return render(req, 'authApp/register.html', {'form': form})
    
    def post(self, req):
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(req, form.error_messages[msg])
            return render(req, 'authApp/register.html', {'form': form})