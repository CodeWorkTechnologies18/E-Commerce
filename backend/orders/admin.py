from django.contrib import admin
from .models import Order
from .models import OrderItem

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'updated_at']
    list_display_links = ['id', 'user']


admin.site.register(OrderItem)

