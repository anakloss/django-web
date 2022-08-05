from django.contrib import admin
from .models import Service, Staff


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=['title', 'content']

class StaffAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display=['name', 'position']

admin.site.register(Service, ServiceAdmin)
admin.site.register(Staff, StaffAdmin)
