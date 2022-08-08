from django.shortcuts import render
from .models import Post, Category


def blog_home(req):
    posts = Post.objects.all()
    return render(req, 'blogApp/blog-home.html', {'posts': posts})

def blog_post(req):
    return render(req, 'blogApp/blog-post.html')

def category(req, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(categories=category)
    return render(req, 'blogApp/categories.html', {'category': category, 'posts': posts})