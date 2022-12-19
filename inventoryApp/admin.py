from django.contrib import admin
from .models import Product, Order
# Register your models here.
admin.site.site_header = 'Inventory'


admin.site.register(Product)
admin.site.register(Order)

