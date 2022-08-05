from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='Blog home'),
    path('post/', views.blog_post, name='Blog post'),
]