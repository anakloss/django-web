from django.shortcuts import render
from .models import Post


def blog_home(req):
    posts = Post.objects.all()
    return render(req, 'blogApp/blog-home.html', {'posts': posts})

def blog_post(req):
    return render(req, 'blogApp/blog-post.html')
