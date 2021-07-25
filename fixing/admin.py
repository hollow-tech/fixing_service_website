from django.contrib import admin
from .models import Worker, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'order_time', 'type', 'status']


admin.site.register(Worker)
admin.site.register(Order, OrderAdmin)
