from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from webApp import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('faq/', views.faq, name='FAQ'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)