from django.contrib import admin
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=['title', 'author']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
