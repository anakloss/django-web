from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
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

def loginView(req):
    if req.method=="POST":
        form = AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(req, user)
                return redirect('Home')
            else:
                messages.error(req, "Ingreso incorrecto")
        else:
            messages.error(req, "Usuario o contraseña no valido")
    
    form = AuthenticationForm()
    return render(req, 'authApp/login.html', {'form': form})

def logoutView(req):
    logout(req)
    return redirect('Home')