from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm


class loginView(View):
    def get(self, req):
        form = UserCreationForm()
        return render(req, 'authApp/login.html', {'form': form})
    
    def post(self, req):
        pass


# def login(req):
#     return render(req, 'authApp/login.html')

