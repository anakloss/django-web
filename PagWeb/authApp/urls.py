from django.urls import path
from .views import registerView


urlpatterns = [
    path('', registerView.as_view(), name='Register'),
]