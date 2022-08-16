from django.contrib import admin
from .models import Order, OrderLine


class OrderAdmin(admin.ModelAdmin):
    readonly_fields=('created_at',)

class OrderLineAdmin(admin.ModelAdmin):
    readonly_fields=('created_at',)
    list_display=['user', 'amount']

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
