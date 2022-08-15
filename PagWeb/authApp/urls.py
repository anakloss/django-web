from django.urls import path
from .views import registerView, loginView, logoutView


urlpatterns = [
    path('', registerView.as_view(), name='Register'),
    path('login/', loginView, name='Login'),
    path('logout/', logoutView, name='Logout'),
]