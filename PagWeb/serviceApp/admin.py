from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=['title', 'content']

admin.site.register(Service, ServiceAdmin)
